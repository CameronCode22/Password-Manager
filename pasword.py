pwd = input("What is the master password?")

def view():
    print("Tim")
    print("Tim")

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'w') as f:
        f.write(name +"|" + pwd)


while True:
    mode = input("Would you like to add a new password or view existing ones")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Inval mode.")
        continue