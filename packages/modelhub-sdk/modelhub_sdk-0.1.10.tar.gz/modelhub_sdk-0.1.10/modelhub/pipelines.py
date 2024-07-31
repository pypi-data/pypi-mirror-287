import yaml
import networkx as nx
import matplotlib.pyplot as plt
from modelhub.models import PipelineCreateRequest, Stage


class Pipeline:
    """ A class to create and manage machine learning pipelines on ModelHub."""
    def __init__(self, modelhub_client, config_path):
        self.modelhub_client = modelhub_client
        self.config_path = config_path
        self.pipeline_request = self.load_config(config_path)

    def load_config(self, config_path):
        """Load pipeline configuration from a YAML file."""
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        return PipelineCreateRequest(**config)

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
            G.add_node(stage.name, label=stage.name)
            for dependency in stage.depends_on:
                G.add_edge(dependency, stage.name)

        pos = nx.spring_layout(G)
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=3000,
            node_color="lightblue",
            font_size=10,
            font_weight="bold",
            arrowsize=20,
        )
        plt.show()
        return G

    def inspect(self):
        """Inspect the pipeline configuration."""
        self.generate_dag_view()
