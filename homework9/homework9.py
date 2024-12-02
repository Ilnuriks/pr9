import re

def split_email(email):
    # Регулярное выражение для проверки и разбивки email
    pattern = r'^(?P<username>[^@]+)@(?P<domain>.+)$'

    match = re.match(pattern, email)
    if match:
        username = match.group('username')
        domain = match.group('domain')
        return username, domain
    else:
        return None, None

def main():
    email = input("Введите ваш email: ")
    username, domain = split_email(email)
    
    if username and domain:
        print(f"username: {username}")
        print(f"domain: {domain}")
    else:
        print("Некорректный email.")

if __name__ == "__main__":
    main()
