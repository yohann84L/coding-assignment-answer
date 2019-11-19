from collections import defaultdict

class DirGraph:
    def __init__(self, node_id: str):
        self.__node_list = set()
        self.__node_list.add(node_id)
        self.__graph = defaultdict(list)
        self.__graph[node_id] = []

    @property
    def graph(self):
        return self.__graph

    def get_node(self, node_id):
        if node_id not in self.__node_list:
            return -1
        return self.__graph[node_id]

    def add_child(self, node_id, new_node_id):
        self.__node_list.add(new_node_id)
        self.__graph[node_id].append(new_node_id)

    def get_child(self, node):
        return self.__graph[node]

    def has_child(self, node):
        if self.__graph[node]:
            return True
        else:
            return False