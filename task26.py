username = input("username: ")

if username.replace('-', '').isalpha():
    print('qabul qilindi')

else:
    print('usernames faqat a-z, A-Z, 0-9, - dan iborat bolishi kearak')