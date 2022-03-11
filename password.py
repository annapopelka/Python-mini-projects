import random

symbols = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ012456789!@#$%^&*()_+}{|":<>?'

while True:
    password_len = int(input('How many characters in the password do you want: '))
    password_count = int(input('How many passwords do you want to generate: '))
    for _ in range(0,password_count):
        password = ''
        for _ in range(0,password_len):
            password_sym = random.choice(symbols)
            password = password + password_sym
        print('How many passwords do you want to generate:', password)
    break

