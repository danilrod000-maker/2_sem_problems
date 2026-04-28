from rational import create, add, sub, mul, div, power, compare, to_int, to_float, to_str


if __name__ == "__main__":
    # Простые тесты без unittest
    def assert_equal(actual, expected, test_name):
        if actual == expected:
            print(f"[OK] {test_name}")
        else:
            print(f"[FAIL] {test_name}: expected {expected}, got {actual}")

    # 1. create
    r1 = create(2, 4)
    assert_equal((r1.numer, r1.denom), (1, 2), "create сокращает 2/4")

    r2 = create(0, 5)
    assert_equal((r2.numer, r2.denom), (0, 1), "create нулевой числитель")

    r3 = create(1, -2)
    assert_equal((r3.numer, r3.denom), (-1, 2), "create отрицательный знаменатель")

    r4 = create(-3, -4)
    assert_equal((r4.numer, r4.denom), (3, 4), "create два отрицательных")

    r5 = create(5, 0)
    assert_equal(r5, None, "create знаменатель ноль")

    # 2. add
    r6 = create(1, 2)
    r7 = create(1, 3)
    res_add = add(r6, r7)
    assert_equal((res_add.numer, res_add.denom), (5, 6), "add 1/2 + 1/3")

    # 3. sub
    res_sub = sub(r6, r7)
    assert_equal((res_sub.numer, res_sub.denom), (1, 6), "sub 1/2 - 1/3")

    # 4. mul
    res_mul = mul(r6, create(2, 3))
    assert_equal((res_mul.numer, res_mul.denom), (1, 3), "mul 1/2 * 2/3")

    # 5. div
    res_div = div(r6, create(2, 3))
    assert_equal((res_div.numer, res_div.denom), (3, 4), "div (1/2) / (2/3)")

    # 6. power
    res_pow = power(create(2, 3), 2)
    assert_equal((res_pow.numer, res_pow.denom), (4, 9), "power (2/3)^2")

    # 7. compare
    assert_equal(compare(create(1,2), create(2,3)), -1, "compare 1/2 < 2/3")
    assert_equal(compare(create(2,3), create(1,2)), 1, "compare 2/3 > 1/2")
    assert_equal(compare(create(1,2), create(2,4)), 0, "compare 1/2 == 2/4")

    # 8. to_int
    assert_equal(to_int(create(7,3)), 2, "to_int 7/3")
    assert_equal(to_int(create(-7,3)), -3, "to_int -7/3")

    # 9. to_float
    f = to_float(create(1,3))
    if abs(f - 0.3333333333333333) < 1e-9:
        print("[OK] to_float 1/3")
    else:
        print(f"[FAIL] to_float 1/3: got {f}")

    # 10. to_str (проверяем только что не падает)
    try:
        to_str(create(3,4))
        print("[OK] to_str выполнился без ошибок (проверьте вывод вручную)")
    except Exception as e:
        print(f"[FAIL] to_str упал с ошибкой: {e}")