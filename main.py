from graph import CityGraph
from reader import read_instance
from simulate import simulate_outcome
from solvers import solve_randomly


if __name__ == "__main__":
    file_path = "a.txt"
    streets, cars, duration_upper_bound, bonus_amount = read_instance(file_path)
    city_graph = CityGraph(streets)
    traffic_solution = solve_randomly(city_graph, 2)
    result = simulate_outcome(
        city_graph, streets, cars, traffic_solution, duration_upper_bound, bonus_amount
    )
    print("a")
