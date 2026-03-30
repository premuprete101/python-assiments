import pandas as pd

# Read CSV file
df = pd.read_csv("books.csv")

# a) Print complete report
print("\nComplete Book Report:\n")
print(df)

# b) Books by given author
author_name = input("\nEnter author name: ")
print("\nBooks by", author_name)
print(df[df['Author'] == author_name])

# c) Books by given publisher
publisher_name = input("\nEnter publisher name: ")
print("\nBooks by publisher:", publisher_name)
print(df[df['Publisher'] == publisher_name])

# d) Cheapest and costliest books
cheapest = df[df['Price'] == df['Price'].min()]
costliest = df[df['Price'] == df['Price'].max()]

print("\nCheapest Book:")
print(cheapest[['Title', 'Price']])

print("\nCostliest Book:")
print(costliest[['Title', 'Price']])

# e) Sort by year of publication
print("\nBooks sorted by Year:")
print(df.sort_values(by='Year'))