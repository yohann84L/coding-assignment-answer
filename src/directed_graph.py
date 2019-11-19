#!usr/bin/python
# -*- coding: utf-8 -*-
from collections import defaultdict


class DirectedGraph:
    """
    DirectedGraph class: Define a Directed Graph, containing a list with all unique node in the graph and all Node (object).
    Argument:
    ---------
        - node_id (str): id of the first (top) node
    """

    def __init__(self, node_id: str):
        # Set up a set to store all unique node_id of the graph
        self.__node_list = set()
        self.__node_list.add(node_id)

        # Initialize the graph with the top node
        self.__graph = defaultdict(Node)
        self.__graph[node_id] = Node("null", node_id)

    @property
    def graph(self):
        return self.__graph

    def get_node(self, node_id):
        """
        Getter method to get a node based on it's id.
        Argument:
        Argument:
        ---------
            - node_id (str): id of the node to get
        Return:
        -------
            - Node object
        """
        # Check the node exist
        if node_id not in self.__node_list:
            return -1
        return self.__graph[node_id]

    def add_node(self, parent_id, new_node_id):
        """
        Method to add new node to the graph
        Arguments:
        ---------
            - parent_id (str): id of the parent
            - new_node_id (str): id of the new node to add
        """
        # Add unique node_id
        self.__node_list.add(new_node_id)

        # Check if node exist and add new_node as children if true
        if parent_id in self.__graph.keys():
            self.__graph[parent_id].add_child(new_node_id)

        # Add the node
        self.__graph[new_node_id] = Node(parent_id, new_node_id)

    def get_children(self, node_id):
        """
        Method to get the children of a node
        Argument:
        ---------
            node_id (str): id of the node we want to get the children
        Return:
        -------
            children_ids (list): list of ids of node
        """
        return self.__graph[node_id].children_ids

    def has_child(self, node_id):
        """
        Method to know of a node have child
        Argument:
        ---------
            node_id (str): id of the node we want to know if have child
        Return:
        -------
            boolean: true if node have child, false else
        """
        if self.__graph[node_id].children_ids:
            return True
        else:
            return False

    def reset_state_node(self):
        """
        Method to reset all node to not new
        """
        for node_id in self.__graph.keys():
            self.__graph[node_id].new_node = False


class Node:
    """
    Class Node: Define a node in a graph, contain parent, children and a boolean to know at $t'$ if the node is a new node.

    Arguments:
    ----------
        - parent_id (str): id of the parent
        - node_id (str): id of the node
    """

    def __init__(self, parent_id: str, node_id: str):
        self.__parent_id = parent_id
        self.__node_id = node_id
        self.__children_ids = set()
        self.__new_node = True

    @property
    def children_ids(self):
        return self.__children_ids

    @property
    def parent_id(self):
        return self.__parent_id

    @property
    def node_id(self):
        return self.__node_id

    @property
    def new_node(self):
        return self.__new_node

    @new_node.setter
    def new_node(self, new_node: bool):
        self.__new_node = new_node

    def add_child(self, child_id: str):
        """
        Method to add a child to the self node.
        Argument:
        ---------
            - child_id (str): id of the child to add
        """
        self.__children_ids.add(child_id)
