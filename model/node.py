class Node:
    def __init__(self, name ):
        self.name = name
        self.edges = []

    def addEge(self, node):
        self.edges.append(node)

    def __str__(self):
        return self.name
