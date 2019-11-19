#!usr/bin/python
# -*- coding: utf-8 -*-
from src.directed_graph import DirGraph
from src.status import Status
from src.utils import int_size


class Database(object):
    def __init__(self, node_id_init: str):
        self.__graph = DirGraph(node_id_init)
        self.__dict_images = dict()

    def add_nodes(self, nodes):
        for new_node_id, parent_node_id in nodes:
            if parent_node_id:
                self.__graph.add_node(parent_node_id, new_node_id)
            else:
                print(
                    """You can not add an other code node. 
                    Input should be : list(tuple(label_child_node, label_parent_node), ...)"""
                )
                raise TypeError

    def add_extract(self, img_extracts: dict):
        self.__graph.reset_state_node()
        for image, nodes_id in img_extracts.items():
            if image not in self.__dict_images:
                self.__dict_images[image] = set()
            self.__dict_images[image].update(nodes_id)

    def get_extract_status(self):
        out_status = dict()
        for image, nodes_id in self.__dict_images.items():
            nodes_id = list(set(map(self.__img_status, nodes_id)))
            score = sum(nodes_id)
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

    def __img_status(self, node_id):
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
