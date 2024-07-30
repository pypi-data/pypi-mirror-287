import os
import logging
import requests
import mlflow
from dotenv import load_dotenv
from modelhub.utils import handle_response

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

## create a modelhub client exception
class ModelHubException(Exception):
    """Exception raised for errors in the ModelHub client."""
    
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ModelHub:
    """A client for interacting with the ModelHub API."""

    def __init__(self, base_url, client_id=None, client_secret=None):
        """
        Initializes a ModelHub object.

        Args:
            base_url (str): The base URL of the ModelHub API.
            client_id (str, optional): The client ID for authentication.
            client_secret (str, optional): The client secret for authentication.
        """

        self.base_url = base_url
        self.modelhub_url = f"{base_url}/modelhub/api/v1"
        self.auth_url = f"{base_url}/ums/api/v1"
        self.client_id = client_id or os.getenv("MODELHUB_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("MODELHUB_CLIENT_SECRET")
        self.token = None
        self.headers = {}
        self.get_token()

    def get_token(self):
        """
        Fetches a token using the client credentials flow and stores it in self.token.
        """
        token_endpoint = f"{self.auth_url}/auth/get-token"
        headers = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "content-type": "application/json",
        }
        logger.debug("Getting token from %s", token_endpoint)
        logger.debug("Headers: %s", headers)
        response = requests.post(token_endpoint, headers=headers, timeout=10)
        response_data = handle_response(response)
        # check if token is in response_data
        if "token" in response_data:
            self.token = response_data.get("token").get("access_token")
            self.headers = {"Authorization": f"Bearer {self.token}"}
        else:
            raise ModelHubException("Token not found in response data")

    def request_with_retry(self, method, endpoint, **kwargs):
        """
        Sends a request and retries with a new token if a 401 Unauthorized response is received.

        Args:
            method (str): The HTTP method to use for the request (e.g., 'get', 'post').
            endpoint (str): The endpoint to send the request to.
            **kwargs: Additional arguments to pass to the request method.

        Returns:
            The response from the server.
        """
        url = f"{self.modelhub_url}/{endpoint}"
        response = requests.request(method, url, headers=self.headers, **kwargs, timeout=10)

        if response.status_code == 401:
            self.get_token()
            kwargs["headers"] = self.headers
            response = requests.request(method, url, **kwargs, timeout=10)

        return handle_response(response)

    def post(self, endpoint, json=None, params=None, files=None, data=None):
        """
        Sends a POST request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the request to.
            json (dict, optional): JSON data to send in the request body. Defaults to None.
            params (dict, optional): Query parameters to include in the request. Defaults to None.
            files (dict, optional): Files to upload with the request. Defaults to None.
            data (dict, optional): Data to send in the request body. Defaults to None.

        Returns:
            The response from the server.
        """
        return self.request_with_retry(
            "post", endpoint, json=json, params=params, files=files, data=data
        )

    def get(self, endpoint, params=None):
        """
        Sends a GET request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the request to.
            params (dict, optional): The query parameters to include in the request. Defaults to None.

        Returns:
            The response from the GET request.
        """
        return self.request_with_retry("get", endpoint, params=params)

    def put(self, endpoint, json=None):
        """
        Sends a PUT request to the specified endpoint with the given JSON payload.

        Args:
            endpoint (str): The endpoint to send the request to.
            json (dict, optional): The JSON payload to include in the request. Defaults to None.

        Returns:
            The response from the server.

        Raises:
            Any exceptions raised by the underlying requests library.
        """
        return self.request_with_retry("put", endpoint, json=json)

    def delete(self, endpoint):
        """
        Sends a DELETE request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the DELETE request to.

        Returns:
            The response from the server.

        Raises:
            Exception: If there is an error in sending the request or handling the response.
        """
        return self.request_with_retry("delete", endpoint)

    def mlflow(self):
        """
        Configures the MLflow tracking and registry URIs and sets environment variables for authentication.

        Returns:
            The configured mlflow object.
        """
        response = self.get("mlflow/tracking_uri")
        tracking_uri = response.get("tracking_uri")
        mlflow.set_tracking_uri(tracking_uri)

        response = self.get("mlflow/credentials")
        username = response.get("username")
        password = response.get("password")

        if username and password:
            mlflow.set_tracking_uri(tracking_uri)
            mlflow.set_registry_uri(tracking_uri)
            os.environ["MLFLOW_TRACKING_USERNAME"] = username
            os.environ["MLFLOW_TRACKING_PASSWORD"] = password

        return mlflow
