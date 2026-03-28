def make_payment(p: float):

    credit_limit = 1000
    min_payment = 20

    if p < min_payment:
        print("Повторить попытку")
    elif p > credit_limit:
        print("Повторить попытку")
    else:
        print("Успех")

make_payment(10)
