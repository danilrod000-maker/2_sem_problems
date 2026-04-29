from rational import create, add, sub, mul, div, power, compare, to_int, to_float, to_str
# Тесты
r = create(2, 4)
assert r.numer == 1 and r.denom == 2, "create(2,4) -> 1/2"

r = create(0, 5)
assert r.numer == 0 and r.denom == 1, "create(0,5) -> 0/1"

r = create(1, -2)
assert r.numer == -1 and r.denom == 2, "create(1,-2) -> -1/2"

r = create(-1, -2)
assert r.numer == 1 and r.denom == 2, "create(-1,-2) -> 1/2"

r = create(5, 0)
assert r is None, "create(5,0) -> None"

a = create(1, 2)
b = create(1, 3)
res = add(a, b)
assert res.numer == 5 and res.denom == 6, "add(1/2,1/3) -> 5/6"

res = sub(a, b)
assert res.numer == 1 and res.denom == 6, "sub(1/2,1/3) -> 1/6"

c = create(2, 3)
res = mul(a, c)
assert res.numer == 1 and res.denom == 3, "mul(1/2,2/3) -> 1/3"

res = div(a, c)
assert res.numer == 3 and res.denom == 4, "div(1/2,2/3) -> 3/4"

res = power(c, 2)
assert res.numer == 4 and res.denom == 9, "power(2/3,2) -> 4/9"

assert compare(a, c) == -1, "compare(1/2,2/3) -> -1"
assert compare(c, a) == 1, "compare(2/3,1/2) -> 1"
d = create(2, 4)
assert compare(a, d) == 0, "compare(1/2,2/4) -> 0"

r = create(7, 3)
assert to_int(r) == 2, "to_int(7/3) -> 2"
r = create(-7, 3)
assert to_int(r) == -3, "to_int(-7/3) -> -3"

r = create(1, 3)
assert abs(to_float(r) - 0.3333333333333333) < 1e-9, "to_float(1/3) ~ 0.33333"

# to_str проверяем только что не падет
try:
    to_str(create(3, 4))
except Exception as e:
    assert False, "error"

print("Все тесты пройдены")