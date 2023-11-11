number = input("Введіть число: ")

digit = len(number)-1
# Виведення розрядів та їх множників
for el in number:
    print(f"множник {el} і його розряд {digit}")
    digit -= 1
