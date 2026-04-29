import random

from merge_sort import merge_sort

arr = []
result = merge_sort(arr)
assert result == []



arr = ["5"]
result = merge_sort(arr)
assert result == ["5"]



arr = ["9", "1"]
result = merge_sort(arr)
assert result == ["1", "9"]


arr = ["1", "2", "3", "4", "5"]
result = merge_sort(arr)
assert result == ["1", "2", "3", "4", "5"]

arr = ["5", "4", "3", "2", "1"]
result = merge_sort(arr)
assert result == ["1", "2", "3", "4", "5"]

arr = ["3", "1", "3", "2", "1", "2"]
result = merge_sort(arr)
assert result == ["1", "1", "2", "2", "3", "3"]

arr = ["7", "7", "7", "7", "7"]
result = merge_sort(arr)
assert result == ["7", "7", "7", "7", "7"]

arr = ["-5", "10", "-3", "0", "7", "-10"]
result = merge_sort(arr)
assert result == ["-10", "-5", "-3", "0", "7", "10"]

arr = [str(random.randint(0, 1000)) for _ in range(100)]
expected = sorted(arr, key=lambda x: int(x))
result = merge_sort(arr)
assert result == expected

arr = [str(random.randint(0, 10000)) for _ in range(1000)]
expected = sorted(arr, key=lambda x: int(x))
result = merge_sort(arr)
assert result == expected


arr = [str(random.randint(0, 100000)) for _ in range(10000)]
expected = sorted(arr, key=lambda x: int(x))
result = merge_sort(arr)
assert result == expected




arr = [str(random.randint(0, 1000000)) for _ in range(100000)]
expected = sorted(arr, key=lambda x: int(x))
result = merge_sort(arr)
assert result == expected

print('Done')