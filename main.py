def get_average(num_list):
    """this functions returns the average of the numbers in the input list"""

    sum = 0
    for i in num_list:
        sum += i
    return sum / len(num_list)

print(get_average([1,3,5,6,7]))