from reader import read_instance 

if __name__ == "__main__":
    file_path = "a.txt"
    streets, cars = read_instance(file_path)
    print(streets, cars)