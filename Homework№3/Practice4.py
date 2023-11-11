import sys

amount = input('Enter the amount of money you want to withdraw: ')
money = int(amount)
if money == 0:
    print('Impossible to issue bills!')
    sys.exit()

bill = [10, 20, 50, 100, 200, 500, 1000]

list_of_limit = [[10] * 10, [20] * 10, [50] * 10, [100] * 10, [200] * 10, [500] * 10, [1000] * 10]
if int(amount[-1]) != 0:
    print('Impossible to withdraw bills smaller than 10')
    sys.exit()


count = [0] * 7
result = ''
summ = 0


for i in range(7):
    for j in list_of_limit[i]:
        if money >= j:
            money -= j
            summ += 1
    count[i] = summ
    summ = 0

if money != 0:
    print('Fail')
    print(money)


for i in range(7):
    if count[i] != 0:
        result += f', {count[i]} x {bill[i]}'

print(f'В здачі ви отримаєте такі купюри:{result[1:]} гривень')