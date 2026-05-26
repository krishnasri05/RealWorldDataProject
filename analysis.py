import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset/sales.csv")

# Show first rows
print(df.head())

# Create graph
df["total_bill"].plot(kind="hist")

# Graph title
plt.title("Total Bill Distribution")

# X label
plt.xlabel("Total Bill")

# Show graph
plt.show()