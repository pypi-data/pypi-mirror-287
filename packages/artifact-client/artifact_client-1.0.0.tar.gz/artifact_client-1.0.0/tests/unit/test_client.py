import unittest
from artifact.client import ArtifactClient


class TestArtifactClient(unittest.TestCase):

    def setUp(self):
        self.api_key = "0fa8f115-847f-4d25-a686-63aa1ed2b1ed"
        self.client = ArtifactClient(api_key=self.api_key)

    def test_create_graph(self):
        graph_id = self.client.create_graph(name="TestGraph", indexing_interval="HOURLY")
        self.assertIsNotNone(graph_id)

    def test_list_graphs(self):
        graphs = self.client.list_graphs()
        self.assertIsNotNone(graphs)

    @unittest.skip("Skipping this test for now")
    def test_ingest_document(self):
        graph = self.client.Graph(name="TestGraph")
        response = graph.ingest(document="sample document")

        self.assertIsNotNone(response)

    @unittest.skip("Skipping this test for now")
    def test_query_graph(self):
        graph = self.client.Graph(name="TestGraph")
        result = graph.query()

        self.assertIsNotNone(result)

    def test_get_graph_stats(self):
        graph = self.client.Graph(name="TestGraph")
        stats = graph.stats()

        self.assertEqual(stats.edge_count, 0)
        self.assertEqual(stats.node_count, 0)

if __name__ == '__main__':
    unittest.main()