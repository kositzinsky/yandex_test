def find_smallest(lst: list):
    smallest_num = lst[0]
    smallest_index = 0
    for i in range (1, len(lst) - 1):
        if lst[i] < smallest_num:
            smallest_num = lst[i]
            smallest_index = i
    return smallest_index


def selection_sort(lst: list):
    sorted_lst = []
    for i in range(len(lst) - 1):
        sorted_lst.append(lst.pop(find_smallest(lst)))
    return sorted_lst


print(selection_sort([2, 3, 45, 1, 2, 3]))

def selection_sort2(arr: list):
    count = 0
    for i in range(len(arr)):
        for j in range (i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                count += 1

    return arr, count
            
print(selection_sort2([12,3,123,1,23,1,52,46,546,8,45,6,3457,12345,2457,43,567,3456,345,75,4637,2346,45,754,67,234,5,154,123,45,123456,457]))