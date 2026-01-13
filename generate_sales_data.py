import pandas as pd
import random
from datetime import datetime, timedelta

regions = ["North", "South", "East", "West"]
categories = ["Electronics", "Clothing", "Furniture"]
customer_types = ["New", "Repeat"]

data = []

start_date = datetime(2023, 1, 1)

for i in range(1, 501):
    order_date = start_date + timedelta(days=random.randint(0, 365))
    quantity = random.randint(1, 4)
    unit_price = random.randint(800, 60000)
    discount = random.choice([0, 0.05, 0.1])
    revenue = quantity * unit_price * (1 - discount)

    data.append([
        f"ORD{i:04d}",
        order_date.strftime("%Y-%m-%d"),
        f"CUST{random.randint(100,200)}",
        random.choice(customer_types),
        random.choice(regions),
        random.choice(categories),
        quantity,
        unit_price,
        discount,
        round(revenue, 2)
    ])

df = pd.DataFrame(data, columns=[
    "Order_ID","Order_Date","Customer_ID","Customer_Type",
    "Region","Product_Category","Quantity",
    "Unit_Price","Discount","Revenue"
])

df.to_csv("raw_sales_data.csv", index=False)
