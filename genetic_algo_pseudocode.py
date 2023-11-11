
GENELIST = [] #solutions to solve
GRAPH = Graph() #given by user to solve
CURRENT_BEST = 0
DIMENSIONS = [x, y]
N_NODES=0
class Graph:
    #collection of nodes
    #first conflict node
    root = Node()
    nodes=set()
    fitness = 0
    vertices=0

    def reset_visited_flag(self):


    def _init_(self, graph, vertices):
        self.vertices = vertices
        self.graph = graph

    def set_fitness(self, GRAPH):
        #har graph ke nodes
        #nodes ke neighbour
        #neighbor ke colors compare
        #fitness += 1 if color is same
        #lower fitness implies better solution
        
        for node in self:
            for neighbor in node.neighbors:
                if neighbor.color == node.color:
                    self.fitness += 1
            

class Node:
    color = 0
    neighbors = set()
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

    def one_generation(MATRIX, GRAPH, n_colors):
        #[[]]


        sort_graph(MATRIX, ideal) #sort on basis of fitness ONLY and not colors
        best_fitness_in_graph = MATRIX[0].fitness
        if fitness(CURRENT_BEST_GRAPH) == 0:
            return 1 #updated best graph
        else:
            remove_second_half(GRAPH)
            crossover(GRAPH)
            return 0


    def random_gen(GENELIST, n_colors, graph):
        for i in range(0,100):
            for i in graph:
                graph[i].color = random.randint(1,n_colors)
            GENELIST.append(graph)            

    def init(GENELIST):
        CURRENT_BEST = get_highest_degree(GRAPH)
        random_gen(GENELIST, CURRENT_BEST, GRAPH)
        #randomly fill the graph cells


def crossover(parent1,parent2):
    pivot =random.randint(2,N_NODES-2)
    child1=Graph()
    child2=Graph()
    for i in range(pivot):
        child1.nodes.add((parent1.nodes)[i])

def crossover_top_half():
    #size of graph is 100
    for i in range(0,50,2):
        parent1,parent2=GENELIST[i],GENELIST[i+1]

        crossover(parent1,parent2)

    


def main():
    temp = 10000
    n_colors = graph.vertices

    while(True and n_colors > 0):
        generation = 0
        random_gen(GENELIST,n_colors,graph)
        GENELIST.sort(key = lambda x: x.fitness)
        #try until you find a n_colored solution or n_generations exceed 10k
        while(CURRENT_BEST != 0 and generation < 10000):
            GENELIST.sort(key = lambda x: x.fitness)
            if (GENELIST[0].fitness!=0):
                #eliminate_bottom_half()
                crossover_top_half(GRAPH)


            else:
                CURRENT_BEST=0
                break
            
            generation += 1
            pass

        if(CURRENT_BEST != 0): #even after 10k generations, n_colored solution couldn't be found
            print("The given graph is "+(n_colors+1)+" colourable")
        else: #n_colored solution was found so we try to find a solution of the graph with n-1 colours
            n_colors -= 1

if _name_ == "_main_":
    main()
