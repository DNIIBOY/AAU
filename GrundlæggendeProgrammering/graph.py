import unittest

g1 = {"a": ["c"], "c": ["a", "b"], "b": ["c"]}
g2 = {
    "a": ["a", "b", "c", "d"],
    "b": ["a", "b", "c", "d"],
    "c": ["a", "b", "c", "d"],
    "d": ["a", "b", "c", "d"]
}

g3 = {
    "a": ["c", "d", "f"],
    "b": ["d", "e", "g"],
    "c": ["a", "e", "h"],
    "d": ["a", "b", "i"],
    "e": ["b", "c", "j"],
    "f": ["a", "j", "g"],
    "g": ["b", "f", "h"],
    "h": ["c", "g", "i"],
    "i": ["d", "h", "j"],
    "j": ["e", "f", "i"],
}


def generate_edges(graph):
    edges = set()
    for node in graph:
        for neighbour in graph[node]:
            if (neighbour, node) not in edges:
                edges.add((node, neighbour))

    return list(edges)


def get_degrees(graph):
    degrees = {}
    for node in graph:
        degree = 0
        edges = set(graph[node])
        if node in edges:
            degree += 2
            edges.remove(node)
        degree += len(edges)
        degrees[node] = degree

    return degrees


def handshake_lemma(graph: list[dict]) -> tuple[int, int]:
    """
    This function calculates the sum of the degrees of all the nodes in a graph
    and twice the number of edges in the graph using the Handshake Lemma.
    :param graph: A graph represented as a dictionary
    :return: A tuple containing the sum of the degrees of all the nodes in the graph
    and twice the number of edges in the graph
    """
    return sum(get_degrees(graph).values()), 2 * len(generate_edges(graph))


class TestGenerateEdges(unittest.TestCase):
    def test_graph_1(self):
        self.assertCountEqual(generate_edges(g1), [("a", "c"), ("c", "b")])

    def test_graph_2(self):
        self.assertCountEqual(
            generate_edges(g2),
            [("b", "c"), ("a", "b"), ("d", "d"), ("a", "c"), ("b", "b"),
             ("c", "d"), ("c", "c"), ("a", "a"), ("a", "d"), ("b", "d")]
        )

    def test_graph_3(self):
        self.assertEqual(len(generate_edges(g3)), 15)
        self.assertCountEqual(
            generate_edges(g3),
            [
                ("i", "j"),
                ("a", "d"),
                ("h", "i"),
                ("b", "g"),
                ("f", "j"),
                ("d", "i"),
                ("b", "e"),
                ("b", "d"),
                ("f", "g"),
                ("c", "e"),
                ("g", "h"),
                ("a", "f"),
                ("a", "c"),
                ("e", "j"),
                ("c", "h"),
            ]
        )


class TestGetDegrees(unittest.TestCase):
    def test_graph_1(self):
        self.assertDictEqual(get_degrees(g1), {"a": 1, "c": 2, "b": 1})

    def test_graph_2(self):
        self.assertDictEqual(get_degrees(g2), {"a": 5, "b": 5, "c": 5, "d": 5})

    def test_graph_3(self):
        self.assertDictEqual(
            get_degrees(g3),
            {
                "a": 3,
                "b": 3,
                "c": 3,
                "d": 3,
                "e": 3,
                "f": 3,
                "g": 3,
                "h": 3,
                "i": 3,
                "j": 3,
            }
        )


class TestHandshakeLemma(unittest.TestCase):
    def test_graph_1(self):
        sum_degrees, double_num_edges = handshake_lemma(g1)
        self.assertEqual(sum_degrees, double_num_edges)

    def test_graph_2(self):
        sum_degrees, double_num_edges = handshake_lemma(g2)
        self.assertEqual(sum_degrees, double_num_edges)

    def test_graph_3(self):
        sum_degrees, double_num_edges = handshake_lemma(g3)
        self.assertEqual(sum_degrees, double_num_edges)


if __name__ == "__main__":
    unittest.main()
