import timeit


class SearchClass:

    def linear_search(self, l, target):
        linearStart = timeit.default_timer()  # Timer for cpu time

        for element in l:  # Iterate through the entire list
            if element == target:  # If value at index element = list then return that the target was found
                linearEnd = timeit.default_timer()  # Timer for cpu time
                print("Time elapsed: " + str(linearEnd - linearStart))
                return "The target number (" + str(target) + ") was found."

        linearEnd = timeit.default_timer()  # Timer for cpu time
        print("Time elapsed: " + str(linearEnd - linearStart))
        return "The target number (" + str(target) + ") was not found."  # Target was not found

    def binary_search(self, l, start, end, target):
        if start > end:  # Base-case: If start/end index have passed each other, then the list does not contain target
            return "The target number (" + str(target) + ") was not found."
        else:
            mid = (start + end) // 2  # Calculate the mid point of a given sub-list
            if l[mid] == target:  # If the value at index mid is target return that it was found
                return "The target number  (" + str(target) + ") was found."
            elif l[mid] > target:  # If the value at index mid is greater than target, check the left sub-list
                return self.binary_search(l, start, mid - 1, target)
            elif l[mid] < target:  # If the value at index mid is greater than target, check the right sub-list
                return self.binary_search(l, mid + 1, end, target)

    def find_min(self, l):
        minStart = timeit.default_timer()  # Timer for cpu time
        minimum = l[0]  # Set minimum to value at index 0 to start
        for element in range(1, len(l)):  # Iterate through all values except index 0
            if l[element] < minimum:  # If item at element is less than minimum, set the new minimum
                minimum = l[element]

        minEnd = timeit.default_timer()  # Timer for cpu time
        print("Time elapsed: " + str(minEnd - minStart))
        return minimum

    def find_max(self, l):
        maxStart = timeit.default_timer()  # Timer for cpu time
        maximum = l[0]  # Set maximum to value at index 0 to start
        for element in range(1, len(l)):  # Iterate through all values except index 0
            if l[element] > maximum:  # If item at element is greater than maximum, set to new maximum
                maximum = l[element]
        maxEnd = timeit.default_timer()  # Timer for cpu time
        print("Time elapsed: " + str(maxEnd - maxStart))
        return maximum  # Return maximum

    def unique(self, l):
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

