# code to get sum of an array / list

def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

A = [3,5,7,2,8,4]

print(sum(A))

