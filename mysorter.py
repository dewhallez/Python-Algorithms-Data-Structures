# Selection sort in python with recursive function

# Selection sort function 
def findSmallest(array):
    smallest = array[0]
    smallest_index = 0

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i 

    return smallest_index


def selectSort(array):
    newArray = []

    for i in range(len(array)):
        smallest = findSmallest(array)
        newArray.append(array.pop(smallest))
    return newArray


print(selectSort([75, 31, 46, 5, 23, 14, 38, 2, 55, 33, 65, 101, 1, 7]))


