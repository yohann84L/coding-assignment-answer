#!usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from src.directed_graph import DirectedGraph


class DirectedGraphTest(unittest.TestCase):
    @staticmethod
    def build_graph():
        """
        Function to build a graph in order to make some test
        """
        build = [("A", "core"), ("B", "core"), ("C", "core"), ("C1", "C"), ("C2", "C")]
        graph = DirectedGraph("core")
        for new_node, parent in build:
            graph.add_node(parent, new_node)
        return graph

    def test_get_children(self):
        """
        Method to test the function get_children()
        """
        # Reference
        ref_children = {"C1", "C2"}

        # Get children
        children = self.build_graph().get_children("C")

        # Test
        self.assertEqual(ref_children, children)

    def test_has_child_true(self):
        """
        Method to test the function has_child()
        """
        # Reference
        ref_has_child = True

        # Get children
        children = self.build_graph().has_child("C")

        # Test
        self.assertEqual(ref_has_child, children)

    def test_has_child_false(self):
        """
        Method to test the function has_child()
        """
        # Reference
        ref_has_child = False

        # Get children
        children = self.build_graph().has_child("B")

        # Test
        self.assertEqual(ref_has_child, children)

    def test_reset_state_node(self):
        """
        Method to test the function reset_state_node()
        """
        # Reference
        ref_state_node_1 = True
        ref_state_node_2 = False

        # Get children
        G = self.build_graph()
        state_node_1 = G.get_node("C").new_node
        G.reset_state_node()
        state_node_2 = G.get_node("C").new_node

        # Test
        self.assertEqual(
            [ref_state_node_1, ref_state_node_2], [state_node_1, state_node_2]
        )


if __name__ == "__main__":
    unittest.main()
