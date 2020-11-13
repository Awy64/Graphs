"""
Simple graph implementation
"""
# from util import Stack, Queue  # These may come in handy
from collections import deque

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        else:
            print("vert exist already")
            return

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 and v2 not in self.vertices:
            print("one or more of this vert's do not exist")
        self.vertices[v1].add(v2)
        

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id not in self.vertices:
            print("this vert does not exist")
            return
        return self.vertices[vertex_id]
        

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        stack = deque()
        found = set()
        if starting_vertex not in self.vertices:
            print("this vert does not exist")
            return
        stack.append(starting_vertex)
        while stack:
            currVert = stack.popleft()
            if currVert not in found:
                found.add(currVert)
                print(currVert)
                for i in self.vertices[currVert]:
                    stack.append(i)
            else:
                continue




    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = deque()
        found = set()
        if starting_vertex not in self.vertices:
            print("this vert does not exist")
            return
        stack.append(starting_vertex)
        while stack:
            currVert = stack.pop()
            if currVert not in found:
                found.add(currVert)
                print(currVert)
                for i in self.vertices[currVert]:
                    stack.append(i)
            else:
                continue

    def dft_util(self, vert, visit):
        visit[vert] = True
        print(vert)
        for i in self.vertices[vert]:
            if visit[i] == False:
                self.dft_util(i, visit)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        found = [False] * (max(self.vertices) + 1)
        self.dft_util(starting_vertex, found)

    


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        stack = deque()
        found = set()
        if starting_vertex not in self.vertices:
            print("this vert does not exist")
            return
        stack.append([starting_vertex])
        while stack:
            currPath = stack.popleft()
            currVert = currPath[-1]
            if currVert == destination_vertex:
                return currPath
            if currVert not in found:
                found.add(currVert)
                print(currVert)
                for i in self.vertices[currVert]:
                    newPath = list(currPath)
                    newPath.append(i)
                    stack.append(newPath)
            else:
                continue

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = deque()
        found = set()
        if starting_vertex not in self.vertices:
            print("this vert does not exist")
            return
        stack.append([starting_vertex])
        while stack:
            currPath = stack.pop()
            currVert = currPath[-1]
            if currVert == destination_vertex:
                return currPath
            if currVert not in found:
                found.add(currVert)
                for i in self.vertices[currVert]:
                    newPath = list(currPath)
                    newPath.append(i)
                    stack.append(newPath)
            else:
                continue

    def dfs_util(self, vert, visit, dest, path):
        visit[vert] = True
        for i in self.vertices[vert]:
            if visit[i] == False:
                return self.dfs_util(i, visit, dest, path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path = deque()
        found = [False] * (len(self.vertices))
        self.dfs_util(starting_vertex, found, destination_vertex, path)
        return list(path)
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
