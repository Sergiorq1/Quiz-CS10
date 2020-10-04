# def get_average(num_list):
#     """this functions returns the average of the numbers in the input list"""

#     sum = 0
#     for i in num_list:
#         sum += i
#     return sum / len(num_list)

# print(get_average([1,3,5,6,7]))


""" QUESTION 2 """
sports = ["basketball\n", "softball\n", "football\n", "baseball\n", "track\n"]

file = open("sports.txt", "a")
for i in range(len(sports)):
    file.write(sports[i])
    
file_a = open("sports.txt", "r")
print(file_a.read())

""" QUESTION 3 """

# hats = {
#     "snapback": 10, 
#     "beanie": 5, 
#     "baseballcap": 3,
# }
# hats["weird top hat"] = 1

# hats["snapback"] += 1

# hats.pop("weird top hat")

""" QUESTION 4 """
def add_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
numbers = [4,5,2,-3]
print(add_numbers(numbers))