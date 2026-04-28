
class Rational:
    pass

def create(num, den):
    res = Rational()
    if den == 0:
        return None

    elif num == 0:
        res.numer = num
        res.denom = 1

    elif num < 0 or den < 0:
        num, den = (-abs(num)), abs(den)

    else:
        a = num
        b = den
        while a != b: #евклид где а - НОД
            if a > b:
                a = a - b
            else:
                b = b - a
        res.numer = abs(den / a)
        res.denom = abs(num / a)
        return res


def add(k,n):
    return create(k.numer * n.denom + k.denom + n.numer, k.denom * n.denom)

def sub(k,n):#вычитание
    return create(k.numer * n.denom - k.denom + n.numer, k.denom * n.denom)

def mul(k,n):#умножение
    return create(k.numer * n.numer, k.denom * n.denom)

def div(k, n):
    return create(k.numer * n.denom, k.denom * n.numer)

def power(k, degree):
    pow_num = (k.numer) ** degree
    pow_den = (k.denom) ** degree
    return create(pow_num, pow_den)

def compare(k,n):
    if sub(k,n) :
        return -1
    elif sub(k,n) == create(0, 1):
        return 0
    else:
        return 1


def to_int(r):
    divised = r.numer // r.denom
    return divised

def to_float(r):
    return r.numer / r.denom



def to_str(r):
    s = create(r.numer, r.denom)
    print(f'{s.numer}/{s.denom}')









