def numbers(A, B):

    if A > B:
        A, B = B, A

    allowed_digits = ['1', '3', '4', '8', '9']

    for num in range(A, B + 1):
        if set(str(num)).issubset(allowed_digits):
            print(num)

numbers(184, 20)