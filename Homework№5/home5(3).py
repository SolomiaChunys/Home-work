entered_size = input('Enter the international size you want to convert (XXS|XS|S|M|L|XL|XXL|XXXL): ')
entered_country = input('Enter the country in which you want to convert (Germany|USA|France|Great Britain): ')

country_size = {
    'GERMANY': [("XXS", 36), ("XS", 38), ("S", 40), ("M", 42), ("L", 44), ("XL", 46), ("XXL", 48), ("XXXL", 50)],
    'USA': [("XXS", 8), ("XS", 10), ("S", 12), ("M", 14), ("L", 16), ("XL", 18), ("XXL", 20), ("XXXL", 22)],
    'FRANCE': [("XXS", 38), ("XS", 40), ("S", 42), ("M", 44), ("L", 46), ("XL", 48), ("XXL", 50), ("XXXL", 52)],
    'GREAT BRITAIN': [("XXS", 24), ("XS", 26), ("S", 28), ("M", 30), ("L", 32), ("XL", 34), ("XXL", 36), ("XXXL", 38)]
}

converted_size = 0
for country, sizes in country_size.items():
    if entered_country.upper() == country:
        for size, value in sizes:
            if entered_size.upper() == size:
                converted_size = value

if converted_size != 0:
    print(f'Size "{entered_size}" in {entered_country} is {converted_size}')
else:
    print('Invalid input. Please enter a valid size and country!')