import timeit
import random

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


def linear_search(l, target):
    linearStart = timeit.default_timer()  # Timer for cpu time

    for element in l: # Iterate through the entire list
        if element == target:  # If value at index element = list then return that the target was found
            linearEnd = timeit.default_timer()  # Timer for cpu time
            print("Time elapsed: " + str(linearEnd - linearStart))
            return "The target number (" + str(target) + ") was found."

    linearEnd = timeit.default_timer()  # Timer for cpu time
    print("Time elapsed: " + str(linearEnd - linearStart))
    return "The target number (" + str(target) + ") was not found."  # Target was not found


def binary_search(l, start, end, target):
    if start > end:  # Base-case: If start and end index have passed each other, then the list does not contain target
        return "The target number (" + str(target) + ") was not found."
    else:
        mid = (start + end) // 2  # Calculate the mid point of a given sub-list
        if l[mid] == target:  # If the value at index mid is target return that it was found
            return "The target number  (" + str(target) + ") was found."
        elif l[mid] > target:  # If the value at index mid is greater than target, check the left sub-list
            return binary_search(l, start, mid - 1, target)
        elif l[mid] < target:  # If the value at index mid is greater than target, check the right sub-list
            return binary_search(l, mid + 1, end, target)


print("#### Linear Search ####")
print(linear_search(list1, t))
print()

print("#### Binary Search ####")
list2 = list1.copy()
list2.sort()
binaryStart = timeit.default_timer() # Timer for cpu time
print(binary_search(list2, 0, len(list1) - 1, t))
print("Time elapsed: " + str(timeit.default_timer() - binaryStart)) # Timer for cpu time
print()


###############################################################
# 4. Find min/max values of unsorted list
###############################################################


def find_min(l):
    minStart = timeit.default_timer()  # Timer for cpu time
    minimum = l[0]  # Set minimum to value at index 0 to start
    for element in range(1, len(l)): # Iterate through all values except index 0
        if l[element] < minimum:  # If item at element is less than minimum, set the new minimum
            minimum = l[element]

    minEnd = timeit.default_timer()  # Timer for cpu time
    print("Time elapsed: " + str(minEnd - minStart))
    return minimum


def find_max(l):
    maxStart = timeit.default_timer()  # Timer for cpu time
    maximum = l[0]  # Set maximum to value at index 0 to start
    for element in range(1, len(l)): # Iterate through all values except index 0
        if l[element] > maximum:  # If item at element is greater than maximum, set to new maximum
            maximum = l[element]
    maxEnd = timeit.default_timer()  # Timer for cpu time
    print("Time elapsed: " + str(maxEnd - maxStart))
    return maximum  # Return maximum


print("#### Minimum Search ####")
print("The minimum value in the list is: " + str(find_min(list1)))
print()

print("#### Maximum Search ####")
print("The maximum value in the list is: " + str(find_max(list1)))
print()


###############################################################
# 5. Unsorted list has distinct numbers
###############################################################


def unique(l):
    uniqueStart = timeit.default_timer()  # Timer for cpu time
    temp1 = []  # Temp list for holding unique value
    temp2 = []  # Temp list for holding duplicate values

    for element in range(len(l)):  # Iterate through the entire list
        if l[element] not in temp1:  # If an element is not in temp1, add it to it
            temp1.append(l[element])
        else:
            temp2.append(l[element])  # Add duplicate values to temp2

    if not temp2:  # If temp2 is empty
        return True  # Return true
    else:  # If temp2 is not empty print
        print("The non-unique numbers are: " + str(temp2))  # Print out duplicate values
        uniqueEnd = timeit.default_timer()  # Timer for cpu time
        print("Time elapsed: " + str(uniqueEnd - uniqueStart))
        return False  # Return false


print("#### Distinct Numbers Search ####")
uniqueStart = timeit.default_timer()
print(unique(list1))
print()


###############################################################
# 7. Perform sorting algorithms
###############################################################

###############################################################
# Selection sort finds the smallest value in a list and moves it to the front. The next iteration will assume the first
# item is sorted and try to find the smallest value in the sub-list and move that to the next available index. Swaps
# continue until the list is sorted.
###############################################################
def selection_sort(l):
    for e1 in range(len(l)):  # Iterate through the entire list

        smallest = e1
        for e2 in range(e1 + 1, len(l)): # Iterate through the entire list that is not sorted
            # If value at e2 is smaller than the current smallest value, then change the new index for smallest
            if l[e2] < l[smallest]:
                smallest = e2

        l[e1], l[smallest] = l[smallest], l[e1]  # Swap the values at e1 and smallest

    return l  # Return the sorted list


print("#### Selection Sort ####")
list3 = list1.copy()
print(selection_sort(list3))
print()


###############################################################
# Insertion sort assumes the first index of the list is sorted, therefore the range from index 1 to len(l) must be
# iterated through for sorting. The variable value is equal to the value at index element because it represents the next
# item
###############################################################
def insertion_sort(l):
    for element in range(1, len(l)):

        value = l[element]

        while l[element - 1] > value and element > 0:
            l[element], l[element - 1] = l[element - 1], l[element]
            element = element - 1

    return l


print("#### Insertion Sort ####")
list4 = list1.copy()
print(insertion_sort(list4))
print()


###############################################################
# Every index except the last
###############################################################
def bubble_sort(l):
    # Iterates through len(l) - 1 last item will be sorted after first iteration
    for e1 in range(len(l) - 1):

        # Iterates through len(l) - 1 - e1 because items should be sorted at the right end of the list after iterations
        for e2 in range(len(l) - 1 - e1):

            # Swap elements at e2 and e1 if element at e2 is greater than e1
            if l[e2] > l[e2 + 1]:
                l[e2], l[e2 + 1] = l[e2 + 1], l[e2]

    return l  # Return the sorted list


print("#### Bubble Sort ####")
list5 = list1.copy()
print(bubble_sort(list5))
print()


###############################################################
# I spent too much time working on this recursive solution getting a "maximum recursion depth  exceeded in comparison"
# error. The lists we're dealing with here were too big, but it turned out to work with smaller lists so I chose to keep
# the function in here.
###############################################################
def rec_bubble_sort(l, length):
    if length == 1:
        return l  # Return l if there is only one element
    for element in range(length - 1): # Iterate to all elements except final so no out of bounds error
        # Swap items at index element and index element + 1 if index element is greater
        if l[element] > l[element + 1]:
            l[element], l[element + 1] = l[element + 1], l[element]

    return rec_bubble_sort(l, length - 1) + [l[-1]]  # Return recursive bubble sort of new sub-list + the sorted element


print("#### Recursive Bubble Sort ####")
list6 = [3, 2, 1, 6, 7, 8, 3, 6, 4]
print(rec_bubble_sort(list6, len(list6)))
print()


###############################################################
# Merge sort is broken down into two functions, merge() and merge_sort(). The merge_sort() function is what is called
# and recursively separates the list into sub-lists. Once the base case is met the first call to merge() is done, which
# returns a single item sub-list. This sub-list is merged with another single item sub-list and then they are both
# passed to merge(), which will sort their values into a new sub-list and return that. This goes on until the whole list
# is sorted.
###############################################################
def merge(l, r):
    temp = []  # Temporary list to hold the sorted sub-list
    left = right = 0  # Initialize both left and right pointers to 0

    # As long as the left and right pointers are not out of bounds, keep comparing values
    while left < len(l) and right < len(r):
        if l[left] < r[right]:  # If value at at index left of l is less than index right of r, add it to temp list
            temp.append(l[left])
            left += 1  # Increment the pointer to look at the next value in the sub-list l
        else:  # If value at index right of r is less than index left of l, add it to temp list
            temp.append(r[right])
            right += 1  # Increment the pointer to look at the next value in the sub-list r

    temp.extend(l[left:])  # Add the remaining values from sub-list left if right was exhausted
    temp.extend(r[right:])  # Add the remaining values from sub-list right if left was exhausted
    return temp  # Return the sorted sub-list


def merge_sort(l):

    if len(l) == 1:  # Base case: if a sub-list is of size 1 return it
        return l

    mid = len(l) // 2  # Get the mid point of l so that it can be split into two sub-lists
    # Calls merge() and on two recursive merg_sort() calls that are passed the two sub-lists
    return merge(merge_sort(l[:mid]), merge_sort(l[mid:]))


print("#### Merge Sort ####")
list7 = list1.copy()
print(merge_sort(list7))
print()
