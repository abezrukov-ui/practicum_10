def find_kratno(a: int, b: int, N: int) :

    min_kratno = a * b

    multi = min_kratno

    while multi <= N:
        print(multi)
        multi += min_kratno

find_kratno(3, 5, 100)
