# Python program for implementing BFS

from collections import defaultdict

class BreadthFirstSearch:

        def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, node, edge):
        self.graph[node].append(edge)

    def bfs(self, startVertex):
        visited = [];
        queue = [];
        visited.append(startVertex)
        queue.append(startVertex)

        while len(queue) != 0:
            node = queue.pop(0)
            print(node)
            for i in self.graph[node]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)

g = BreadthFirstSearch()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
print ("Following is Breadth First Traversal (starting from vertex 2)")
g.bfs(2)
