import pandas as pd

# Load the CSV data
df = pd.read_csv("pop_over_years.csv")

# Remove commas and convert "World Population" to numeric
df["World Population"] = df["World Population"].str.replace(",", "").astype(float)

# Save the cleaned data back to a CSV file
df.to_csv("cleaned_pop_over_years.csv", index=False)
