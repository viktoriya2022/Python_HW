# ===========================================================
# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]
# ===========================================================

from functools import wraps


def cacher(func):
    cach = {}

    @wraps(func)
    def wrapper(*args):
        key = args
        if key not in cach:
            cach[key] = func(*args)
        print(cach)
        return cach[key]

    return wrapper


@cacher
def seq(n):
    lst = []
    for i in range(n):
        res = (1 + i) ** i
        lst.append(res)
    return lst
    


def main():
    print(seq(5))
    print(seq(1))
    print(seq(7))
    print(seq(5))
    

if __name__ == '__main__':
    main()
