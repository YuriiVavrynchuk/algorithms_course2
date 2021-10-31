from Hamster import Hamster


def parse_hamster_file(path_to_hamster_file: str):
    hamsters_file = open(path_to_hamster_file, 'r+')
    hamsters_data = [line for line in hamsters_file.readlines()]
    amount_of_feed = int(hamsters_data[0])
    amount_of_hamsters = int(hamsters_data[1])
    hamsters_info_array = [hamster_info.split() for hamster_info in hamsters_data[2:]]
    hamster_array = [Hamster(int(hamster_info[0]), int(hamster_info[1])) for hamster_info in hamsters_info_array]
    return amount_of_feed, amount_of_hamsters, hamster_array


def get_feed_reducing(hamsters_array, hamster_index_to_remove):
    feed_reducing = 0
    for i in range(len(hamsters_array)):
        if i != hamster_index_to_remove:
            feed_reducing += hamsters_array[i].avidity
        else:
            feed_reducing += hamsters_array[i].consumption + hamsters_array[i].avidity * (len(hamsters_array) - 1)
    return feed_reducing


def get_sum(hamsters_array):
    return sum([hamster.consumption + hamster.avidity * (len(hamsters_array) - 1) for hamster in hamsters_array])


def buy_hamsters(amount_of_feed, hamsters_array):
    if get_sum(hamsters_array) <= amount_of_feed:
        return len(hamsters_array)
    else:
        feed_reducing_array = [get_feed_reducing(hamsters_array, i) for i in range(len(hamsters_array))]
        index_max = max(range(len(feed_reducing_array)), key=feed_reducing_array.__getitem__)
        del hamsters_array[index_max]
        return buy_hamsters(amount_of_feed, hamsters_array)


def main(hamster_data_file_path: str):
    amount_of_feed, amount_of_hamsters, hamster_array = parse_hamster_file(hamster_data_file_path)
    number_of_bought_hamsters = buy_hamsters(amount_of_feed, hamster_array)
    with open("hamsters_out.txt", "w") as hamsters_out_file:
        hamsters_out_file.write(str(number_of_bought_hamsters))
    hamsters_out_file.close()


if __name__ == '__main__':
    main("hamsters_data.txt")
