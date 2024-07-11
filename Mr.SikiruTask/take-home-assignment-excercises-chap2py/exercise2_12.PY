# Define the principal, rate, and years
principal = 1000
rate = 0.07  # 7% as a decimal
years = [10, 20, 30]

# Calculate and display the future value for each year
for year in years:
    amount = principal * (1 + rate) ** year
    print(f"After {year} years, you'll have ${amount:.2f}")


