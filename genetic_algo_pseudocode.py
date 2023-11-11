import random

class Graph:
    #collection of nodes
    #first conflict node
    # root = Node()
    nodes = []
    node_colors = []
    fitness = 0
    vertices = 0

    # def reset_visited_flag(self):

    def _init_(self, graph):
        for i in graph:
            self.nodes.add(i)
            for j in i:
                self.nodes[i].neighbours.add(j)

class Node:
    color = 0
    neighbors = []
    conflicts = 0
    visited = False

    def set_conflicts(self):
        pass

    def get_fitness(self, ideal):
        #return #graph validity failed at how many places
        #weighted fitness
        #50% -> weightage : lesser the colors used
        #50% -> weightage : validity
        pass

# def one_generation(MATRIX, GRAPH, n_colors):
#     sort_graph(MATRIX, ideal) #sort on basis of fitness ONLY and not colors
#     best_fitness_in_graph = MATRIX[0].fitness
#     if fitness(CURRENT_BEST_GRAPH) == 0:
#         return 1 #updated best graph
#     else:
#         remove_second_half(GRAPH)
#         crossover(GRAPH)
#         return 0


GENELIST = [] #solutions to solve
GRAPH = Graph() #given by user to solve
CURRENT_BEST = 0
# DIMENSIONS = [x, y]
N_NODES = len(GRAPH.nodes)

n = 40
graph = [] 
for i in range(n): 
    vertex = [] 
    for j in range(n): 
        vertex.append(random.randint(0, 1)) 
    graph.append(vertex) 
for i in range(n): 
    for j in range(0, i): 
        graph[i][j] = graph[j][i] 
for i in range(n): 
    graph[i][i] = 0
for v in graph: 
    print(v) 


def random_gen(GENELIST, n_colors, graph):
    for i in range(0,100):
        for i in graph.nodes:
            graph.node_colors[i] = random.randint(1,n_colors+1)
        GENELIST.append(graph)            

# def init(GENELIST):
#     CURRENT_BEST = get_highest_degree(GRAPH)
#     random_gen(GENELIST, CURRENT_BEST, GRAPH)
#     #randomly fill the graph cells

def set_fitness(g):
        for node in g.nodes:
            for neighbor in node.neighbors:
                if neighbor.color == node.color:
                    g.fitness += 1

def crossover(parent1,parent2):
    pivot = random.randint(2,N_NODES-2)
    child1=Graph()
    child2=Graph()
    child1.nodes = child2.nodes = parent1.nodes
    for i in range(pivot):
        child1.node_colors[i] = parent1.node_colors[i]
        child2.node_colors[i] = parent2.node_colors[i]
    
    for i in range (pivot, N_NODES):
        child1.node_colors[i] = parent2.node_colors[i]
        child2.node_colors[i] = parent1.node_colors[i]

    return child1, child2

def crossover_top_half():
    #size of graph is 100
    for i in range(0,50,2):
        GENELIST[50+i], GENELIST[50+i+1] = crossover(GENELIST[i],GENELIST[i+1])

def mutation(n_colors):
    probability = 0.2
    for j in range(50,len(GENELIST)):
        for i in range(N_NODES):
            rand = random.uniform(0,1)
            if(rand <= probability):
                GENELIST[j].node_colors[i] = random.randint(1,n_colors+1)

def main():
    n_colors = N_NODES

    while(n_colors > 0):
        generation = 0
        random_gen(GENELIST,n_colors,GRAPH)
        for i in GENELIST:
            set_fitness(i)
            if(i.fitness < CURRENT_BEST): CURRENT_BEST = i.fitness
        GENELIST.sort(key = lambda x: x.fitness)
        #try until you find a n_colored solution or n_generations exceed 10k
        while(CURRENT_BEST != 0 and generation < 10000):
            crossover_top_half(GRAPH)
            mutation(n_colors)
            for i in GENELIST:
                set_fitness(i)
                if(i.fitness < CURRENT_BEST): CURRENT_BEST = i.fitness
            GENELIST.sort(key = lambda x: x.fitness)
            generation += 1

        if(CURRENT_BEST != 0): #even after 10k generations, n_colored solution couldn't be found
            print("The given graph is "+(n_colors+1)+" colourable")
        else: #n_colored solution was found so we try to find a solution of the graph with n-1 colours
            n_colors -= 1

if __name__ == "_main_":
    main()
