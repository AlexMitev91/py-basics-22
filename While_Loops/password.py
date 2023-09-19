username = input()
password = input()

while True:
    login_attempt = input()
    if login_attempt == password:
        print(f"Welcome {username}!")
        break