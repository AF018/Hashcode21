from typing import List

import attr

from data_class import Street


@attr.s(repr=True, eq=False, auto_attribs=True, kw_only=True)
class Edge():
    id: int
    origin_node_id: int
    destination_node_id: int
    length: int


@attr.s(repr=True, eq=False, auto_attribs=True, kw_only=True)
class Node():
    id: int
    outward_edges: List[Edge]
    inward_edges: List[Edge]


class CityGraph():
    def __init__(self, streets: List[Street]):
        self.edges: Dict[int, Edge] = {}
        inward_edges_per_node_id: Dict[int, List[Edge]] = {}
        outward_edges_per_node_id: Dict[int, List[Edge]] = {}
        for street in streets.values():
            edge = Edge(
                id=street.street_id, 
                origin_node_id=street.origin_id, 
                destination_node_id=street.destination_id, 
                length=street.crossing_time
            )
            outward_edges_per_node_id.setdefault(street.origin_id, []).append(edge)
            inward_edges_per_node_id.setdefault(street.destination_id, []).append(edge)
            self.edges[street.street_id] = edge
        self.nodes: Dict[int, Node] = {}
        for node_id, inward_edges in inward_edges_per_node_id.items():
            outward_edges = outward_edges_per_node_id.get(node_id, [])
            node = Node(id=node_id, inward_edges=inward_edges, outward_edges=outward_edges)
            self.nodes[node_id] = node
        self.nodes_amount = len(self.nodes)
        self.edges_amount = len(self.edges)
