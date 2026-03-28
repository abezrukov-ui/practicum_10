def fibonacci(n: int):
    a, b = 1, 1
    if n <= 0:
        print("Число меньше нуля")
        return

    if n == 1:
        print(a)
        return

    print(a, b, end=" ")

    for _ in range(n - 2):
        a, b = b, a + b
        print(b, end=" ")
    print()

fibonacci(55)