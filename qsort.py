# Quick sort with python
# divide and sort with pivot

def quick_sort(array):
    if len(array) < 2:
        return array

    else:
        pivot = array[0]

        less = [i for i in array[1:] if i <= pivot]

        greater = [ i for i in array[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([3,1,13,5,39,25,7,4]))

##### [1, 3, 4, 5, 7, 13, 25, 39]

