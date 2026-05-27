import pandas as pd
df = pd.read_csv('wild_boars.csv')

print(df['tusk_length_cm'])
print(f'Максимальная длина клыков: {df['tusk_length_cm'].max()}')
print(f'Минимальная длина клыков: {df['tusk_length_cm'].min()}')