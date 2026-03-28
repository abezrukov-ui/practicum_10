def prosto(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prosto_N():
    try:
        N = int(input("Введите натуральное число N: "))
        if N < 1:
            print("Ошибка: N должно быть натуральным числом (>=1)")
            return

        for _ in range(1, N + 1):
            if prosto(_):
                print(_)
    except ValueError:
        print("Ошибка: нужно ввести целое число")

prosto_N()