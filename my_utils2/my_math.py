from math import sqrt

def find_roots(a, b, c):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return ()
    elif D == 0:
        return -b / (2 * a)
    else:
        return ((-b - sqrt(D)) / 2 * a,
                (-b + sqrt(D)) / 2 * a,
                )
