
import linked_2 as function



assert function.length(None) == 0

assert function.length(function.from_list([1])) == 1
assert function.length(function.from_list([1, 2, 3])) == 3


x = function.prepend(None, 5)
assert function.to_list(x) == [5]
x = function.prepend(function.from_list([2, 3]), 1)
assert function.to_list(x) == [1, 2, 3]
x = function.prepend(function.from_list([]), 10)
assert function.to_list(x) == [10]

x = function.from_list([10, 20, 30])
assert function.get(x, 0) == 10
assert function.get(x, 1) == 20
assert function.get(x, 2) == 30

x = function.from_list([7])
assert function.get_last(x) == 7
x = function.from_list([7, 8])
assert function.get_last(x) == 8
x = function.from_list([1, 2, 3, 4])
assert function.get_last(x) == 4


x = function.from_list([1, 2, 3, 2])
assert function.find(x, 2) == 1
assert function.find(x, 3) == 2
assert function.find(x, 9) == -1


x = function.from_list([10, 20, 30])
val, new_x = function.remove(x, 1)
assert val == 20
assert function.to_list(new_x) == [10, 30]

x = function.from_list([1, 2, 3])
val, new_x = function.remove(x, 0)
assert val == 1
assert function.to_list(new_x) == [2, 3]

x = function.from_list([1, 2, 3])
val, new_x = function.remove(x, 2)
assert val == 3
assert function.to_list(new_x) == [1, 2]

x = function.from_list([1, 2, 3, 2])
y = function.remove_first(x, 2)
assert function.to_list(y) == [1, 3, 2]

x = function.from_list([5, 5, 5])
y = function.remove_first(x, 5)
assert function.to_list(y) == [5, 5]

x = function.from_list([1, 2, 3])
y = function.remove_first(x, 9)
assert function.to_list(y) == [1, 2, 3]

x = function.from_list([1, 2, 2, 3, 2])
y = function.remove_all(x, 2)
assert function.to_list(y) == [1, 3]

x = function.from_list([4, 4, 4])
y = function.remove_all(x, 4)
assert function.to_list(y) == []

x = function.from_list([1, 2, 3])
y = function.remove_all(x, 9)
assert function.to_list(y) == [1, 2, 3]


x = function.from_list([1, 2, 3])
y = function.copy(x)
assert function.to_list(y) == [1, 2, 3]
y.next.data = 99
assert function.to_list(x) == [1, 2, 3]
assert function.to_list(y) == [1, 99, 3]

x = function.from_list([])
y = function.copy(x)
assert function.to_list(y) == []

x = function.from_list([7])
y = function.copy(x)
assert function.to_list(y) == [7]

a = function.from_list([1, 2])
b = function.from_list([3, 4])
c = function.concat(a, b)
assert function.to_list(c) == [1, 2, 3, 4]
assert function.to_list(a) == [1, 2]
assert function.to_list(b) == [3, 4]

a = None
b = function.from_list([5, 6])
c = function.concat(a, b)
assert function.to_list(c) == [5, 6]
assert function.to_list(b) == [5, 6]

a = function.from_list([7])
b = None
c = function.concat(a, b)
assert function.to_list(c) == [7]
assert function.to_list(a) == [7]


x = function.from_list([1, 2, 3])
acc = []
function.foreach(x, lambda v: acc.append(v))
assert acc == [1, 2, 3]

x = function.from_list([])
acc = []
function.foreach(x, lambda v: acc.append(v))
assert acc == []

x = function.from_list([5, 6])
tmp = []
function.foreach(x, lambda v: tmp.append(v * 2))
assert tmp == [10, 12]

x = function.from_list([1, 5, 8, 10])
value, index = function.find_custom(x, lambda z: z % 2 == 0 and z > 6)
assert value == 8
assert index == 2

x = function.from_list([3, 4, 5])
value, index = function.find_custom(x, lambda z: z > 10)
assert value is None
assert index == -1


x = function.from_list([2, 4, 6])
value, index = function.find_custom(x, lambda z: z % 2 == 0)
assert value == 2
assert index == 0
arr = [4, 5, 6]
x = function.from_list(arr)
assert function.to_list(x) == [4, 5, 6]
arr = []
x = function.from_list(arr)
assert function.to_list(x) == []
arr = [9]
x = function.from_list(arr)
assert function.to_list(x) == [9]