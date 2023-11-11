file = open('text_for_practice4(3).txt')

while True:
    summ = 0
    division = 0

    line = file.readline()
    if not line:
        break

    part_of_line = line.split(';')

    part1 = part_of_line[0].split()
    part2 = part_of_line[1].split()

    for i in part1:
        summ += int(i)
        division = summ % int(part2[0])

    if division == int(part2[1]):
        result = True
    else:
        result = False

    print(f'{line.strip()}  {result}')

file.close()

