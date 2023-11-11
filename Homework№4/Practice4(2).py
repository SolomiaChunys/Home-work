import sys

number = int(input("Enter a positive, odd number: "))

if not number % 2:
    print("Incorrect number, it`s even!!!")
    sys.exit()
elif number <= 0:
    print("Incorrect number, it`s less than or equal zero!!!")
    sys.exit()

for i in range(number):
    if i % 2:
        number_of_spaces = ((number - i) / 2)
        print(int(number_of_spaces)*' ' + i*'*' + int(number_of_spaces)*' ')
for i in range(number, 0, -1):
    if i % 2:
        number_of_spaces = ((number - i) / 2)
        print(int(number_of_spaces)*' ' + i*'*' + int(number_of_spaces)*' ')
