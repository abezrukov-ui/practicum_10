def sms_message(message: str):

    if len(message) <= 160:
        return message
    else:
        return message[:160]

print(sms_message("Х" * 200))
