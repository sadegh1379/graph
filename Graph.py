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
        
    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

g = Graph()