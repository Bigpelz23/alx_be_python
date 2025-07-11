# Prompt user for monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt user for monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% interest
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_annual_savings = annual_savings + interest

# Output results
print(f"\nYour monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected annual savings after 5% interest: ${projected_annual_savings:.2f}")
