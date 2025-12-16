'''Q3:
Given a CSV file Products.csv with columns:
Write a Python program to:

a) Read the CSV

b) Print each row in a clean format

c) Total number of rows

d) Total number of products priced above 500
e) Average price of all products
f) List all products belonging to a specific category (user input)
g) Total quantity of all items in stock'''

import pandas as pd

df=pd.read_csv("D:\Internship(GEN AI)\GEN AI\Day01assignment\products.csv")
print(df)
print("Number of rows:", len(df))
product_count =  len(df[df['price'] > 500])
print("Total number of products priced above 500:", product_count)
average_price = df['price'].mean()
print("Average price of all products:", average_price)
category = input("Enter category: ")
print(df[df['category'] == category])
print("Total quantity of all items in stock:", df['quantity'].sum())