from collections import deque
from typing import Dict, List

from data_class import Car, Street
from graph import CityGraph
from solvers.utils import TrafficSolution


def get_open_edge_id(
    traffic_solution: TrafficSolution, current_duration: int, node_id: int
):
    cycle_duration = sum(traffic_solution[node_id].values())
    modulo_duration = current_duration % cycle_duration
    for edge_id, traffic_duration in traffic_solution[node_id].items():
        if modulo_duration >= traffic_duration:
            modulo_duration -= traffic_duration
        else:
            return edge_id


def simulate_outcome(
    city_graph: CityGraph,
    streets: List[Street],
    cars: List[Car],
    traffic_solution: TrafficSolution,
    duration_upper_bound: int,
    bonus_points: int,
) -> int:
    current_duration: int = 0
    waiting_car_per_edge: Dict[int, deque] = {}
    for car in cars:
        starting_edge_name = car.visited_street_names[0]
        starting_edge_id = streets[starting_edge_name].id
        waiting_car_per_edge.setdefault(starting_edge_id, deque()).appendleft(car.id)
    crossing_car_per_edge: Dict[int, Dict[int, int]] = {}
    for edge_id in city_graph.edges.keys():
        crossing_car_per_edge[edge_id] = {}
    travel_time_per_car: Dict[int, int] = {}
    while current_duration <= duration_upper_bound:
        for edge_id, crossing_time_per_car in crossing_car_per_edge.items():
            for crossing_car, crossing_time in crossing_time_per_car.items():
                if crossing_time + 1 == city_graph.edges[edge_id].length:
                    del crossing_time_per_car[crossing_car]
                    travel_time_per_car[crossing_car] = current_duration + 1
                else:
                    crossing_time_per_car[crossing_car] = crossing_time + 1
        for node_id, node in city_graph.nodes.items():
            open_edge_id = get_open_edge_id(traffic_solution, current_duration, node_id)
            if waiting_car_per_edge.get(edge_id, None):
                crossing_car_id = waiting_car_per_edge[edge_id].pop()
                crossing_car_per_edge[edge_id][crossing_car_id] = 0
        current_duration += 1
    return travel_time_per_car
