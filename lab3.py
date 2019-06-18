from random import seed
from random import randint


def get_indexes(list, min_num = 1, max_num = 99):
    new_list = []
    for i, val in enumerate(list):
        if min_num <= val <= max_num:
            print("list[" + str(i) + "] => " + str(val))
            new_list.append(i)
    return new_list


try:
    seed(1)
    list = [randint(0, 99) for i in range(50)]
    print("Generated list: ", list)
    min_num = int(input("Enter minimum number: "))
    max_num = int(input("Enter maximum number: "))
    print("Result list: ", get_indexes(list, min_num, max_num))

except:
    print("Incorrect input")

