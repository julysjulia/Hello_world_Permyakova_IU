weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (м): "))

bmi = weight / (height ** 2)
print(f"Вес:\t {weight}\nРост:\t {height} м.\nИндекс массы тела пациента: {bmi:.2f}") 