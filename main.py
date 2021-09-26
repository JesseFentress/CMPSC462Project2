import time
import random

list1 = []


def fill_list(list1, size):

    for i in range(0, size):
        list1.append(random.randint(0, size * 3))


fill_list(list1, 10000)

print(list1)




