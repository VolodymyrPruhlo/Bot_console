import re


def hello_func():
    return 'Hello how can i help you?'


def add_contacts(contacts):
    def inner(command):
        result = command.split()
        command_add, name, new_phone = result
        all_contacts = [f'{k}: {v}' for k, v in contacts.items()]

        if f'{name}: {new_phone}' in all_contacts:
            return 'Contact not exist'
        else:
            contacts[name] = new_phone
            return f"Contact '{name}' with phone '{new_phone}' added successfully."
    return inner


def change_contact(contacts):
    def inner(command):
        result = command.split()
        command_change, name, new_phone = result
        names_contact = [k for k in contacts.keys()]

        if name in names_contact:
            contacts[name] = new_phone
            return f'The phone number has been successfully replaced in the contact {name}.'
        else:
            return 'Contact not exist'
    return inner


def phone_contact(contacts):
    def inner(command):
        result = command.split()
        command_phone, name = result
        names_contact = [k for k in contacts.keys()]

        if name in names_contact:
            return contacts[name]
        else:
            return 'Contact not found'
    return inner


def show_all_func(contacts):
    if not contacts:
        return 'Contacts is empty'
    else:
        result = [f'{k}: {v}' for k, v in contacts.items()]
        return '\n'.join(result)


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except (KeyError, TypeError, IndexError) as e:
            return str(e)
    return wrapper


@input_error
def handler(contacts):
    def inner(command):

        parts = command.split()
        pattern_for_name = r"^[a-zA-Zа-яА-ЯІіЇї\s'\".,-]{2,}$"
        pattern_for_phone = r"\+38\d{10}|0\d{9}|38\d{10}"

        if command == 'hello':
            hello_function = hello_func()
            return hello_function

        elif parts[0] == 'add':
            if len(command.split()) != 3:
                return "Invalid format. Please use 'add NAME PHONE' format."
            else:
                if re.match(pattern_for_name, parts[1]) and re.match(pattern_for_phone, parts[2]):
                    add_func = add_contacts(contacts)
                    return add_func(command)
                return 'invalid Name or Phone, please check again'

        elif parts[0] == 'change':
            if len(command.split()) != 3:
                return "Invalid format. Please use 'change NAME PHONE' format."
            else:
                if re.match(pattern_for_name, parts[1]) and re.match(pattern_for_phone, parts[2]):
                    change_func = change_contact(contacts)
                    return change_func(command)
                return 'invalid Name or Phone, please check again'

        elif parts[0] == 'phone':
            if len(command.split()) != 2:
                return "Invalid format. Please use 'phone NAME' format."
            else:
                if re.match(pattern_for_name, parts[1]):
                    phone_func = phone_contact(contacts)
                    return phone_func(command)
                return 'invalid Name, please check again'

        elif parts[0] == 'show' and len(parts) == 2 and parts[1] == 'all':
            show_all_function = show_all_func(contacts)
            return show_all_function

        else:
            return "Command not recognized"
    return inner



def main():
    contacts = {}
    print('Welcome to assist bot')

    while True:
        command = input('Enter command: ')

        if command == 'close':
            print('Good bye')
            break
        else:
            response = handler(contacts)
            print(response(command))


if __name__ == '__main__':
    main()
