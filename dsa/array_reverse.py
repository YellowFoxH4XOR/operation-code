def reverse_array(arr):
    for i in range(0, int(len(arr) / 2)):
        arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
    return arr

print(reverse_array([34, 56, 65]))
assert reverse_array([1,2,3,4,5,6,7]) == [7,6,5,4,3,2,1]