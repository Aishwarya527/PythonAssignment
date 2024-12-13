
salary = float(input("Enter your salary: "))
bill1 = float(input("Enter the amount of first shopping bill: "))
bill2 = float(input("Enter the amount of second shopping bill: "))
bill3 = float(input("Enter the amount of third shopping bill: "))
total_shopping_amount = bill1 + bill2 + bill3
percentage = (total_shopping_amount / salary) * 100
print(f"Total shopping amount: {total_shopping_amount}")
print(f"Percentage of salary spent on shopping: {percentage:.2f}%")
