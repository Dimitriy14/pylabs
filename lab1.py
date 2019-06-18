from random import seed
from random import randint

seed(1)

rand_nums = [randint(0, 99) for i in range(50)]
print("Generated list: ", list)

new_list = []

try:
    min_num = int(input("Enter minimum number: "))
    max_num = int(input("Enter maximum number: "))
    for i, val in enumerate(rand_nums):
        if min_num <= val <= max_num:
            print("list[" + str(i) + "] => " + str(val))
            new_list.append(i)

except:
    print("Incorrect input")

print("Result list: ", new_list)
