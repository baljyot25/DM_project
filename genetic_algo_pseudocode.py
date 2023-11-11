import random

GENELIST = [] #solutions to solve
GRAPH = Graph() #given by user to solve
CURRENT_BEST = 0
DIMENSIONS = [x, y]
N_NODES=0
class Graph:
    #collection of nodes
    #first conflict node
    # root = Node()
    nodes = []
    node_colors = []
    fitness = 0
    vertices = 0

    # def reset_visited_flag(self):


    def _init_(self, graph, vertices):
        self.vertices = vertices
        self.graph = graph

    def set_fitness(self, GRAPH):
        #har graph ke nodes
        #nodes ke neighbour
        #neighbor ke colors compare
        #fitness += 1 if color is same
        #lower fitness implies better solution
        
        for node in self.nodes:
            for neighbor in node.neighbors:
                if neighbor.color == node.color:
                    self.fitness += 1
            

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


def random_gen(GENELIST, n_colors, graph):
    for i in range(0,100):
        for i in graph.nodes:
            graph.node_colors[i] = random.randint(1,n_colors+1)
        GENELIST.append(graph)            

# def init(GENELIST):
#     CURRENT_BEST = get_highest_degree(GRAPH)
#     random_gen(GENELIST, CURRENT_BEST, GRAPH)
#     #randomly fill the graph cells


def crossover(parent1,parent2):
    pivot = random.randint(2,len(GRAPH.nodes)-2)
    child1=Graph()
    child2=Graph()
    child1.nodes = child2.nodes = parent1.nodes
    for i in range(pivot):
        child1.node_colors[i] = parent1.node_colors[i]
        child2.node_colors[i] = parent2.node_colors[i]
    
    for i in range (pivot, len(GRAPH.nodes)):
        child1.node_colors[i] = parent2.node_colors[i]
        child2.node_colors[i] = parent1.node_colors[i]

    return child1, child2

def crossover_top_half():
    #size of graph is 100
    for i in range(0,50,2):
        GENELIST[50+i], GENELIST[50+i+1] = crossover(GENELIST[i],GENELIST[i+1])

def mutation(n_colors):
    for j in range(len(GENELIST)):
        probability = 0.2
        for i in range(len(GRAPH.nodes)):
            rand = random.uniform(0,1)
            if(rand <= probability):
                GENELIST[j].node_colors = random.randint(1,n_colors+1)

def main():
    n_colors = len(GRAPH.nodes)

    while(n_colors > 0):
        generation = 0
        random_gen(GENELIST,n_colors,GRAPH)
        GENELIST.sort(key = lambda x: x.fitness)
        #try until you find a n_colored solution or n_generations exceed 10k
        while(CURRENT_BEST != 0 and generation < 10000):
            GENELIST.sort(key = lambda x: x.fitness)
            if (GENELIST[0].fitness!=0):
                crossover_top_half(GRAPH)
                mutation(n_colors)
            else:
                CURRENT_BEST=0
                break
            
            generation += 1

        if(CURRENT_BEST != 0): #even after 10k generations, n_colored solution couldn't be found
            print("The given graph is "+(n_colors+1)+" colourable")
        else: #n_colored solution was found so we try to find a solution of the graph with n-1 colours
            n_colors -= 1

if __name__ == "_main_":
    main()
