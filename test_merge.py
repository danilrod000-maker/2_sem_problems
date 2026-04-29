import merge_sort as sort
import random


assert sort.merge_sort([]) == []

assert sort.merge_sort([42]) == [42]

assert sort.merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

assert sort.merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

assert sort.merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

assert sort.merge_sort(["banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]

assert sort.merge_sort(["b", "a", "b", "c"]) == ["a", "b", "b", "c"]

original = [3, 2, 1]
copy = original[:]
sorted_arr = sort.merge_sort(original)
assert original == copy
assert sorted_arr == [1, 2, 3]


# избежать рекурсии, использовать один массив, 20000 символов рандом тесты,
print(ord('a'))