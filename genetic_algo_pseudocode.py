import random
import copy
import adjustText
import numpy as np
import matplotlib.pyplot as plt

def map_colors(color_indices):
    distinct_colors = [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
        '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5',
        '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5'
    ]
    
    color_map = dict(zip(range(1, 21), distinct_colors))
    return [color_map[i] for i in color_indices]

# Function to plot a graph from an adjacency matrix with node colors
def plot_graph(adjacency_matrix, color_array):
    num_nodes = len(adjacency_matrix)
    positions = np.array([[np.cos(2 * np.pi * i / num_nodes), np.sin(2 * np.pi * i / num_nodes)] for i in range(num_nodes)])

    fig, ax = plt.subplots(figsize=(20, 20))  # Adjust the figure size as needed

    # Plot edges
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if adjacency_matrix[i][j] == 1:
                ax.plot([positions[i, 0], positions[j, 0]], [positions[i, 1], positions[j, 1]], color='black')

    # Map color indices to visually distinct colors
    node_colors = map_colors(color_array)

    # Plot nodes with specified colors
    scatter = ax.scatter(positions[:, 0], positions[:, 1], color=node_colors, zorder=5)

    # Plot nodes with labels
    for i in range(num_nodes):
        # ax.text(positions[i, 0], positions[i, 1], str(i + 1), fontsize=12, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.7))
        adjustText.adjust_text([plt.text(positions[i, 0], positions[i, 1], str(i + 1), fontsize=12, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.7)) for i in range(num_nodes)])

    ax.axis('off')
    
    # Adjust label positions to avoid overlap
    

    plt.show()


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
N_NODES = 20
num_graph_generated = 100

def random_gen( n_colors):
    print("random gen started")
    l=[]
    local=list()
    for i in range(0,num_graph_generated):#need to make 100

        GRAPH.node_colors=list()
        l=list()
        
        temp_graph=copy.deepcopy(GRAPH)
        # print("num_color:",n_colors)
        # print("rand")
        for i in range(len(GRAPH.nodes)):
            
            rand=random.randint(1,n_colors)
            # print(rand,end=" ")
            temp_graph.nodes[i].color=rand
            l.append(rand)
        
        temp_graph.node_colors=l.copy()

        # print(temp_graph.node_colors)
            
        local.append((temp_graph))   
        # print(local)
    # print()
    return local 
         

# def init(GENELIST):
#     CURRENT_BEST = get_highest_degree(GRAPH)
#     random_gen(GENELIST, CURRENT_BEST, GRAPH)
#     #randomly fill the graph cells

def set_fitness(g):
        g.fitness=0
        for node in range(len(g.nodes)):
            for i in range(len(g.matrix[0])):
                if (g.matrix[node][i]==1):
                    if (g.node_colors[node]==g.node_colors[i]):
                        g.fitness+=1
            
        # print(g.fitness,end="  ")

def crossover(parent1,parent2):
    pivot = random.randint(2,N_NODES-2)
    #everything is same apart from the colors
    # print("pivot",pivot)
    
    child1_new=list()
    child2_new=list()

    # child1.nodes = child2.nodes = parent1.nodes
    for i in range(pivot):
        child1_new.append( parent1.node_colors[i])
        child2_new.append(parent2.node_colors[i])
    
    for i in range (pivot, N_NODES):
        child1_new.append(parent2.node_colors[i])
        child2_new.append(parent1.node_colors[i])
    # print("parents")
    # print(parent1.node_colors)
    # print(parent2.node_colors)
    # print("childs")
    # print(child1_new)
    # print(child2_new)
    

    return child1_new, child2_new

def crossover_top_half():
    # print("crossover started")
    #size of graph is 100
    for i in range(0,int(num_graph_generated/2),2):
        # print(int(num_graph_generated/2)+i+1)
        if (int(num_graph_generated/2)+i+1>=num_graph_generated):
            # print("edge case trigerred")
            GENELIST[int(num_graph_generated/2)+i].node_colors, not_used=crossover(GENELIST[0],GENELIST[i])
        else:
            # print(GENELIST[int(num_graph_generated/2)+i].nodes_color, GENELIST[int(num_graph_generated/2)+i+1].nodes_color)
            # GENELIST[int(num_graph_generated/2)+i].node_colors, GENELIST[int(num_graph_generated/2)+i+1].node_colors=[],[]
            # print("len",len(GENELIST))
            # print(int(num_graph_generated/2)+i)
            GENELIST[int(num_graph_generated/2)+i].node_colors, GENELIST[int(num_graph_generated/2)+i+1].node_colors = crossover(GENELIST[i],GENELIST[i+1])
            # print(GENELIST[int(num_graph_generated/2)+i].nodes_color, GENELIST[int(num_graph_generated/2)+i+1].nodes_color)

def mutation(n_colors):
    probability = 0.2
    for j in range(int(num_graph_generated/2),len(GENELIST)):
        # print("before mutatiing", j)
        # print_graph(GENELIST[j])
        for i in range(N_NODES):
            rand = random.uniform(0,1)
            if(rand <= probability):
                # print("i have mutated")
                GENELIST[j].node_colors[i] = random.randint(1,n_colors)
                (GENELIST[j].nodes)[i].color=rand
        # print("AFter mutating")
        # print_graph(GENELIST[j])



def print_graph(g):
    print("start graph printing")
    # for i in g.matrix:
    #     print(i)
    # print("colors")
    print(g.node_colors)
def main():
    # print("dnsfa")
    n = N_NODES
    GRAPH.nodes = [] 
    # ma=[[0, 1, 1,1], [1, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0]]

    for i in range(n):
        node=Node() 
        node.neighbors = [] 
        for j in range(n): 
            node.neighbors.append(random.randint(0,1)) 
        # print("ok1")
        # print(node.neighbors)
        
        GRAPH.nodes.append(node) 
    
    for i in range(n): 
        for j in range(0, i): 
            (((GRAPH.nodes)[i]).neighbors)[j] = (((GRAPH.nodes)[j]).neighbors)[i]
    for i in range(n): 
        (((GRAPH.nodes)[i]).neighbors)[i]=0
    
    # tem_graph

   

    # print_graph()
    # print("start graph printing")
    for i in range(N_NODES):
        GRAPH.matrix.append(GRAPH.nodes[i].neighbors)
    # print_graph(GRAPH)
    max_num_colors = 0
    for i in range(n): 
        if sum((GRAPH.matrix)[i]) > max_num_colors: 
            max_num_colors = sum((GRAPH.matrix)[i])+ 1

    # print(max_num_colors)
    n_colors = max_num_colors
    # print(n_colors)
   
    # random_gen(n_colors)
    at_least_1_colorable=0
    # print(GRAPH.matrix)
    while(n_colors > 0):
        CURRENT_BEST=1e9
        generation = 0
        # print("n_colors",n_colors)
        global GENELIST
        GENELIST=list()
        GENELIST=random_gen(n_colors)
        # for i in GENELIST:
            
        
        
        # print(len(GENELIST))
        # for i in range(num_graph_generated):
        #     print_graph(GENELIST[i])
        for i in range(len(GENELIST)):
            # print(i,end=" ")
            # print(GENELIST[i].node_colors)
            set_fitness(GENELIST[i])
            # print("fitness",GENELIST[i].fitness)
            if(GENELIST[i].fitness < CURRENT_BEST): CURRENT_BEST = GENELIST[i].fitness
        # print(CURRENT_BEST)
        GENELIST.sort(key = lambda x: x.fitness)
        # print("printing fitness after sort")
        # for i in range(num_graph_generated):
        #     print(GENELIST[i].fitness)
        #try until you find a n_colored solution or n_generations exceed 10k
        while(CURRENT_BEST != 0 and generation < 100):
            # print("generation",generation,"color",n_colors)
            # print("printing graph before crossovver")
            # for i in range(num_graph_generated):
            #     print_graph(GENELIST[i])
            crossover_top_half()
            # print("crossover ended")
            # print("printing graph after crossovver")

            # for i in range(num_graph_generated):
            #     print_graph(GENELIST[i])
            
            mutation(n_colors)
            # exit(0)
            for i in range(len(GENELIST)):
                # print(i,end=" ")
                set_fitness(GENELIST[i])
                if(GENELIST[i].fitness < CURRENT_BEST): CURRENT_BEST =GENELIST[i].fitness
            # print()
            # print(CURRENT_BEST)
            GENELIST.sort(key = lambda x: x.fitness)
            # print("printing fitness after sort")
            # for i in range(num_graph_generated):
            #     print(GENELIST[i].fitness)
            generation += 1
        # print()
        for i in range(len(GENELIST)):
                # print(GENELIST[i].node_colors)
                print(GENELIST[i].fitness,end=" ")
        if(CURRENT_BEST==0):
            print("at least one colorable found")
            at_least_1_colorable=1
            tem_graph=GENELIST[0]
        
        if(CURRENT_BEST != 0 and at_least_1_colorable==1): #even after 10k generations, n_colored solution couldn't be found
            print("The given graph is "+str(n_colors+1)+" colourable")

            print(tem_graph.node_colors)
            plot_graph(tem_graph.matrix,tem_graph.node_colors)
        
            break
        else: #n_colored solution was found so we try to find a solution of the graph with n-1 colours
            # at_least_1_colorable=1
            print("colors-1")
            n_colors -= 1
   
if __name__ == "__main__":
    print("djanf")
    main()
