fizz = int(input('Enter the fizz number: '))
buzz = int(input('Enter the buzz number: '))
number = int(input('Enter the number: '))

output = ''
for i in range(1, number+1):
    if not i % fizz and i % buzz:
        output += "F "
    if not i % buzz and i % fizz:
        output += "B "
    if not i % fizz and not i % buzz:
        output += "FB "
    if i % fizz and i % buzz:
        output += str(i) + ' '

print(output)
