import time

list_of_numbers = [45, 77, 89, 33, 56, 13, 87, 90, 888, 66, 44, 332, 345, 677, 5443 ,322, 5,56,57,58,59,89,78,789,7865,345,67,890,876,54,3]
number_to_search = 87


position = -1
start_time = time.time()



def binary_search(input_list, n):
    '''performs binary search'''

    


    # sorts input_list
    sorted_list = sorted(input_list)
    print(f'Input list: {input_list}, Number to find: {n}')
    print(f'Sorted list: {sorted_list}')

    # set the lower and upper bound
    lower_bound = 0
    upper_bound = len(input_list) - 1


    while lower_bound <= upper_bound:

        #finding the mid value
        mid = (lower_bound + upper_bound) // 2

        # compare mid value to the value to search for
        if sorted_list[mid] == n:
            globals()['position'] = mid
            return True

        # if sill not found
            # will set a new mid value
        else:
            if sorted_list[mid] < n:
                lower_bound = mid+1
            else:
                upper_bound = mid-1

    return False



if binary_search(list_of_numbers, number_to_search):
    print(f'Found at index: {position+1}')
    print(f'Time: {time.time() - start_time}')
else:
    print('Not Found')
