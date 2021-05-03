class InstanceReader:
    def __init__(self, file_path: str):
        with open(file_path, "r") as input_f:
            problem_quantities = input_f.readline()
            (
                simulation_duration,
                intersection_amount,
                street_amount,
                car_amount,
                bonus_amount,
            ) = problem_quantities.split(" ")
        print(
            simulation_duration,
            intersection_amount,
            street_amount,
            car_amount,
            bonus_amount,
        )
