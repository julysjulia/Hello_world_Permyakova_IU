import pandas as pd
df = pd.read_csv('wild_boars.csv')

means = df.mean(numeric_only=True)
avg_litter_females = df[df['gender'] == 'Female']['litter_size'].mean()

with open ("average_characteristics_of_boars", 'w') as file:
    for column, average in means.items():
        param_name = column.replace('_', ' ')
        if param_name == 'litter_size':
            file.write(f"Boars average {param_name} (females only) is {avg_litter_females:.2f}\n")
        elif param_name == 'boar id':
            continue
        else:
            file.write(f"Boars average {param_name} is {average:.2f}\n") 