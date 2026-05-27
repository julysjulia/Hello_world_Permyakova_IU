import pandas as pd
df = pd.read_csv('wild_boars.csv')

medians = df.median(numeric_only=True)
median_litter_females = df[df['gender'] == 'Female']['litter_size'].median()

with open ("median_characteristics_of_boars", 'w') as file:
    for column, median in medians.items():
        param_name = column.replace('_', ' ')
        if param_name == 'litter_size':
            file.write(f"Boars median {param_name} (females only) is {median_litter_females:.2f}\n")
        elif param_name == 'boar id':
            continue
        else:
            file.write(f"Boars median {param_name} is {median:.2f}\n") 