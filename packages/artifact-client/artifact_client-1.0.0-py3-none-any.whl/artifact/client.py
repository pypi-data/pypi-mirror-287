from openapi_client.api import default_api
from openapi_client.models.create_graph_request import CreateGraphRequest
from openapi_client.models.ingest_document_request import IngestDocumentRequest
from openapi_client.configuration import Configuration
from openapi_client.api_client import ApiClient

class ArtifactClient:
    def __init__(self, api_key: str, base_url: str = "https://xxny160gbe.execute-api.us-east-1.amazonaws.com/Prod"):
        # Configure the client
        config = Configuration(host=base_url)
        config.api_key = {"Authorization": api_key}
        config.api_key_prefix['Authorization'] = 'Bearer'
        self.client = ApiClient(configuration=config)
        self.api_instance = default_api.DefaultApi(api_client=self.client)
        self.api_key = api_key

    def set_auth_headers(self):
        """Set the Authorization header."""
        headers = {'Authorization': f'{self.api_key}'}
        return headers

    def Graph(self, name: str = None, graph_id: str = None, indexing_interval: str = "IMMEDIATE"):
        """Retrieve or create a graph."""
        if graph_id:
            # Connect to an existing graph
            return self.GraphInstance(self, graph_id=graph_id)
        elif name:
            # List all graphs and check if one with the given name already exists
            try:
                graphs = self.list_graphs()
                for graph in graphs:
                    if graph.name == name:
                        # Create from Graph object
                        return self.GraphInstance(self, graph_id=graph.uuid, name=graph.name)
                # If no graph with the given name exists, create a new one
                new_graph = self.create_graph(name=name, indexing_interval=indexing_interval)
                return self.GraphInstance(self, graph_id=new_graph.uuid)
            except Exception as e:
                print(f"Exception during graph retrieval or creation: {e}")
                raise
        else:
            raise ValueError("Either 'name' or 'graph_id' must be provided to retrieve or create a graph.")


    def create_graph(self, name: str, indexing_interval: str = "IMMEDIATE"):
        """Create a new graph."""
        body = CreateGraphRequest(name=name, indexing_interval=indexing_interval)
        headers = self.set_auth_headers()
        response = self.api_instance.create_graph(create_graph_request=body, _headers=headers)
        return response

    def list_graphs(self):
        """Lists all graphs."""
        headers = self.set_auth_headers()
        response = self.api_instance.list_graphs(_headers=headers)
        return response

    def _get_graph_id_by_name(self, name: str):
        """Retrieve the graph ID by its name."""
        graphs = self.list_graphs()
        for graph in graphs:
            if graph.name == name:
                return graph.id
        return None

    class GraphInstance:
        def __init__(self, artifact_client: 'ArtifactClient', name: str = None, graph_id: str = None, indexing_interval: str = "IMMEDIATE"):
            self.artifact_client = artifact_client
            self.name = name
            self.indexing_interval = indexing_interval
            self.graph_id = graph_id

        def ingest(self, document: str):
            """Ingest a document into the graph."""
            body = IngestDocumentRequest(document=document)
            headers = self.artifact_client.set_auth_headers()
            return self.artifact_client.api_instance.ingest_document(graph_id=self.graph_id, ingest_document_request=body, _headers=headers)

        def query(self) -> str:
            """Query the graph."""
            headers = self.artifact_client.set_auth_headers()
            return self.artifact_client.api_instance.query_graph(graph_id=self.graph_id, _headers=headers)

        def stats(self):
            """Get graph statistics."""
            headers = self.artifact_client.set_auth_headers()
            return self.artifact_client.api_instance.get_graph_stats(graph_id=self.graph_id, _headers=headers)