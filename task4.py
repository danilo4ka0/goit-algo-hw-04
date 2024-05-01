from threading import main_thread



def parse_input(user_input):
    """Parse user input like command and arguments"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(arguments,contacts):
    name,phone=arguments    
    contacts[name] = phone
    print("Contact added.")

def change_contact(arguments,contacts):
    name,phone=arguments 
    if name in contacts:
        
        contacts[name] = phone
        print("Contact updated.")
    else:
        print("Contact not found.")

def show_phone(name,contacts):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

def show_all(contacts):
    print(contacts)
def main():
    print("Welcome to the assistant bot!")
    contacts = {}  # словник для зберігання імен та номерів телефонів
    while True:
        command = input("Enter a command: ").strip().lower()
        action, *arguments = parse_input(command)

        if action in ["close", "exit"]:
            print("Good bye!")
            break

        
        if action == "hello":
            print("How can I help you?")

        elif action == "add":   
            print(arguments)
            add_contact(arguments,contacts)
        elif action == "change":
            change_contact(arguments,contacts)
        elif action == "phone":
            if len(arguments) == 1:
                show_phone(arguments[0],contacts)
            else:
                print("Invalid command. Usage: phone [name]")

        elif action == "all":
            show_all(contacts)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
