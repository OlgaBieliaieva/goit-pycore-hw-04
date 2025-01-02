from command_parser import parse_input
from contacts_manager import add_contact, change_contact, show_phone, show_all
from utils import is_valid_phone

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2:
            _, phone = args
            if is_valid_phone(phone):
                print(add_contact(args, contacts))
            else:
                print("Invalid phone number. Please enter a 10-digit number.")
        elif command == "change" and len(args) == 2:
            print(change_contact(args, contacts))
        elif command == "phone" and len(args) == 1:
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()