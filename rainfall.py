# Daily rainfall observations in mm

rainfall = [12, 15, 8, 20, 10, 25, 18]

# Calculate total rainfall
total_rainfall = sum(rainfall)

# Calculate average rainfall
average_rainfall = total_rainfall / len(rainfall)

# Display results
print("Rainfall Analysis")
print("-----------------")
print("Total rainfall:", total_rainfall, "mm")
print("Average rainfall:", round(average_rainfall, 2), "mm")