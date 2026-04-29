# ---- Тесты для create ----
# Нормальное сокращение
r = create(6, 8)
assert r.numer == 3 and r.denom == 4

# Нулевой числитель
r = create(0, 10)
assert r.numer == 0 and r.denom == 1

# Отрицательный знаменатель -> знак в числитель
r = create(3, -5)
assert r.numer == -3 and r.denom == 5

# Два отрицательных -> дробь положительная
r = create(-4, -6)
assert r.numer == 2 and r.denom == 3

# Отрицательный числитель
r = create(-5, 7)
assert r.numer == -5 and r.denom == 7

# Знаменатель 0 -> None
r = create(1, 0)
assert r is None
r = create(-1, 0)
assert r is None
r = create(0, 0)
assert r is None

# Сокращение с отрицательными
r = create(-8, 12)
assert r.numer == -2 and r.denom == 3

# Большие числа
r = create(123456, 246912)
assert r.numer == 1 and r.denom == 2  # 123456*2 = 246912

# Единица
r = create(7, 7)
assert r.numer == 1 and r.denom == 1

# ---- Тесты для add ----
a = create(1, 2)
b = create(1, 3)
res = add(a, b)
assert res.numer == 5 and res.denom == 6

# Сложение с нулём
zero = create(0, 1)
res = add(a, zero)
assert res.numer == a.numer and res.denom == a.denom

# Сложение отрицательных
neg = create(-1, 2)
res = add(a, neg)
assert res.numer == 0 and res.denom == 1

# Сложение двух отрицательных
res = add(neg, create(-1, 3))
assert res.numer == -5 and res.denom == 6

# Сложение с целым числом (знаменатель 1)
whole = create(2, 1)
res = add(a, whole)
assert res.numer == 5 and res.denom == 2  # 1/2 + 2 = 5/2

# ---- Тесты для sub ----
a = create(2, 3)
b = create(1, 3)
res = sub(a, b)
assert res.numer == 1 and res.denom == 3

# Вычитание нуля
zero = create(0, 1)
res = sub(a, zero)
assert res.numer == a.numer and res.denom == a.denom

# Вычитание отрицательного = сложение
neg = create(-1, 3)
res = sub(a, neg)
assert res.numer == 1 and res.denom == 1  # 2/3 - (-1/3) = 1

# Вычитание из нуля
res = sub(zero, a)
assert res.numer == -2 and res.denom == 3

# Вычитание равных дробей
res = sub(a, a)
assert res.numer == 0 and res.denom == 1

# ---- Тесты для mul ----
a = create(2, 3)
b = create(3, 4)
res = mul(a, b)
assert res.numer == 1 and res.denom == 2  # 2/3 * 3/4 = 6/12 = 1/2

# Умножение на ноль
zero = create(0, 1)
res = mul(a, zero)
assert res.numer == 0 and res.denom == 1

# Умножение отрицательных
neg = create(-2, 3)
res = mul(neg, create(3, 4))
assert res.numer == -1 and res.denom == 2

# Умножение двух отрицательных
res = mul(neg, create(-3, 4))
assert res.numer == 1 and res.denom == 2

# Умножение на единицу
one = create(1, 1)
res = mul(a, one)
assert res.numer == a.numer and res.denom == a.denom

# ---- Тесты для div ----
a = create(2, 3)
b = create(4, 5)
res = div(a, b)
assert res.numer == 5 and res.denom == 6  # (2/3)/(4/5) = 10/12 = 5/6

# Деление на 1
one = create(1, 1)
res = div(a, one)
assert res.numer == a.numer and res.denom == a.denom

# Деление на отрицательное
neg = create(-1, 2)
res = div(a, neg)
assert res.numer == -4 and res.denom == 3  # (2/3)/(-1/2) = -4/3

# Деление нуля
zero = create(0, 1)
res = div(zero, a)
assert res.numer == 0 and res.denom == 1

# Деление на ноль (должно вернуть None)
b_zero = create(0, 1)
res = div(a, b_zero)
assert res is None

# Деление отрицательного на отрицательное
res = div(create(-2, 3), create(-4, 5))
assert res.numer == 5 and res.denom == 6

# ---- Тесты для power ----
a = create(2, 3)
res = power(a, 2)
assert res.numer == 4 and res.denom == 9

res = power(a, 0)
assert res.numer == 1 and res.denom == 1

res = power(a, 1)
assert res.numer == 2 and res.denom == 3

res = power(create(1, 2), 3)
assert res.numer == 1 and res.denom == 8

# Степень с отрицательным основанием
neg = create(-2, 3)
res = power(neg, 2)
assert res.numer == 4 and res.denom == 9  # знак уходит в квадрат

res = power(neg, 3)
assert res.numer == -8 and res.denom == 27

# Степень с нулевым числителем
zero = create(0, 5)
res = power(zero, 3)
assert res.numer == 0 and res.denom == 1

# Отрицательная степень? Функция не поддерживает, но проверим поведение
# Если передать отрицательный degree, может быть ошибка или дробь. Пропустим по заданию.

# ---- Тесты для compare ----
a = create(1, 2)
b = create(2, 3)
assert compare(a, b) == -1
assert compare(b, a) == 1
assert compare(a, create(2, 4)) == 0

# Сравнение с отрицательными
neg = create(-1, 2)
assert compare(neg, a) == -1
assert compare(neg, create(-2, 4)) == 0
assert compare(create(-2, 3), create(-1, 2)) == -1  # -2/3 < -1/2

# Сравнение с нулём
zero = create(0, 1)
assert compare(zero, a) == -1
assert compare(a, zero) == 1
assert compare(zero, create(0, 5)) == 0

# Сравнение больших чисел
big1 = create(100, 200)
big2 = create(150, 300)
assert compare(big1, big2) == 0

# ---- Тесты для to_int ----
r = create(7, 3)
assert to_int(r) == 2
r = create(-7, 3)
assert to_int(r) == -3
r = create(5, 1)
assert to_int(r) == 5
r = create(0, 10)
assert to_int(r) == 0
r = create(1, 2)
assert to_int(r) == 0  # целая часть 0
r = create(-1, 2)
assert to_int(r) == -1  # -0.5 округляется вниз до -1

# ---- Тесты для to_float ----
r = create(1, 3)
assert abs(to_float(r) - 0.3333333333333333) < 1e-9
r = create(2, 5)
assert abs(to_float(r) - 0.4) < 1e-9
r = create(-3, 2)
assert abs(to_float(r) + 1.5) < 1e-9
r = create(0, 1)
assert to_float(r) == 0.0

# ---- Тесты для to_str (проверяем, что не падает и выводит корректно) ----
import sys
from io import StringIO

captured = StringIO()
sys.stdout = captured
to_str(create(3, 4))
sys.stdout = sys.__stdout__
assert captured.getvalue().strip() == "3/4"

captured = StringIO()
sys.stdout = captured
to_str(create(-2, 5))
sys.stdout = sys.__stdout__
assert captured.getvalue().strip() == "-2/5"

captured = StringIO()
sys.stdout = captured
to_str(create(0, 1))
sys.stdout = sys.__stdout__
assert captured.getvalue().strip() == "0/1"

print("Все расширенные тесты пройдены")