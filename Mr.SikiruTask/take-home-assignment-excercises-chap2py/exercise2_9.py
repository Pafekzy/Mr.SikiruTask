# Input three integers from the user
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))

# Calculate the sum, average, and product
sum = num1 + num2 + num3
average = sum / 3
product = num1 * num2 * num3

# Determine the smallest and largest numbers
smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)

# Display the results
print("Sum:", sum)
print("Average:", average)
print("Product:", product)
print("Smallest:", smallest)
print("Largest:", largest)
