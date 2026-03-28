def phone_card_value(cost):

    if cost == 5 or cost == 10:
        print(cost)
    elif cost == 25:
        print(cost + 3)
    elif cost == 50:
        print(cost + 8)
    elif cost == 100:
        print(cost + 20)
    else:
        print("Нет! - Только 5, 10, 25, 50 или 100")

phone_card_value(30)


