# Bubble sort with python
import time

#Starting time
start = time.time()

def bubbleSort(array):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

                swapped = True

    return array


array = [10, 3, 12, 7, 5, 1, 9]

print(bubbleSort(array))

# Sleep for 1 second to get 10 second runtime
time.sleep(1)

# end time
end = time.time()

# Total time
print(f"Runtime of the program is {end - start} ")

