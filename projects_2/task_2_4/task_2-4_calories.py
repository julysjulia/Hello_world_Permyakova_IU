proteins = int(input())
fats = int(input())
carbs = int(input())
calories = proteins * 4 + fats * 9 + carbs * 4
print(f'{calories}=({proteins}×4)+({fats}×9)+({carbs}×4)')