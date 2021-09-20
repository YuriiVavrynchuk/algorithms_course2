import argparse
import time

parser = argparse.ArgumentParser(description='Enter information for heap sorting')
parser.add_argument('--order', type=str, help="Order of the sorting")
parser.add_argument('--sorting_array', type=int, nargs='+', help='An integers for the sorting')
args = parser.parse_args()

comparisons = 0
swaps = 0


def heapify(input_array, heapifying_limit, starting_root, order):
    global comparisons
    root = starting_root
    left_child = 2 * starting_root + 1
    right_child = 2 * starting_root + 2

    if order == 'asc':
        if left_child < heapifying_limit and input_array[root] < input_array[left_child]:
            root = left_child

        if right_child < heapifying_limit and input_array[root] < input_array[right_child]:
            root = right_child
    elif order == 'desc':
        if left_child < heapifying_limit and input_array[root] > input_array[left_child]:
            root = left_child

        if right_child < heapifying_limit and input_array[root] > input_array[right_child]:
            root = right_child
    else:
        raise Exception("Only \"asc\" or \"dsc\" values for sorting order.")
    comparisons += 2

    if root != starting_root:
        swap(input_array, starting_root, root)
        heapify(input_array, heapifying_limit, root, order)


def heap_sort(input_array, order):
    for i in range(len(input_array) // 2 - 1, -1, -1):
        heapify(input_array, len(input_array), i, order)

    for i in range(len(input_array) - 1, 0, -1):
        swap(input_array, 0, i)
        heapify(input_array, i, 0, order)


def swap(input_array, index1, index2):
    global swaps
    input_array[index1], input_array[index2] = input_array[index2], input_array[index1]
    swaps += 1
    return input_array


def main():
    global swaps
    global comparisons
    print("Heap sort:")

    starting_time = time.perf_counter()
    heap_sort(args.sorting_array, args.order)
    ending_time = time.perf_counter()
    duration = (ending_time - starting_time) * 1000

    print(f"Execution time: {duration}")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    print("Sorted array: ")
    print(args.sorting_array, "\n")

    swaps, comparisons = 0, 0

    return args.sorting_array


if __name__ == "__main__":
    main()
