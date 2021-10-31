from Hamster import Hamster


def parse_hamster_file(path_to_hamster_file: str):
    hamsters_file = open(path_to_hamster_file, 'r+')
    hamsters_data = [line for line in hamsters_file.readlines()]
    amount_of_feed = int(hamsters_data[0])
    amount_of_hamsters = int(hamsters_data[1])
    hamsters_info_array = [hamster_info.split() for hamster_info in hamsters_data[2:]]
    hamster_array = [Hamster(int(hamster_info[0]), int(hamster_info[1])) for hamster_info in hamsters_info_array]
    return amount_of_feed, amount_of_hamsters, hamster_array

def get_sum

def buy_hamsters(amount_of_feed, hamster_array):



if __name__ == '__main__':
    amount_of_feed, amount_of_hamsters, hamster_array = parse_hamster_file("hamsters_data.txt")

