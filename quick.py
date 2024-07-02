arr = [5, 3, 8, 4, 9, 1, 6, 2, 7]

def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            less_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick(less_arr) + equal_arr + quick(greater_arr)


print(quick(arr))
