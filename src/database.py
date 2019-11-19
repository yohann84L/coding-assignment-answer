#!usr/bin/python
# -*- coding: utf-8 -*-
from src.directed_graph import DirectedGraph
from src.utils import Status
from src.utils import int_size


class Database(object):
    """
    Database class to build a flexible structure to handle day-to-day modification.

    Argument:
    ---------
        - node_id_init (str): id of the top/first node
    """
    def __init__(self, node_id_init: str):
        # Initialize DirectedGraph
        self.__graph = DirectedGraph(node_id_init)
        # Initialize dictionnary of images
        self.__dict_images = dict()

    def add_nodes(self, nodes: list):
        """
        Method to add list of nodes to the database

        Argument:
        ---------
            nodes (list): List of node to add, each node should be (child_node_id, parent_node_id)
        """
        for new_node_id, parent_node_id in nodes:
            if parent_node_id:
                self.__graph.add_node(parent_node_id, new_node_id)
            else:
                print(
                    """You can not add an other core node. 
                    Input should be : list(tuple(child_node_id, parent_node_id), ...)"""
                )
                raise TypeError

    def add_extract(self, img_extracts: dict):
        """
        Method to add image extracts to the dictionnary.

        Argument:
        ---------
            - img_extracts (dict): dictionnary of image name with their node_id
        """
        # Reset all node to non-seen
        self.__graph.reset_state_node()

        # For each image we assign a list of node ids
        for image, node_ids in img_extracts.items():
            if image not in self.__dict_images:
                self.__dict_images[image] = set()
            self.__dict_images[image].update(node_ids)

    def get_extract_status(self):
        """
        Method to get the status of each image

        Return:
        -------
            - out_status (dict): dictionnary with image name as key and their corresponding status as value
        """
        # Initialize output status dict
        out_status = dict()
        # Loop over dictionnary of image
        for image, nodes_id in self.__dict_images.items():
            # Transform list of image into list of status
            nodes_id = list(set(map(self.__img_status, nodes_id)))
            # Sum the list in order to get a number, the number will correspond to a status
            score = sum(nodes_id)

            # switch case of the score obtained
            if int_size(score) == 4:
                out_status[image] = Status.invalid.name
            elif int_size(score) == 3:
                out_status[image] = Status.coverage_staged.name
            elif int_size(score) == 2:
                out_status[image] = Status.granularity_staged.name
            elif int_size(score) == 1:
                out_status[image] = Status.valid.name
            else:
                out_status[image] = "Status not found"

        return out_status

    def __img_status(self, node_id: str):
        """
        Method to get the status of a node

        Argument:
        ---------
            - node_id (str): id of the node we want to get the status

        Return:
        -------
            - status (int): status code of the node
        """
        if self.__graph.get_node(node_id) == -1:
            return Status.invalid.value

        parent_id = self.__graph.get_node(node_id).parent_id
        if self.__graph.get_node(parent_id) != -1:
            children = self.__graph.get_node(parent_id).children_ids
            new_node_bool = any(
                [self.__graph.get_node(child).new_node for child in children]
            )
            if new_node_bool:
                return Status.coverage_staged.value

        if self.__graph.has_child(node_id):
            return Status.granularity_staged.value

        return Status.valid.value
