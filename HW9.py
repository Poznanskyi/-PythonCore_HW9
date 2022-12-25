phone_book = {}


def input_error(func):

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "Enter name user"
        except ValueError:
            return "Phone number not correct!"
        except IndexError:
            return "Enter name and phone namber please!"
    return wrapper


@input_error
def say_hello(lst):
    return "Hello, can I help you?"

@input_error
def add_user(lst):
    phone = str(lst[-1])
    name = " ".join(lst[:-1])
    if phone:
        phone_book[name.title()] = phone
        return f"Contact {name.title()} was created!"
    elif command == phone:
        return "Phone number already exists!"
    else:
        return ""

@input_error
def show_phone(lst):
    name = " ".join(lst)
    return phone_book[name.title()]

@input_error
def show_all(lst):
    if len(phone_book) == 0:
        return "No records"
    text = ""
    for name, phone in phone_book.items():
        text += f"{name} {phone}"
    return text

@input_error
def say_goodbye(lst):
    return "Good bye!"

commands = {
    "hello": say_hello,
    "add": add_user,
    "phone": show_phone,
    "show all": show_all,
    ("good bye", "close", "exit"): say_goodbye,
    }

def main():
    while True:
        command = input("Enter command: ")
        if command == "End":
            break
        command = command.lower().split()
        for key in commands:
            if command[0] in key:
                print(commands[key](command[1:]))

if __name__ == "__main__":
    main()