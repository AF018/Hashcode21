from graph import CityGraph
from reader import read_instance 
from solvers import solve_randomly


if __name__ == "__main__":
    file_path = "a.txt"
    streets, cars = read_instance(file_path)
    city_graph = CityGraph(streets)
    random_solution = solve_randomly(city_graph, 2)
    print('a')
