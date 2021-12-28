
# OOP EX3 - Directed Weighted Graph Python
This project has written by [Adi Oman](https://github.com/adiOmann) and [Adi Miller](https://github.com/AdiMM1).

This assigment is the fourth as part of an object-oriented programming course. <br />
The assigment implements a data structure of weighted and directional gragh in Python.

![image](https://github.com/adiOmann/OOP_EX3/blob/main/Weighted-Graph.jpg)

## DiGraph implement GraphInterface:

### class Node
* Id
* position
* weight
* Tag

### class Edge
* src
* dest
* weight
* Tag
* Info

The DiGraph built with 3 dictionaries:
1. dictionary that represent list of Nodes.
2. dictionary that represent list of Nodes's fathers.
3. dictionary that represent list of Nodes's children.

This class displays a graph and implements the following functions:
* *add_edge*
* *add_node*
* *remove_node*
* *remove_edge*
* *v_size* (returns the number of nodes)
* *e_size* (returns the number of edges)
* *get_all_v* (return a dictionary of all the nodes)
* *all_in_edges_of_node* (return a dictionary of all the nodes connected to node_id)
* *all_out_edges_of_node* (return a dictionary of all the nodes connected from node_id)
* *get_mc* 

## AlgoGraph implement GraphAlgoInterface:

This class implements the following functions:
* *load json file* - load a json file.
* *save json file* - save the graph in json file.
* *shortest path* - returns the shortest path from node to other node.
[based on Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
* *TSP* - returns the shortest path that visits all the nodes in the list. 
[Explanation of Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_proble)
* center point - returns the center node in the graph.

## UML
![image](https://github.com/adiOmann/OOP_EX3/blob/main/UML/UML_screenshot.jpg)
