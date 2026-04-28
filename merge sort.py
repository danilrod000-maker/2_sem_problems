def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # сортировка каждую половину
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    #сливаем две отсортированные половины
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0
    #сравниваем элементы из левой и правой частей и добавляем меньший
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1






    #оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])
    return result






unsorted = input().split()
sorted_arr = merge_sort(unsorted)
#print(unsorted)
print(sorted_arr)