# graph.py

__author__ = "Christian Pedrigal"
__email__ = "cpedrigal@scu.edu"
__date__ = "2024/07/24"
__version__ = "0.0.1"
__license__ = "CC BY-NC-SA 4.0"
__description__ = "Finds shortest cycle using Dijkstra's"

from typing import List, Dict, Union, Optional
import heapq 

import networkx as nx 
import matplotlib.pyplot as plt 


Id = Union[str, int]
Numeric = Union[float, int, complex]


class Vertex:

    def __init__(self, id: Id):

        # Identification
        self.id: Id = id
        self.nid: int = -1

        # List of neighbor vertices
        self.neighbors: List[List[int]] = list()

        # Previous vertex (during traversal)
        self.prev_vertex: Vertex = None
        
        # Distance associated (during SPT algo)
        self.dist = float('inf')

        # connected component number (during traversal)
        self.CC_num: int = None

        # pre- and post-number (during traversal)
        self.prev: int = -1
        self.post: int = -1


    def add_neighbor(self, vertex, w: Numeric = 0):
        if id not in self.neighbors:
            self.neighbors.append([vertex, w])

    @property
    def degree(self):
        return len(self.neighbors)
        

class Graph:
    def __init__(self, is_directed: bool = True, is_weighted: bool = True):

        # DS for vertices (and optional weights associated)
        self.adj_list: Dict[int, List[int, Optional[int]]] = dict()
        
        # numeric ID system for vertices (accounts for non-integer vertices)
        self.ID_cnt: int = 0
        self.ID_to_vertex: Dict[int, Id] = dict()
        self.vertex_to_ID: Dict[Id, int] = dict()
        self.vertex_to_addr: Dict[Id, Vertex] = dict()
        
        # Type of graph
        self.is_directed: bool = is_directed
        self.is_weighted: bool = is_weighted

        # Extra space for visualization
        self.visual = list()
        self.edges = list()



    def add_vertex(self, u1: Union[Id, Vertex]) -> None:
        
        # If vertex id already exists
        if u1 in self.vertex_to_ID:
            return self.vertex_to_addr[u1]
        # If is not a vertex
        elif not(isinstance(u1, Vertex)):
            u = Vertex(u1)

        # If the verex is is not in the graph
        if u not in self.vertex_to_ID:
            # Assign an internal ID to Vertex
            u.nid = self.ID_cnt
            self.vertex_to_ID[u.id] = self.ID_cnt
            self.ID_to_vertex[self.ID_cnt] = u.id
            self.vertex_to_addr[u.id] = u
            self.ID_cnt += 1
            return u
        else:
            u.nid = self.vertex_to_ID[u.id]
            return self.vertex_to_addr[u.id]

        
        

    def add_edge(self, u1: Union[Id, Vertex], v1: Union[Id, Vertex], 
                                                    w: Numeric = 0) -> None:
        
        # Add vertices
        u: Vertex = self.add_vertex(u1)
        v: Vertex = self.add_vertex(v1)

        # Add visual edges
        self.edges.append((u.id, v.id, w))

        # Add edge to list
        if u.nid not in self.adj_list:
            self.adj_list[u.nid] = [(v.nid, w)]
        else:
            self.adj_list[u.nid].append((v.nid, w))
        
        u.add_neighbor(v, w)
        self.visual.append([u.id, v.id])

        # Add edge from other node if undirected
        if not(self.is_directed):
            if v.nid not in self.adj_list:
                self.adj_list[v.nid] = [(u.nid, w)]
            else:
                self.adj_list[u.nid].append((v.nid, w))
            v.add_neighbor(u, w)

            self.visual.append((v.id, u.id))
        else:
            if v.nid not in self.adj_list:
                self.adj_list[v.nid] = []


    def visualize(self, debug = False):

        # Directed graph
        if self.is_directed:
            G = nx.DiGraph()
        else:
            G = nx.Graph()

        # Weighted edges
        if self.is_weighted:
            G.add_weighted_edges_from(self.edges)

            if debug:
                print(G.edges(data=True))
                print(G.nodes())
                edge_weights = nx.get_edge_attributes(G, 'weight')
                print(edge_weights)

        else:
            G.add_edges_from(self.visual) 

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    
    def dijkstra_shortest_path(self, src: int = 0, 
                                debug: bool = False) -> List[Numeric]:
        # Priority queue (pq) to store vertices being preprocessed
        # (weight, vertex)
        
 
        # Initialize all distances as infinite (INF)
        dist = [float('inf')] * len(self.adj_list)
        dist[src] = 0
        pq = [(dist[src], src)]
 
        # Looping until the pq becomes empty
        while pq:
            # Extract the vertex with min weight from the pq
            current_dist, u = heapq.heappop(pq)
 
            # Iterate over all adjacent vertices of a vertex
            for v, weight in self.adj_list[u]:
                # If there is a shorter path to v through u
                if dist[v] > dist[u] + weight:
                    # Update the distance of v
                    dist[v] = dist[u] + weight
                    # Keep track of previous vertex
                    self.vertex_to_addr[self.ID_to_vertex[v]].prev_vertex = \
                                    self.vertex_to_addr[self.ID_to_vertex[u]]
                    # Update minimum element not visited
                    heapq.heappush(pq, (dist[v], v))


        # Print shortest distances
        if debug:
            print(f"Vertex Distance from Source {self.ID_to_vertex[src]}")
            for i in range(self.numV):
                print(f"{self.ID_to_vertex[i]}\t\t{dist[i]}")
            
        return dist

    def shortest_cycle_length(self, 
                              debug: bool = False) -> List[Numeric]:
        
        if not(self.is_directed):
            if debug:
                print(("Graph is undirected! "
                      f"{self.shortest_cycle_length.__name__}"
                                        "() cannot be run"))
            return -1

        dist: List[List[int]] = [[] for _ in range(self.numV)]
        min: Numeric = float('inf')
        s: int = -1
        t: int = -1

        for u in range(self.numV):
            dist[u] = self.dijkstra_shortest_path(u, debug = debug)
        
        for u in range(self.numV):
            for v in range(self.numV):
                if u != v and dist[u][v] + dist[v][u] <= min:
                    min = dist[u][v] + dist[v][u]
                    s = u
                    t = v

        if min == float('inf'):
            if debug:
                print("Graph is acyclic!")
            return -1
        else:
            if debug:
                # print(f"s: {s} of ID {self.ID_to_vertex[s]}, \
                #        t: {t} of ID {self.ID_to_vertex[t]}")
                print(f"Minimum distance: {min} from ", end="")
                it: int = t
                while it != s:
                    print(f"{self.ID_to_vertex[it]}-", end="")
                    it = self.vertex_to_addr[self.ID_to_vertex[it]].prev_vertex.nid
                print(f"{self.ID_to_vertex[it]}", end="\n")

            return s, t, min
        
        

    def __iter__(self):
        return iter(self.adj_list.values())
    
    @property
    def numV(self):
        return len(self.ID_to_vertex)
    
    @property
    def numE(self):
        cnt: int = 0

        for key in self.adj_list:
            cnt += len(self.adj_list[key])

        return cnt


if __name__ == "__main__":
    print(__name__)

    ex: int = 2

    g = Graph(is_directed=True, is_weighted=True)

    # Acyclic graph
    if ex == 1:

        g.add_edge("a", "b", 10) 
        g.add_edge("a", "c", 12) 
        g.add_edge("b", "c", 9) 
        g.add_edge("b", "d", 8) 
        g.add_edge("c", "e", 3)
        g.add_edge("c", "f", 1)
        g.add_edge("d", "e", 7)
        g.add_edge("d", "g", 8)
        g.add_edge("d", "h", 5)
        g.add_edge("e", "f", 3)
        g.add_edge("f", "h", 6)
        g.add_edge("g", "h", 9)
        g.add_edge("g", "i", 2)
        g.add_edge("h", "i", 11)

    # Directed graph
    if ex == 2:
        g.add_edge("a", "e", 4)
        g.add_edge("b", "c", 2)
        g.add_edge("b", "a", 7)
        g.add_edge("c", "d", 4)
        g.add_edge("d", "e", 1)
        g.add_edge("e", "b", 3)
        

    # # TODO: Need to add vertex that is not same CC
    # g.add_vertex("isolated vertex")

    g.visualize()
    # g.dijkstra_shortest_path()
    g.shortest_cycle_length(debug = True)