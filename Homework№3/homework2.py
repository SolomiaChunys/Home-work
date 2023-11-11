f = open('file2.txt')
count = 0

while True:
    count += 1
    line = f.readline().split()

    if not line:
        break

    fizz = int(line[0])
    buzz = int(line[1])
    number = int(line[2])

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
    print(f'{count}: {output}')

f.close()

