import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Total sales and revenue
total_sales = df["Quantity"].sum()
total_revenue = df["Revenue"].sum()

print("SALES AND REVENUE ANALYSIS")
print("--------------------------")
print("Total Sales:", total_sales)
print("Total Revenue: Rs.", total_revenue)

# Product-wise revenue
product_sales = df.groupby("Product")["Revenue"].sum()

print("\nProduct-wise Revenue:")
print(product_sales)

# Region-wise revenue
region_sales = df.groupby("Region")["Revenue"].sum()

print("\nRegion-wise Revenue:")
print(region_sales)

# Product revenue chart
product_sales.plot(kind="bar", title="Product-wise Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("product_revenue.png")
plt.show()

# Region revenue chart
region_sales.plot(kind="bar", title="Region-wise Revenue")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("region_revenue.png")
plt.show()
