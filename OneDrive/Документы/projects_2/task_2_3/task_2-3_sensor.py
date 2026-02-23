name = input('Введите имя оператора: ')
presure = input('Введите текущее значение давления (Па): ')
with open("sensor_log.txt", "w", encoding="utf-8") as f:
    f.write(f"{name}\t {presure}\n")
print('Данные успешно сохранены в sensor_log.txt')