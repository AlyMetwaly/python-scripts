# Graphs are used to represent many real-life 
# applications like networks, transportation paths of a city, and social network connections.
# Each node is called a Vertex and the connection between two of them is called an Edge.
# We store the matrix in a two-dimensional list, called adj.

# The __init__ method creates the adj matrix with the given size (number of vertices) and initializes all values to zeros.
# The add_edge() method is used to add an edge by setting the corresponding values to 1.
# Similarly, the remove_edge() method sets the values to 0.
class Graph(): 
    def __init__(self, size): 
        self.adj = [ [0] * size for i in range(size)]
        self.size = size 
    
    def add_edge(self, orig, dest): 
        if orig > self.size or dest > self.size or orig < 0 or dest < 0: 
            print("Invalid Edge") 
        else: 
            self.adj[orig-1][dest-1] = 1 
            self.adj[dest-1][orig-1] = 1 
        
    def remove_edge(self, orig, dest): 
        if orig > self.size or dest > self.size or orig < 0 or dest < 0: 
            print("Invalid Edge") 
        else: 
            self.adj[orig-1][dest-1] = 0 
            self.adj[dest-1][orig-1] = 0 
            
    def display(self): 
        for row in self.adj: 
            print() 
            for val in row: 
                print('{:4}'.format(val),end="") 

#a sample Graph 
G = Graph(4) 
G.add_edge(1, 3) 
G.add_edge(3, 4)
G.add_edge(2, 4)
G.display()