numb = int(input('Введіть число: '))

for i in range(1, numb + 1):
    if not numb % i:
        print(i)
