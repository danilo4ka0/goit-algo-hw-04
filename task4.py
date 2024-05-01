from threading import main_thread


if __name__ == "__main__":
    main_thread()


contacts = {}  # словник для зберігання імен та номерів телефонів

def parse_input(command):
    parts = command.split()
    action = parts[0].lower()
    arguments = parts[1:]
    return action, arguments

def add_contact(name, phone):
    contacts[name] = phone
    print("Contact added.")

def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print("Contact updated.")
    else:
        print("Contact not found.")

def show_phone(name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

def show_all():
    if not contacts:
        print("No contacts available.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def main():
    print("Welcome to the assistant bot!")
    while True:
        
        
        
        command = input("Enter a command: ").strip().lower()
        action, *arguments = parse_input(command)

        if action in ["close", "exit"]:
            print("Good bye!")
            break

        
        if action == "hello":
            print("How can I help you?")

        elif action == "add":
            if len(arguments) == 2:
                add_contact(arguments[0], arguments[1])
            else:
                print("Invalid command. Usage: add [name] [phone]")

        elif action == "change":
            if len(arguments) == 2:
                change_contact(arguments[0], arguments[1])
            else:
                print("Invalid command. Usage: change [name] [new_phone]")

        elif action == "phone":
            if len(arguments) == 1:
                show_phone(arguments[0])
            else:
                print("Invalid command. Usage: phone [name]")

        elif action == "all":
            show_all()

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
