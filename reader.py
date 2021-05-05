from data_class import Car, Street

def read_instance(file_path: str):
    with open(file_path, "r") as input_f:
        str_params = input_f.readline()
        (
            simulation_duration,
            intersection_amount,
            street_amount,
            car_amount,
            bonus_amount,
        ) = (int(str_param) for str_param in str_params.split(" "))
        streets: Dict[int, Street] = {}
        for street_id in range(street_amount):
            street_line = input_f.readline().strip()
            (
                origin_id,
                destination_id,
                street_name,
                crossing_time,
            ) = street_line.split(" ")
            streets[street_name] = Street(
                origin_id=int(origin_id), 
                destination_id=int(destination_id), 
                street_id=street_id,
                street_name=street_name, 
                crossing_time=int(crossing_time)
            )
        cars: List[Car] = []
        for car_id in range(car_amount):
            car_line = input_f.readline().strip()
            time_limit, *visited_street_names = car_line.split(" ")
            cars.append(
                Car(
                    time_limit=int(time_limit), 
                    visited_street_names=visited_street_names, 
                )
            )
    return streets, cars