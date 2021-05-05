import random as rd

from graph import CityGraph
from .utils import TrafficSolution


def solve_randomly(
    city_graph: CityGraph, max_green_light_duration: int
) -> TrafficSolution:
    traffic_solution: TrafficSolution = {}
    for node_id, node in city_graph.nodes.items():
        for edge in node.inward_edges:
            traffic_solution.setdefault(node.id, {})[edge.id] = rd.randint(
                1, max_green_light_duration
            )
    return traffic_solution
