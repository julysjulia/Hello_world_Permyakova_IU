import pandas as pd
df = pd.read_csv('wild_boars.csv')

q1_group = df.groupby('gender')['length_cm'].quantile(0.25)
q1_Male = q1_group['Male']
q1_Female = q1_group['Female']

q3_group = df.groupby('gender')['length_cm'].quantile(0.75)
q3_Male = q3_group['Male']
q3_Female = q3_group['Female']

iqr_male = q3_Male - q1_Male 
iqr_female = q3_Female - q1_Female

with open('interquartile_ranges', 'w') as file:
    file.write(f"Q1_male (25%): {q1_Male:.2f} cm")
    file.write(f"\nQ3_male (75%): {q3_Male:.2f} cm")
    file.write(f"\nIQR_male: {iqr_male:.2f} cm")
    
    file.write(f"\n\nQ1_female (25%): {q1_Female:.2f} cm")
    file.write(f"\nQ3_female (75%): {q3_Female:.2f} cm")
    file.write(f"\nIQR_female: {iqr_female:.2f} cm")
    