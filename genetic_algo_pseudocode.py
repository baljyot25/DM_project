import random



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



# for v in graph: 
#     print(v) 

# def print_graph():


def random_gen(GENELIST, n_colors):
    print("random gen started")
    for i in range(0,100):

        GRAPH.node_colors=list()
        for i in range(len(GRAPH.nodes)):
            rand=random.randint(1,n_colors)
            GRAPH.nodes[i].color=rand
            GRAPH.node_colors.append(rand)

            
        GENELIST.append(GRAPH)            

# def init(GENELIST):
#     CURRENT_BEST = get_highest_degree(GRAPH)
#     random_gen(GENELIST, CURRENT_BEST, GRAPH)
#     #randomly fill the graph cells

def set_fitness(g):
        for node in g.nodes:
            for neighbor in node.neighbors:
                
                if g.nodes[neighbor].color == node.color:
                    g.fitness += 1
        print(g.fitness)

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


def print_graph():
    print("start graph printing")
    for i in range(N_NODES):
        print(GRAPH.nodes[i].neighbors)
def main():
    print("dnsfa")
    n = 5
    GRAPH.nodes = [] 

    for i in range(n):
        node=Node() 
        node.neighbors = [] 
        for j in range(n): 
            node.neighbors.append(random.randint(0, 1)) 
        print("ok1")
        print(node.neighbors)
        
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

    print(max_num_colors)

    
    n_colors = max_num_colors

    print_graph()
    print("start graph printing")
    for i in range(N_NODES):
        GRAPH.matrix.append(GRAPH.nodes[i].neighbors)
    print(GRAPH.matrix)
   

    while(n_colors > 0):
        CURRENT_BEST=10000
        generation = 0
        random_gen(GENELIST,n_colors)
        print(len(GENELIST))
        for i in range(len(GENELIST)):
            print(i,end=" ")
            set_fitness(GENELIST[i])
            if(GENELIST[i].fitness < CURRENT_BEST): CURRENT_BEST = GENELIST[i].fitness
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

if __name__ == "__main__":
    print("djanf")
    main()
