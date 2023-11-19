# DM_project

# How to Run the Code:

1) To run the code using VS Code, you can click on the "run" button (if you have the Python Extension for VS Code installed)
2) To run the code via terminal (Windows), you can type "python -u <file_path>".
3) To run the code via terminal (Linux), you can type "python3 -u <file_path>".


# How does the code work?

In our application, we have considered that for every conflict in the colours of a graph of a generation, the fitness value of that graph is increased by one. For any generation of graphs, the lower the value of the fitness function for any graph, the fitter it is.

First, after getting the graph to be coloured efficiently as input, we derive the max number of colours that may be used to colour the given graph by finding out the node with the highest number of neighbouring nodes.

Each generation of the graphs has a fixed population (for example, 100) and all the graphs belonging to the same generation is stored in an array.
Then, for the first generation of graphs, we randomly generate graph colourings for all the graphs and calculate each graph’s fitness function.

If this generation has a graph with a fitness value 0, then it means that the program has successfully found a valid colouring of the graph with the given number of colours.

If in a generation, no graph has a fitness value of 0 (which means no valid colouring was found for the given graph with the given number of colours), then we create another generation of graphs from the current generation of graphs using three concepts “natural selection”, “cross-over” and “mutation”.

For creating the next generation of graphs, we first choose the best 50% of the graphs from the previous generation by sorting the graphs in ascending order based on their fitness values.

Then, from the best 50% of the graphs chosen from the previous generation, we choose two graphs each time and construct new graphs from them using the “cross-over” method.

In the "cross-over" method, we take two graphs from the best 50% of the previous generation, randomly select a node (cross-over point) among all the nodes available, and partition the two selected graphs (from previous generation) into two parts. Now, we create two new graphs by using the following method, the first child gets the colouring of the first parent graph till the cross-over point and the colouring of the second parent graph after the cross-over point, and the second child gets the colouring of the second parent till the cross-over point and the colouring of the first parent after the cross-over point.

After, graph colourings of the two selected parent graphs to create two new graphs, for both the newly created graphs, we "mutate" their node colourings.

In the "mutation" method, firstly we set a small probability (between 0 and 1) for mutation. Then, we iterate over each node of the selected graph and generate a random number between 0 and 1. If the number generated for that node of the graph is lesser than or equal to the probability of mutation we fixed earlier, then we mutate that node by assigning it a random colour from the available range of colours.

After following this process repeatedly, we manage to generate a new generation of graphs comprising of the best 50% of the graphs from the previous generation and new graphs generated using the best 50% graphs from the previous generation.

Now, we repeat the process of calculating the fitness functions of all the graphs of this new generation and check whether any graph in this generation has a fitness value of 0.

The main flow of the program is that for every “maximum number of available colours” chosen, we try to find a valid colouring of the graph. 

If the program finds a valid colouring of the graph using the specified “maximum number of available colours”, then we stop generating more generations of graphs using the specified “maximum number of available colours” and then set the “maximum number of available colours” to 1 lesser than its previous value.

We continue this process till the time for a specified “maximum number of available colours”, the program is not able to find a valid colouring of the graph within 10000 generations. Then we terminate the program with the conclusion that a valid colouring of the graph exists with the chromatic number as 1 more than the current “maximum number of available colours”.
