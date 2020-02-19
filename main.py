from model.node import Node
from model.graph import Graph

print("START")

#Create empty graph
graph = Graph()

#Create a node
finn = Node(name='Finn')

#Add that node to the graph
graph.addNode(finn)

#Create and Add to the graph in one step
jake = graph.addNode(name='Jake')
iceking = graph.addNode(name='Ice King')
gunter = graph.addNode('Gunter')
lsp = graph.addNode('lsp')

#Add edges to the nodes
finn.addEge(jake)
jake.addEge(gunter)
jake.addEge(lsp)
gunter.addEge(iceking)
iceking.addEge(lsp)
iceking.addEge(finn)
lsp.addEge(finn)
lsp.addEge(gunter)

#Calculate hamyltonian cycles
allPaths = graph.search_hamiltonian_cycles(finn, print=True)


print("END")

