# count items in a list / array

def count(array):
    if array == []:  # check if array is empty
        return 0     # return 0 if empty
    return 1 + count(array[1:])  # other wise return  for the item at index 0 + every other item in the list starting at index 1


list = [1,2,3,4,5,6,7,8,9,11,13,14,18]

print(count(list))