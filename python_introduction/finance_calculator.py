monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = float(monthly_income) - float(monthly_expenses)
project_savings = int(monthly_savings * 12 + (monthly_savings*12*0.05))
print("Your monthly savings are $"+str(monthly_savings)+".")
print("Projected Savings after one year, with interest, is: $" + str(project_savings)+".")

