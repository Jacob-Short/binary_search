from datetime import datetime


list_of_numbers = [45, 77, 89, 33, 56, 13, 87, 90, 54, 3]
number_to_search = 99999


def linear_search(input_list, n):
    start_time = datetime.now()
    for i, number in enumerate(get_numbers(100000)):
        if number == n:
            print(f"Found at index: {i}")
            end_time = datetime.now()
            print('Duration: {}'.format(end_time - start_time))


def get_numbers(n):
    result = []
    for number in range(n):
        result.append(number)

    return result



linear_search(list_of_numbers, number_to_search)