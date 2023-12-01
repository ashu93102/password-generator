#this is password generator
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
total_letters = ""
for i in range(0, nr_letters + 1):
    total_letters += random.choice(letters)

total_symbols = ""
for i in range(0, nr_symbols + 1):
    total_symbols += random.choice(symbols)

total_num = ""
for i in range(0, nr_numbers + 1):
    total_num += random.choice(numbers)

print(f"Your password is {total_letters}{total_symbols}{total_num}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total_letters = ""
for i in range(0, nr_letters + 1):
    total_letters += random.choice(letters)

total_symbols = ""
for i in range(0, nr_symbols + 1):
    total_symbols += random.choice(symbols)

total_num = ""
for i in range(0, nr_numbers + 1):
    total_num += random.choice(numbers)

password = total_letters + total_symbols + total_num
pass_key = list(password)
random.shuffle(pass_key)
#Converting list to string using map function of lsit comprehension
new_pass = ''.join(map(str, pass_key))


print(f"Your password is {new_pass}")
