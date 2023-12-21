arr1 = [1, 7, 3, 6, 2, 9]
arr2 = [1, 2, 3, 4, 5, 6]




def findmid(array):
    for i in range(1, len(array)):
        left = sum(array[0:i])
        right = sum(array[i+1:])

        if left == right:
            return i
    return -1


print(findmid(arr1))
print(findmid(arr2))


