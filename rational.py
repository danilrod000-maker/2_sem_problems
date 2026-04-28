class Rational:
    pass

def create(num, den):
    if den == 0:
        return None
    res = Rational()
    if num == 0:
        res.numer = 0
        res.denom = 1
        return res
    # перенос знака в числитель
    if den < 0:
        num = -num
        den = -den
    # сокращение дроби через алгоритм Евклида (вычитанием)
    a = abs(num)
    b = den
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    gcd = a
    res.numer = num // gcd
    res.denom = den // gcd
    return res

def add(k, n):
    return create(k.numer * n.denom + n.numer * k.denom, k.denom * n.denom)

def sub(k, n):
    return create(k.numer * n.denom - n.numer * k.denom, k.denom * n.denom)

def mul(k, n):
    return create(k.numer * n.numer, k.denom * n.denom)

def div(k, n):
    return create(k.numer * n.denom, k.denom * n.numer)

def power(k, degree):
    pow_num = k.numer ** degree
    pow_den = k.denom ** degree
    return create(pow_num, pow_den)

def compare(k, n):
    left = k.numer * n.denom
    right = n.numer * k.denom
    if left < right:
        return -1
    elif left == right:
        return 0
    else:
        return 1

def to_int(r):
    return r.numer // r.denom

def to_float(r):
    return r.numer / r.denom

def to_str(r):
    print(f'{r.numer}/{r.denom}')






