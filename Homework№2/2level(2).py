age = int(input('Enter your age: '))

adult = 0
if age >= 18:
    adult = True
print('You are already of legal age!' if adult else 'You are still a child!')

