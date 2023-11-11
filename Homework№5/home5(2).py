d = {
    'Brad Pitt': ['Python'],
    'Johnny Depp': ['FrontEnd'],
    'Christian Bale': ['FullStack'],
    'Tom Holland': ['Java'],
    'Heath Ledger': ['Python', 'FullStack', 'Java'],
    'Andrew Garfield': ['FrontEnd', 'Java'],
    'Jacob Elordi': ['FullStack'],
    'Ryan Reynolds': ['FrontEnd', 'Java']
}

More_than_one_group = ''
Dont_learn_frontend = ''
Learn_Java_and_Python = ''

for names, groups in d.items():
    if len(groups) >= 2:
        More_than_one_group += f' {names},'
print(f'Students, who are in more than one group: {More_than_one_group[:-1]}.')

for names, groups in d.items():
    if 'FrontEnd' not in groups and 'FullStack' not in groups:
        Dont_learn_frontend += f' {names},'
print(f'Students, who don`t learn Frontend: {Dont_learn_frontend[:-1]}.')

for names, groups in d.items():
    if 'Python' in groups or 'Java' in groups:
        Learn_Java_and_Python += f' {names},'
print(f'Students, who learn Python or Java: {Learn_Java_and_Python[:-1]}.')