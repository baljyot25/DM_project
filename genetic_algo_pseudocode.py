import random
import copy

class Graph:
    #collection of nodes
    #first conflict node
    # root = Node()
    nodes = []
    matrix=[]
    node_colors = []
    fitness = 0
    vertices = 0

    # def reset_visited_flag(self):

    def _init_(self, graph):
        for i in graph:
            self.nodes.add(i)
            for j in i:
                self.nodes[i].neighbors.add(j)

class Node:
    color = 0
    neighbors = []
    conflicts = 0
    visited = False

    def set_conflicts(self):
        pass

    def get_fitness(self, ideal):
        
        pass

GENELIST = [] #solutions to solve
GRAPH = Graph() #given by user to solve
CURRENT_BEST = 0
# DIMENSIONS = [x, y]
N_NODES = 5
num_graph_generated=10

# for v in graph: 
#     print(v) 

# def print_graph():


def random_gen(GENELIST, n_colors):
    print("random gen started")
    l=[]
    for i in range(0,num_graph_generated):#need to make 100

        GRAPH.node_colors=list()
        l=list()

        for i in range(len(GRAPH.nodes)):
            rand=random.randint(1,n_colors)
            GRAPH.nodes[i].color=rand
            l.append(rand)
        
        GRAPH.node_colors=l.copy()

        print(GRAPH.node_colors)
            
        GENELIST.append(copy.deepcopy(GRAPH))          

# def init(GENELIST):
#     CURRENT_BEST = get_highest_degree(GRAPH)
#     random_gen(GENELIST, CURRENT_BEST, GRAPH)
#     #randomly fill the graph cells

def set_fitness(g):
        for node in g.nodes:
            for neighbor in node.neighbors:
                
                if g.nodes[neighbor].color ==g.nodes[node].color:
                    g.fitness += 1
        print(g.fitness)

def crossover(parent1,parent2):
    pivot = random.randint(2,N_NODES-2)
    #everything is same apart from the colors
    print("pivot",pivot)
    
    child1_new=[]
    child2_new=[]

    # child1.nodes = child2.nodes = parent1.nodes
    for i in range(pivot):
        child1_new.append( parent1.node_colors[i])
        child2_new.append(parent2.node_colors[i])
    
    for i in range (pivot, N_NODES):
        child1_new.append(parent2.node_colors[i])
        child2_new.append(parent1.node_colors[i])
    # print("parents")
    # print_graph(parent1)
    # print_graph(parent2)
    # print("childs")
    # print_graph(child1)
    # print_graph(child2)

    return copy.deepcopy(child1_new), copy.deepcopy(child2_new)

def crossover_top_half():
    print("crossover started")
    #size of graph is 100
    for i in range(0,int(num_graph_generated/2),2):
        print(int(num_graph_generated/2)+i+1)
        if (int(num_graph_generated/2)+i+1>=num_graph_generated):
            # print("edge case trigerred")
            GENELIST[int(num_graph_generated/2)+i].nodes_color, not_used=crossover(GENELIST[0],GENELIST[i])
        else:
            GENELIST[int(num_graph_generated/2)+i].nodes_color, GENELIST[int(num_graph_generated/2)+i+1].nodes_color = crossover(GENELIST[i],GENELIST[i+1])

def mutation(n_colors):
    probability = 0.2
    for j in range(int(num_graph_generated/2),len(GENELIST)):
        print("before mutatiing", j)
        print_graph(GENELIST[j])
        for i in range(N_NODES):
            rand = random.uniform(0,1)
            if(rand <= probability):
                print("i have mutated")
                GENELIST[j].node_colors[i] = random.randint(1,n_colors+1)
                (GENELIST[j].nodes)[i].color=rand
        print("AFter mutating")
        print_graph(GENELIST[j])



def print_graph(g):
    print("start graph printing")
    # for i in g.matrix:
    #     print(i)
    # print("colors")
    print(g.node_colors)
def main():
    print("dnsfa")
    n = 5
    GRAPH.nodes = [] 

    for i in range(n):
        node=Node() 
        node.neighbors = [] 
        for j in range(n): 
            node.neighbors.append(random.randint(0, 1)) 
        # print("ok1")
        # print(node.neighbors)
        
        GRAPH.nodes.append(node) 
    
    for i in range(n): 
        for j in range(0, i): 
            (((GRAPH.nodes)[i]).neighbors)[j] = (((GRAPH.nodes)[j]).neighbors)[i]
    for i in range(n): 
        (((GRAPH.nodes)[i]).neighbors)[i]=0
    

    max_num_colors = 1
    for i in range(n): 
        if sum((GRAPH.nodes)[i].neighbors) > max_num_colors: 
            max_num_colors = sum((GRAPH.nodes)[i].neighbors)+ 1

    # print(max_num_colors)
    n_colors = max_num_colors

    # print_graph()
    # print("start graph printing")
    for i in range(N_NODES):
        GRAPH.matrix.append(GRAPH.nodes[i].neighbors)
    # print_graph(GRAPH)
   
   

    while(n_colors > 0):
        CURRENT_BEST=10000
        generation = 0
        random_gen(GENELIST,n_colors)
        print(len(GENELIST))
        for i in range(num_graph_generated):
            print_graph(GENELIST[i])
        for i in range(len(GENELIST)):
            print(i,end=" ")
            set_fitness(GENELIST[i])
            if(GENELIST[i].fitness < CURRENT_BEST): CURRENT_BEST = GENELIST[i].fitness
        print(CURRENT_BEST)
        GENELIST.sort(key = lambda x: x.fitness)
        print("printing fitness after sort")
        for i in range(num_graph_generated):
            print(GENELIST[i].fitness)
        #try until you find a n_colored solution or n_generations exceed 10k
        while(CURRENT_BEST != 0 and generation < 10):
            print("printing graph before crossovver")
            for i in range(num_graph_generated):
                print_graph(GENELIST[i])
            crossover_top_half()
            print("crossover ended")
            print("printing graph after crossovver")
            for i in range(num_graph_generated):
                print_graph(GENELIST[i])
            
            # mutation(n_colors)
            # exit(0)
            for i in range(len(GENELIST)):
                print(i,end=" ")
                set_fitness(GENELIST[i])
                if(GENELIST[i].fitness < CURRENT_BEST): CURRENT_BEST =GENELIST[i].fitness
            print(CURRENT_BEST)
            GENELIST.sort(key = lambda x: x.fitness)
            print("printing fitness after sort")
            for i in range(num_graph_generated):
                print(GENELIST[i].fitness)
            generation += 1
        exit(0)
        if(CURRENT_BEST != 0): #even after 10k generations, n_colored solution couldn't be found
            print("The given graph is "+str(n_colors+1)+" colourable")
        else: #n_colored solution was found so we try to find a solution of the graph with n-1 colours
            n_colors -= 1

if __name__ == "__main__":
    print("djanf")
    main()
