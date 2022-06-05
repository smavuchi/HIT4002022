import sys
import random

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        graph = {}

        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges(self, node):
        # Returns the neighbors of a node
        connections = []

        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)

        return connections

    def value(self, node1, node2):
        # Returns the value of an edge between 2 nodes
        return self.graph[node1][node2]

# Dijkstra Algorithm Implementation

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}

    # Use max_value to initialize the "infinity" value of the unvisited nodes
    max_value = sys.maxsize

    for node in unvisited_nodes:
        shortest_path[node] = max_value

    # However, we initialize the starting node's value with 0

    shortest_path[start_node] = 0

    # Start the algorithm
    while unvisited_nodes:
        current_min_node = None

        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node

            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbors = graph.get_outgoing_edges(current_min_node)

        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)

            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value

                # Update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path

# Print out the results

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Add start node manually
    path.append(start_node)

    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))

    print(" -> ".join(reversed(path)))

    return path

# The algorithm in action

def dijkstra(stations, connected_stations, current_station):
    # nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens", "Mbare"]
    nodes = []

    for station in stations:
        nodes.append(station["_id"]["$oid"])

    init_graph = {}

    # for node in nodes:
    #     init_graph[node] = {}

    cost = random.randint(0, 10)

    for node in nodes:
        # Giving TypeError: unhashable type: 'dict'
        # init_graph[station["_id"]["$oid"]] = {}
        init_graph[node] = {}

    for connection in connected_stations:
        init_graph[connection["stations"][0]][connection["stations"][1]] = connection["stations"][-1]

    # init_graph["Reykjavik"]["Oslo"] = 5

    # init_graph["Reykjavik"]["Mbare"] = 1
    # init_graph["Berlin"]["Mbare"] = 1
    # init_graph["Rome"]["Reykjavik"] = 1

    # init_graph["Reykjavik"]["London"] = 4
    # init_graph["Oslo"]["Berlin"] = 1
    # init_graph["Oslo"]["Moscow"] = 3
    # init_graph["Moscow"]["Belgrade"] = 5
    # init_graph["Moscow"]["Athens"] = 4
    # init_graph["Athens"]["Belgrade"] = 1
    # # init_graph["Rome"]["Berlin"] = 2
    # init_graph["Rome"]["Berlin"] = 4
    # init_graph["Rome"]["Athens"] = 2
    # init_graph["London"]["Berlin"] = 3

    print(init_graph)

    # Create object of Graph class

    graph = Graph(nodes, init_graph)

    # Pass fully constructed graph to dijkstra_algorithm function

    # previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Reykjavik")
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=current_station)

    # Now printing the results

    # print_result(previous_nodes, shortest_path, start_node="Reykjavik", target_node="Belgrade")
    path = print_result(previous_nodes, shortest_path, start_node=current_station, target_node="62341959ab81458108afaed5")

    return path