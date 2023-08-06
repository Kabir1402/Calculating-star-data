import pandas as pd

# Load the cleaned merged CSV file
cleaned_merged_df = pd.read_csv('cleaned_merged_stars.csv')

# Convert mass into kilograms by multiplying with 1.989e+30
cleaned_merged_df['Mass'] *= 1.989e+30

# Convert radius into meters by multiplying with 6.957e+8
cleaned_merged_df['Radius'] *= 6.957e+8

# Make an empty list to store gravity values
gravity_values = []

# Write a function to calculate gravity
def calculate_gravity(mass, radius):
    G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
    gravity = (G * mass) / (radius ** 2)
    return gravity

# Calculate gravity for each row and append to gravity_values list
for index, row in cleaned_merged_df.iterrows():
    gravity = calculate_gravity(row['Mass'], row['Radius'])
    gravity_values.append(gravity)

# Add the gravity column to the DataFrame
cleaned_merged_df['Gravity'] = gravity_values

# Save the updated DataFrame to a new CSV file
final_dataset_csv = 'final_dataset.csv'
cleaned_merged_df.to_csv(final_dataset_csv, index=False)

print("Final dataset saved to 'final_dataset.csv'")
  