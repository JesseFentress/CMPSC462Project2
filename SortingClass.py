class SearchClass:

    def __init__(self):

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
        for e2 in range(e1 + 1, len(l)):  # Iterate through the entire list that is not sorted
            # If value at e2 is smaller than the current smallest value, then change the new index for smallest
            if l[e2] < l[smallest]:
                smallest = e2

        l[e1], l[smallest] = l[smallest], l[e1]  # Swap the values at e1 and smallest

    return l  # Return the sorted list


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

###############################################################
# I spent too much time working on this recursive solution getting a "maximum recursion depth  exceeded in comparison"
# error. The lists we're dealing with here were too big, but it turned out to work with smaller lists so I chose to keep
# the function in here.
###############################################################
def rec_bubble_sort(l, length):
    if length == 1:
        return l  # Return l if there is only one element
    for element in range(length - 1):  # Iterate to all elements except final so no out of bounds error
        # Swap items at index element and index element + 1 if index element is greater
        if l[element] > l[element + 1]:
            l[element], l[element + 1] = l[element + 1], l[element]

    return rec_bubble_sort(l, length - 1) + [
        l[-1]]  # Return recursive bubble sort of new sub-list + the sorted element

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
        if l[left] < r[
            right]:  # If value at at index left of l is less than index right of r, add it to temp list
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