import pandas as pd

df=pd.read_csv('sales_data.csv')

print("=====Generate Statistics=====")

high_sales = df[df["amount"] > 500]

total_sales=df["amount"].sum()
high_sale=df["amount"].max()
average_sales=df["amount"].mean()

print("\n=== HIGH VALUE SALES ===")
print(high_sale)

print("\n=== REPORT ===")
print(f"Total Sales: {total_sales}")
print(f"Average Sale: {average_sales}")

high_sales.to_csv("high_value_sales.csv", index=False)

print("\n✓ Exported high_value_sales.csv")

report = f"""
Total Sales: {total_sales}
Average Sale: {average_sales}
"""

with open("report.txt","w") as file:
    file.write(report)