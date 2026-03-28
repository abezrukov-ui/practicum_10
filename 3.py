def final_price(cost: float, card: bool, holiday: bool):

    discount = 0.0

    if cost > 30000:
        discount += 10
    elif cost > 20000:
        discount += 7
    elif cost > 15000:
        discount += 5
    elif cost > 5000:
        discount += 3
    if card:
        discount += 5
    if holiday:
        discount += 3
    if discount > 15:
        discount = 15

    final_cost = cost * (1 - discount / 100)

    return round(final_cost, 2)

print(final_price(7500, False, False))
