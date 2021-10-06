import timeit
import random
from SortingClass import SortingClass
from SearchClass import SearchClass

###############################################################
# 1. Generate list of random numbers
###############################################################


list1 = []


def fill_list(list1, size):
    for i in range(0, size):
        list1.append(random.randint(0, size * 3))


fill_list(list1, 10000)

###############################################################
# 2. Generate random target number
###############################################################


t = random.randint(0, len(list1) * 2)


###############################################################
# 3. Perform linear and binary search
###############################################################

se = SearchClass()

print("#### Linear Search ####")
print(se.linear_search(list1, t))
print()

print("#### Binary Search ####")
list2 = list1.copy()
list2.sort()
binaryStart = timeit.default_timer() # Timer for cpu time
print(se.binary_search(list2, 0, len(list1) - 1, t))
print("Time elapsed: " + str(timeit.default_timer() - binaryStart))  # Timer for cpu time
print()

###############################################################
# 4. Find min/max values of unsorted list
###############################################################

print("#### Minimum Search ####")
print("The minimum value in the list is: " + str(se.find_min(list1)))
print()

print("#### Maximum Search ####")
print("The maximum value in the list is: " + str(se.find_max(list1)))
print()


###############################################################
# 5. Unsorted list has distinct numbers
###############################################################


print("#### Distinct Numbers Search ####")
print(se.unique(list1))
print()

###############################################################
# 7. Perform sorting algorithms
###############################################################

so = SortingClass()

print("#### Selection Sort ####")
list3 = list1.copy()
selStart = timeit.default_timer()
print(SortingClass.selection_sort(list3))
print("Time elapsed: " + str(timeit.default_timer() - selStart))  # Timer for cpu time
print()


print("#### Insertion Sort ####")
list4 = list1.copy()
insStart = timeit.default_timer()
print(SortingClass.insertion_sort(list4))
print("Time elapsed: " + str(timeit.default_timer() - insStart))  # Timer for cpu time
print()


print("#### Bubble Sort ####")
list5 = list1.copy()
bubStart = timeit.default_timer()
print(SortingClass.bubble_sort(list5))
print("Time elapsed: " + str(timeit.default_timer() - bubStart))  # Timer for cpu time
print()


print("#### Recursive Bubble Sort ####")
list6 = [3, 2, 1, 6, 7, 8, 3, 6, 4]
print(SortingClass.rec_bubble_sort(so, list6, len(list6)))
print()


print("#### Merge Sort ####")
list7 = list1.copy()
mergStart = timeit.default_timer()
print(SortingClass.merge_sort(so, list7))
print("Time elapsed: " + str(timeit.default_timer() - mergStart))  # Timer for cpu time
print()
