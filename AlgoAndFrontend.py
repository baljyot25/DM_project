import random
import copy
import adjustText
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.graph_objects as go

class Graph:
    nodes = []
    matrix = []
    node_colors = []
    fitness = 0
    vertices = 0

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


# Global Variables
GENE_LIST = []  # solutions to solve
GRAPH = Graph()  # given by user to solve
CURRENT_BEST = 0
N_NODES = 50
N_GRAPHS_GENERATED = 100


def map_colors(color_indices):
    distinct_colors = [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
        '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5',
        '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5',
        '#393b79', '#637939', '#8c6d31', '#843c39', '#7b4173',
        '#5254a3', '#637939', '#8c6d31', '#843c39', '#7b4173',
        '#393b79', '#637939', '#8c6d31', '#843c39', '#7b4173',
        '#5254a3', '#637939', '#8c6d31', '#843c39', '#7b4173',
        '#393b79', '#637939', '#8c6d31', '#843c39', '#7b4173',
        '#5254a3', '#637939', '#8c6d31', '#843c39', '#7b4173',
        '#393b79', '#637939', '#8c6d31', '#843c39', '#7b4173',
        '#5254a3', '#637939', '#8c6d31', '#843c39', '#7b4173',
        '#393b79', '#637939', '#8c6d31', '#843c39', '#7b4173',
        '#5254a3', '#637939', '#8c6d31', '#843c39', '#7b4173',
        '#393b79', '#637939', '#8c6d31', '#843c39', '#7b4173',
        '#5254a3', '#637939', '#8c6d31', '#843c39', '#7b4173',
        '#393b79', '#637939', '#8c6d31', '#843c39', '#7b4173',
        '#5254a3', '#637939', '#8c6d31', '#843c39', '#7b4173',
        '#393b79', '#637939', '#8c6d31', '#843c39', '#7b4173'
    ]

    color_map = dict(zip(range(1, 101), distinct_colors))
    return [color_map[i] for i in color_indices]

def plot_graph(adjacency_matrix, color_array):
    num_nodes = len(adjacency_matrix)
    positions = np.array(
        [[np.cos(2 * np.pi * i / num_nodes), np.sin(2 * np.pi * i / num_nodes)] for i in range(num_nodes)]
    )

    node_colors = map_colors(color_array)

    edge_x = []
    edge_y = []
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if adjacency_matrix[i][j] == 1:
                edge_x.extend([positions[i, 0], positions[j, 0], None])
                edge_y.extend([positions[i, 1], positions[j, 1], None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    node_x = positions[:, 0]
    node_y = positions[:, 1]

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=[str(i + 1) for i in range(num_nodes)],
        textposition='bottom center',
        marker=dict(
            showscale=False,
            color=node_colors,
            size=10,
            line_width=2
        ),
        hoverinfo='text'
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                    ))

    st.plotly_chart(fig)


def random_gen(n_colors):
    print("[TASK] Starting random generation")
    local = list()
    for i in range(N_GRAPHS_GENERATED):
        GRAPH.node_colors = list()
        color_list = list()

        temp_graph = copy.deepcopy(GRAPH)
        for i in range(len(GRAPH.nodes)):
            random_color = random.randint(1, n_colors)
            temp_graph.nodes[i].color = random_color
            color_list.append(random_color)

        temp_graph.node_colors = color_list.copy()
        local.append(temp_graph)

    return local


def set_fitness(g):
    g.fitness = 0
    for node in range(len(g.nodes)):
        for i in range(len(g.matrix[0])):
            if g.matrix[node][i] == 1:
                if g.node_colors[node] == g.node_colors[i]:
                    g.fitness += 1


def crossover(parent1, parent2):
    pivot = random.randint(2, N_NODES - 2)

    child_1 = list()
    child_2 = list()

    for i in range(pivot):
        child_1.append(parent1.node_colors[i])
        child_2.append(parent2.node_colors[i])

    for i in range(pivot, N_NODES):
        child_1.append(parent2.node_colors[i])
        child_2.append(parent1.node_colors[i])

    return child_1, child_2


def crossover_top_half():
    upper = N_GRAPHS_GENERATED // 2
    for i in range(0, upper, 2):
        if upper + i + 1 >= N_GRAPHS_GENERATED:  # edge case
            GENE_LIST[upper + i].node_colors, not_used = crossover(GENE_LIST[0], GENE_LIST[i])
        else:
            GENE_LIST[upper + i].node_colors, GENE_LIST[upper + i + 1].node_colors = crossover(GENE_LIST[i],
                                                                                               GENE_LIST[i + 1])


def mutation(n_colors):
    probability = 0.2
    for j in range(N_GRAPHS_GENERATED // 2, len(GENE_LIST)):
        for i in range(N_NODES):
            random_color = random.uniform(0, 1)
            if random_color <= probability:
                GENE_LIST[j].node_colors[i] = random.randint(1, n_colors)
                GENE_LIST[j].nodes[i].color = random_color


def main():
    global N_NODES
    GRAPH.nodes = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = 0

    # Streamlit UI
    st.title("Graph Generator")

    n = st.number_input("Enter number of nodes in Graph:", min_value=4, step=1)

    generate_random_graph = st.radio("Do you want us to generate a random Graph?", ('Yes', 'No'))
    
    if generate_random_graph == 'Yes':
        if st.button("Generate Random Graph"):
            st.session_state['generated'] = 1
            N_NODES=n
            for i in range(n):
                node=Node() 
                node.neighbors = [] 
                for j in range(n): 
                    node.neighbors.append(random.randint(0,1))
                
                GRAPH.nodes.append(node) 
            st.success("Random graph generated successfully!")
            for i in GRAPH.nodes: 
                print(i.neighbors)

    elif generate_random_graph == 'No':
        print("started self")
        neighbors_input = []
        for i in range(n):
            neighbors = st.text_input(f"Enter neighbors for node {i} (0-indexed):")
            neighbors_input.append(neighbors)

        if st.button("Submit Graph"):
            st.session_state['generated'] = 1
            N_NODES=n
            for i in range(n):
                node=Node()
                node.neighbors=[0]*n
                for j in neighbors_input[i].split(): 
                    node.neighbors[int(j)]=1
                GRAPH.nodes.append(node)
            st.success("Graph submitted successfully!")
            for i in GRAPH.nodes: 
                    print(i.neighbors)

        

    if st.session_state['generated']:
        st.session_state['generated'] = 0
        for i in range(n): 
            for j in range(0, i): 
                (((GRAPH.nodes)[i]).neighbors)[j] = (((GRAPH.nodes)[j]).neighbors)[i]
        for i in range(n): 
            (((GRAPH.nodes)[i]).neighbors)[i]=0

        for i in range(N_NODES):
            GRAPH.matrix.append(GRAPH.nodes[i].neighbors)

        max_num_colors = 0
        for i in range(n): 
            if sum((GRAPH.matrix)[i]) > max_num_colors: 
                max_num_colors = sum((GRAPH.matrix)[i])+ 1

        n_colors = max_num_colors
        at_least_1_colorable=0
        while n_colors > 0:
            CURRENT_BEST = 1e9
            generation = 0
            print("n_colors", n_colors)
            global GENE_LIST
            GENE_LIST = list()

            # Generate gene_list using random generate function
            GENE_LIST = random_gen(n_colors)

            # Set fitness of each graph in the Gene List
            for i in range(len(GENE_LIST)):
                set_fitness(GENE_LIST[i])
                if GENE_LIST[i].fitness < CURRENT_BEST:
                    CURRENT_BEST = GENE_LIST[i].fitness

            # Sort the GeneList on basis of the fitness of each graph
            GENE_LIST.sort(key=lambda x: x.fitness)

            # Try until you find a n_colored solution or n_generations exceed 10k
            while CURRENT_BEST != 0 and generation < 1000:
                crossover_top_half()
                mutation(n_colors)
                for i in range(len(GENE_LIST)):
                    set_fitness(GENE_LIST[i])
                    if GENE_LIST[i].fitness < CURRENT_BEST:
                        CURRENT_BEST = GENE_LIST[i].fitness

                GENE_LIST.sort(key=lambda x: x.fitness)
                generation += 1

            if CURRENT_BEST == 0:
                print("At least one colorable found")
                at_least_1_colorable = True
                tem_graph = GENE_LIST[0]

            # Even after 10k Generations, n_colored solution couldn't be found
            if CURRENT_BEST != 0 and at_least_1_colorable:
                st.subheader("Output:")
                st.write("The given graph is " + str(n_colors + 1) + " colourable")
                print(tem_graph.node_colors)
                plot_graph(tem_graph.matrix, tem_graph.node_colors)
                break

            else:  # n_colored solution was found so we try to find a solution of the graph with n-1 colours
                # at_least_1_colorable=True
                print("colors-1")
                n_colors -= 1


if __name__ == "__main__":
    main()
