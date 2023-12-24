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

g = Graph()