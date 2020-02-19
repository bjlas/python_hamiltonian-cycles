from model.node import Node

class Graph:
    def __init__(self):
        self.nodes=[]

    def addNode(self, node):
        self.nodes.append(node)

    def addNode(self, name):
        newNode = Node(name=name)
        self.nodes.append(newNode)
        return newNode

    def search_hamiltonian_cycles(self, start, print=bool):
        cycles = self.find_hamiltonian(start, visited=[], cycles=[])
        if print is True:
            self.printPaths(cycles)
        return cycles


    def find_hamiltonian(self, current, visited, cycles):
        if current not in visited:
            visited.append(current)
            if (len(visited) == len(self.nodes) and visited[0] in current.edges):
                cycle = visited.copy()
                cycle.append(visited[0]) #add first node to close the path
                cycles.append(cycle)
            else:
                for edge in current.edges:
                    self.find_hamiltonian(edge, visited, cycles)
            visited.remove(current)
        return cycles

    def printPaths(self, allPaths):
        if len(allPaths)>0:
            for index, path in enumerate(allPaths):
                print("\n Path %s:" % (index+1))
                for node in path:
                        print("[%s]" % (node.name), end='')
            print("\n")
        else:
            print("No solution")

