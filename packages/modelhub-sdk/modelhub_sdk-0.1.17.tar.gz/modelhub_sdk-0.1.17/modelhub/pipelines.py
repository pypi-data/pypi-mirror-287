import os
import yaml
import networkx as nx
from modelhub.models import PipelineCreateRequest
import base64


class Pipeline:
    """A class to create and manage machine learning pipelines on ModelHub."""

    def __init__(self, modelhub_client, config_path):
        self.modelhub_client = modelhub_client
        self.config_path = config_path
        self.pipeline_request = self.load_config(config_path)

    def load_config(self, config_path):
        """Load pipeline configuration from a YAML file."""
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        for stage in config["stages"]:
            if "script" in stage and stage["script"]:
                stage["script"] = self.encode_file(stage["script"])
            if "requirements" in stage and stage["requirements"]:
                stage["requirements"] = self.encode_file(stage["requirements"])

        return PipelineCreateRequest(**config)

    def encode_file(self, file_path):
        """Encode the contents of a file in Base64."""
        with open(file_path, "rb") as file:
            encoded = base64.b64encode(file.read()).decode("utf-8")
        return encoded

    def create_or_update(self):
        """Create or update a pipeline based on the configuration."""
        existing_pipeline = self.modelhub_client.search_pipeline(
            self.pipeline_request.name
        )
        if existing_pipeline:
            return self.modelhub_client.put(
                f"pipelines/{existing_pipeline['pipeline_id']}",
                json=self.pipeline_request.dict(),
            )
        else:
            return self.modelhub_client.post(
                "pipelines", json=self.pipeline_request.dict()
            )

    def submit(self):
        response = self.create_or_update()
        pipeline_id = response["pipeline_id"]
        return self.modelhub_client.post(f"pipelines/{pipeline_id}/submit")

    def generate_dag_view(self):
        stages = self.pipeline_request.stages
        G = nx.DiGraph()

        for stage in stages:
            G.add_node(stage.name)
            for dependency in stage.depends_on:
                G.add_edge(dependency, stage.name)

        try:
            from networkx.drawing.nx_agraph import graphviz_layout
            import matplotlib.pyplot as plt
            from matplotlib import get_backend

            # Ensure the matplotlib backend is set correctly
            if get_backend() != "module://matplotlib_inline.backend_inline":
                plt.switch_backend("module://matplotlib_inline.backend_inline")

            pos = graphviz_layout(G, prog="dot")
            plt.figure(figsize=(12, 8))
            nx.draw(
                G,
                pos,
                with_labels=True,
                node_size=3000,
                node_color="lightblue",
                font_size=10,
                font_weight="bold",
                arrows=True,
                arrowsize=20,
            )
            plt.show()
        except ImportError:
            print(
                "matplotlib and pygraphviz are required for DAG visualization. Please install them using 'pip install matplotlib pygraphviz'."
            )

    def inspect(self):
        """Inspect the pipeline configuration."""
        self.generate_dag_view()
