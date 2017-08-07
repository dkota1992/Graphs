from graphClass import Vertex, Graph

a = Graph()

a.addVertex("Vijayawada")
a.addVertex("Eluru")
a.addVertex("Gunturu")
a.addVertex("Hyderabad")
a.addVertex("Vizag")

a.addEdge("Vijayawada", "Eluru",60)
a.addEdge("Vijayawada", "Gunturu",50)
a.addEdge("Vijayawada", "Hyderabad",460)
a.addEdge("Vijayawada", "Vizag",360)
a.addEdge("Vijayawada", "Bhimavaram",95)
a.addEdge("Bhimavaram","Eluru",95)
a.addEdge("Bhimavaram","Eluru",40)
a.addEdge("Bhimavaram","Vizag",395)
a.addEdge("Bhimavaram","Gunturu",195)

print(a.vertList["Vijayawada"])