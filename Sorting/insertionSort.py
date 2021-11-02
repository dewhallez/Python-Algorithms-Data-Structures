# insertion sort, good for sorting small arrays or list.
#Time complexity / worst case = 0(n^2)
#Best case/Space complexity = 0(n)


def insertion_sort(array):

    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index


        while currentPosition > 0 and array[currentPosition - 1 ] > currentValue:

            print("Swapped {} for {}".format(array[currentPosition], array[currentPosition-1]))
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition -1 

            array[currentPosition] = currentValue



array = [3, 23, 31, 26, 54, 6, 9, 4, 25, 66]

insertion_sort(array)

print(f"sorted array: {array}")