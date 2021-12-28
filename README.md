
# OOP EX3 - Directed Weighted Graph Python
This asssinment has written by Adi Oman and Adi Miller.

## DiGraph implement GraphInterface:

The DiGraph built with 3 dictionaries:
1. dictionary that represent list of Nodes.
2. dictionary that represent list of Nodes's father.
3. dictionary that represent list of Nodes's children.

This class displays a graph and implements the following functions:
* add_edge
* add_node
* remove_node
* remove_edge
* v_size (returns the number of nodes)
* e_size (returns the number of edges)
* get_all_v (return a dictionary of all the nodes)
* all_in_edges_of_node (return a dictionary of all the nodes connected to node_id)
* all_out_edges_of_node (return a dictionary of all the nodes connected from node_id)
* get_mc 

## AlgoGraph implement GraphAlgoInterface:

This class implements the following functions:
* load_from_json - load a json file.
* save_to_json - save the graph in json file.
* shortest_path - returns the shortest path from node to other node.
* TSP - returns the shortest path that visits all the nodes in the list. 
[Explanation of Travelling salesman preblem] (https://en.wikipedia.org/wiki/Travelling_salesman_proble)
* centerPoint - returns the center node in the graph.
