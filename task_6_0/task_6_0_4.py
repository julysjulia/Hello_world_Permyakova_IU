import pandas as pd
df = pd.read_csv('wild_boars.csv')

modes = df.mode().iloc[0]
mode_litter_females = df[df['gender'] == 'Female']['litter_size'].mode().iloc[0]

with open ("mode_characteristics_of_boars", 'w') as file:
    for column, mode in modes.items():
        param_name = column.replace('_', ' ')
        if param_name == 'litter_size':
            file.write(f"Boars mode {param_name} (females only) is {mode_litter_females}\n")
        elif param_name == 'boar id':
            continue
        else:
            file.write(f"Boars mode {param_name} is {mode}\n") 