import pandas as pd
df = pd.read_csv('wild_boars.csv')

avg_group = df.groupby('gender')['tusk_length_cm'].mean()
std_group = df.groupby('gender')['tusk_length_cm'].std()
co_var_male = (std_group['Male'] / avg_group['Male']) * 100
co_var_female = (std_group['Female'] / avg_group['Female']) * 100

with open('variation_by_tusk_length)', 'w') as file:
    file.write(f'Coefficient of variation of males by tusk length is {co_var_male:.2f} %\n')
    file.write(f'Coefficient of variation of females by tusk length is {co_var_female:.2f} %')