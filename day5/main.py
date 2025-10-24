print('Welcome to the password generator!')
letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers='0123456789'
symbols='!#$%&()*+'
num_letters=int(input('How many letters would you like in your password?\n'))
num_symbols=int(input('How many symbols would you like?\n'))
num_numbers=int(input('How many numbers would you like?\n'))
import random
password_list=[]
for char in range(num_letters):
    password_list.append(random.choice(letters))
for char in range(num_symbols):
    password_list.append(random.choice(symbols))
for char in range(num_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print(f'Your password is: {password}')
