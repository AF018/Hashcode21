from typing import Dict, List

import attr


@attr.s(repr=True, auto_attribs=True, kw_only=True)
class Street:
    origin_id: int
    destination_id: int
    id: int
    street_name: str
    crossing_time: int


@attr.s(repr=True, auto_attribs=True, kw_only=True)
class Car:
    id: int
    time_limit: int
    visited_street_names: List[str]
