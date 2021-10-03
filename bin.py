from datetime import datetime

list_of_numbers = [45, 77, 89, 33, 56, 13, 87, 90, 54, 3]
number_to_search = 99999


position = -1
start_time = datetime.now()


def binary_search(input_list, n):
    """completes binary search on list
    and searches for number passed in"""

    # sorts input_list
    sorted_list = sorted(input_list)
    # print(f"Input list: {input_list}, Number to find: {n}")
    # print(f"Sorted list: {sorted_list}")

    # set the lower and upper bound
    lower_bound = 0
    upper_bound = len(input_list) - 1

    while lower_bound <= upper_bound:

        # finding the mid value
        mid = (lower_bound + upper_bound) // 2

        # compare mid value to the value to search for
        if sorted_list[mid] == n:
            globals()["position"] = mid
            return True

        # if sill not found
        # will set a new mid value
        else:
            if sorted_list[mid] < n:
                lower_bound = mid + 1
            else:
                upper_bound = mid - 1

    return False


def get_numbers(n):
    result = []
    for number in range(n):
        result.append(number)

    return result


if binary_search(get_numbers(100000), number_to_search):
    print(f"Found at index: {position+1}")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
else:
    print("Not Found")
