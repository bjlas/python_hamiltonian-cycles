PYTHON HAMILTONIAN CYCLES
===========

A Phyton program to create graphs, nodes, edges and calculate the possible Hamiltonian cycles:
https://en.wikipedia.org/wiki/Hamiltonian_path

Made to calculate a Secret Santa draw.

#Create graph
```graph = Graph()```

#Create node
```finn = Node(name='Finn')```

#Add node to the graph
```graph.addNode(finn)```

#Add edge to the nodes
```
jake.addEge(gunter)
jake.addEge(lsp)
```

#Calculate hamyltonian cycles
``` allPaths = graph.search_hamiltonian_cycles(finn, print=True) ```

Where parameters are:
* first: Start node for search
* second: True/False for print in console the results

## Example Graph
![Alt text](exampleGraph.png?raw=true "Example Graph")

In that case the app will return two Hamiltonian cycles:

Path 1:
`[Finn][Jake][Gunter][Ice King][lsp][Finn]` 

Path 2:
`[Finn][Jake][lsp][Gunter][Ice King][Finn]` 

