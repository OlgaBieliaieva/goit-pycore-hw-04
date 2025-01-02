def is_valid_phone(phone):
    #Перевіряє, чи є номер телефону валідним
    return phone.isdigit() and len(phone) == 10