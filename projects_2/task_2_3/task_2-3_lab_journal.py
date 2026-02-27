name_researcher = input()
date = input()
name_experiment = input()
conclusion = input()
with open('journal.txt', 'w', encoding='utf-8') as file:
    file.write(f'''+{'-'*50}+
|{'Электронный лабораторный журнал':^{50}}|
+{'-'*50}+
| {'ФИО исследователя : ' + name_researcher:<{50-1}}|
| {'Дата              : ' + date:<{50-1}}|
| {'Эксперимент       : ' + name_experiment:<{50-1}}|
+--------------------------------------------------+
| {'Вывод:':<{50-1}}|
''')