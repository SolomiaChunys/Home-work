import sys

amount = input('Enter the amount of money you want to withdraw: ')
money = int(amount)
if money == 0:
    print('Impossible to issue bills!')
    sys.exit()

if int(amount[-1]) != 0:
    print('Impossible to withdraw bills smaller than 10')
    sys.exit()

bills = [1000, 500, 200, 100, 50, 20, 10]
count = [0, 0, 0, 0, 0, 0, 0]
result = ''

for i in range(7):
    if money >= bills[i]:
        count[i] = money // bills[i]
        money = money % bills[i]

for i in range(7):
    if count[i] != 0:
        result += f', {count[i]} x {bills[i]}'

print(f'В здачі ви отримаєте такі купюри:{result[1:]} гривень')