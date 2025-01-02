def add_contact(args, contacts):
    #Додає контакт до словника
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    #Змінює номер телефону контакту
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    #Показує номер телефону контакту
    name = args[0]
    if name in contacts:
        return f"The phone number of {name} is {contacts[name]}."
    else:
        return "Contact not found."

def show_all(contacts):
    #Показує всі контакти
    if not contacts:
        return "No contacts saved."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])