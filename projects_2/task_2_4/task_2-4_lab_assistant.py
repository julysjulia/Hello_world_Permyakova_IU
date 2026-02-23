volume = int(input())
mass = volume * 0.009
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("Общий объем: {volume} мл\nМасса соли: {mass:.2f} г\nОбъем воды: {volume} мл")