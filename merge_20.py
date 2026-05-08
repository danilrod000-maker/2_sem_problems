

def merge_sort_by_key(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr

    n = len(arr)
    temp = [None] * n
    width = 1

    while width < n:
        # Слияние из arr во temp
        for i in range(0, n, 2 * width):
            left = i
            mid = min(i + width, n)
            right = min(i + 2 * width, n)

            l, r, k = left, mid, left
            while l < mid and r < right:
                if key(arr[l]) <= key(arr[r]):
                    temp[k] = arr[l]
                    l += 1
                else:
                    temp[k] = arr[r]
                    r += 1
                k += 1
            while l < mid:
                temp[k] = arr[l]
                l += 1
                k += 1
            while r < right:
                temp[k] = arr[r]
                r += 1
                k += 1

        #копируем temp обратно в arr
        for i in range(n):
            arr[i] = temp[i]

        width *= 2

    return arr