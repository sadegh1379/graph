class Graph:

    class Vertex:
        def __init__(self, x):
            self.element = x
            self.visited = False

        def is_visited(self):
            return self.visited

        def element(self):
            return self.element()

        def __hash__(self):
            return hash(id(self))
        
    class Edge:
        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            return (self._origin, self._destination)

        def opposite(self, v):
            return self._destination if v is self._origin else self._origin

        def element(self):
            return self._element

        def __hash__(self):
            return hash((self._origin, self._destination))
        
    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v] for v in self._outgoing))

        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()

        for secondary_map in self._outgoing.values():
            for edge in secondary_map.values():
                result.add(edge)

        return result

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming

        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):

        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        e = self.Edge(u, v, x)

        self._outgoing[u][v] = e
        self._incoming[v][u] = e
    def bfs(self, start_vertex):
        queue = [start_vertex]
        start_vertex.visited = True
        print("BFS ****:")

        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex.element, end=' ')

            for neighbor in self._outgoing[current_vertex]:
                if not neighbor.is_visited():
                    neighbor.visited = True
                    queue.append(neighbor)

    def dfs(self, start_vertex):
        queue = [start_vertex]
        current_vertex = queue.pop(0)
        for neighbor in self._outgoing[current_vertex]:
                if neighbor.is_visited():
                    neighbor.visited = False
                    queue.append(neighbor)
        print("DFS ***:")
        self._dfs(start_vertex)

    def _dfs(self, vertex):
        vertex.visited = True
        print(vertex.element, end=' ')

        for neighbor in self._outgoing[vertex]:
            if not neighbor.is_visited():
                self._dfs(neighbor)
                
g = Graph(directed=1)
n = int(input('Enter vertex number: '))
v = dict()

for i in range (n) :
    name = input('Vertex name : ')
    v[name] = g.insert_vertex(name)

m = int(input('Enter edge number: '))


for i in range(m) :
    yal = input('Please enter vertex like (1 -> 3): ').split()
    v1 = yal[0]
    v2= yal[1]

    g.insert_edge(v[v1] , v[v2])

print("Graph vertices:")
for i in g.vertices():
    print(i.element, end=' ')

print("\nGraph edges:")
for e in g.edges():
    print(f"({e._origin.element}, {e._destination.element})", end=' ')

b1 = input('\nEnter BFS start vertex : ')

g.bfs(v[b1])

d1 = input('\nEnter DFS start vertex :')
g.dfs(v[d1])