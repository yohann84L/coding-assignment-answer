from collections import defaultdict

class Node:
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
        self.__children_ids.add(child_id)

class DirGraph:
    def __init__(self, node_id: str):
        self.__node_list = set()
        self.__node_list.add(node_id)

        self.__graph = defaultdict(Node)
        self.__graph[node_id] = Node('null', node_id)

    @property
    def graph(self):
        return self.__graph

    def get_node(self, node_id):
        if node_id not in self.__node_list:
            return -1
        return self.__graph[node_id]

    def add_node(self, parent_id, new_node_id):
        self.__node_list.add(new_node_id)

        if parent_id in self.__graph.keys():
            self.__graph[parent_id].add_child(new_node_id)

        self.__graph[new_node_id] = Node(parent_id, new_node_id)

    def get_children(self, node):
        return self.__graph[node].children_ids

    def has_child(self, node):
        if self.__graph[node].children_ids:
            return True
        else:
            return False

    def reset_state_node(self):
        for node_id in self.__graph.keys():
            self.__graph[node_id].new_node = False
