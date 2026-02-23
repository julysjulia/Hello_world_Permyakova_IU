name = input('Введите название питательной среды: ')
concentration = input('Введите концентрацию агара (%): ')
temp = input('Введите температуру стерилизации (°C): ')
with open('recipe.txt', 'w', encoding='utf-8') as recipe:
    recipe.write(f'{name}\n {concentration}\n {temp}')
print('Файл recipe.txt успешно сформирован!')    