# Daily rainfall observations in mm

rainfall = [12, 15, 8, 20, 10, 25, 18]

# Calculate total rainfall
total_rainfall = sum(rainfall)

# Calculate average rainfall
average_rainfall = total_rainfall / len(rainfall)

# Count rainy days
rainy_days = 0

for value in rainfall:
    if value > 0:
        rainy_days += 1

# Display results
print("Rainfall Analysis")
print("-----------------")
print("Total rainfall:", total_rainfall, "mm")
print("Average rainfall:", round(average_rainfall, 2), "mm")
print("Number of rainy days:", rainy_days)