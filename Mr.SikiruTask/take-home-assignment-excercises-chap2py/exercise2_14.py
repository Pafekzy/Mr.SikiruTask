# Input the user's age
age = int(input("Enter your age: "))

# Calculate the maximum heart rate
max_heart_rate = 220 - age

# Calculate the target heart rate range (50-85% of max)
target_range = (max_heart_rate * 0.5, max_heart_rate * 0.85)

# Display the results
print(f"Your maximum heart rate is {max_heart_rate} beats per minute.")
print(f"Your target heart rate range is {target_range[0]:.0f}-{target_range[1]:.0f} beats per minute.")

