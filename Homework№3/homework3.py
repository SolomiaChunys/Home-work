with open('file2.txt') as file2, open('file3.txt', 'w') as file3:
    for count, line in enumerate(file2, 1):

        fizz, buzz, number = map(int, line.split())

        conditions = ["F " if not i % fizz and i % buzz else "B " if not i % buzz and i % fizz else "FB " if not i % fizz and not i % buzz else str(i)+' ' for i in range(1, number+1)]
        lines = ''.join(conditions)

        file3.write(f'''
        {count}: {lines}''')

file2.close()
file3.close()
