import sys

amount = input('Enter the amount of money you want to withdraw: ')
money = int(amount)
if money == 0:
    print('Impossible to issue bills!')
    sys.exit()

if int(amount[-1]) != 0:
    print('Impossible to withdraw bills smaller than 10')
    sys.exit()

one_thousand, five_hundred, two_hundred, one_hundred, fifty, twenty, ten = 0, 0, 0, 0, 0, 0, 0
count = ''
while money != 0:
    if money >= 1000:
        money -= 1000
        one_thousand += 1
    elif money >= 500:
        money -= 500
        five_hundred += 1
    elif money >= 200:
        money -= 200
        two_hundred += 1
    elif money >= 100:
        money -= 100
        one_hundred += 1
    elif money >= 50:
        money -= 50
        fifty += 1
    elif money >= 20:
        money -= 20
        twenty += 1
    elif money >= 10:
        money -= 10
        ten += 1

    else:
        break
if one_thousand != 0:
    count += f', {one_thousand} x 1000'
if five_hundred != 0:
    count += f', {five_hundred} x 500'
if two_hundred != 0:
    count += f', {two_hundred} x 200'
if one_hundred != 0:
    count += f', {one_hundred} x 100'
if fifty != 0:
    count += f', {fifty} x 50'
if twenty != 0:
    count += f', {twenty} x 20'
if ten != 0:
    count += f', {ten} x 10'



print(f'В здачі ви отримаєте такі купюри: {count[1:]} гривень')