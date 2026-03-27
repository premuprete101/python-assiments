Practical No: 5

Lab Assignment-1

Develop a program that asks the user to enter a series of integers and store them ina Tuple.

Develop a program that asks the user to enter a series of integers and store them in a Tuple. Perform the following:

a) Print the total number of items in the Tuple.

b) Print the last item in the Tuple.

c) Print the Tuple elements in reverse order

d) Print Yes if the Tuple contains an integer 5 and No otherwise.

e) Remove the first and last items from the Tuple, sort the remaining items, and print the result.

Lab Assignment-2

Create a program to store the Prices of sold items on a particular day of a shop in a Tuple.

Perform the following operations: a) Print the total number of items sold

b) Print the price of cheapest item sold

c) Print the price of costliest item sold

d) Print the price list in ascending order

e) Print the number of costliest items sold on the day

CODE
 Lab Assignment – 1 (Tuple Operations)
# Taking input from user
nums = input("Enter integers separated by space: ")

# Converting input string to tuple of integers
t = tuple(map(int, nums.split()))

# a) Total number of items
print("Total number of items:", len(t))

# b) Last item
if len(t) > 0:
    print("Last item:", t[-1])
else:
    print("Tuple is empty")

# c) Reverse order
print("Tuple in reverse order:", t[::-1])

# d) Check if 5 is present
if 5 in t:
    print("Yes")
else:
    print("No")

# e) Remove first & last, sort remaining
if len(t) > 2:
    new_tuple = tuple(sorted(t[1:-1]))
    print("Sorted tuple after removing first and last:", new_tuple)
else:
    print("Not enough elements to remove first and last")


Lab Assignment – 2 (Shop Price Analysis)
# Input prices
prices_input = input("Enter prices of items separated by space: ")

# Convert to tuple
prices = tuple(map(float, prices_input.split()))

# a) Total items sold
print("Total items sold:", len(prices))

# b) Cheapest item
if len(prices) > 0:
    print("Cheapest item price:", min(prices))
else:
    print("No items")

# c) Costliest item
if len(prices) > 0:
    print("Costliest item price:", max(prices))
else:
    print("No items")

# d) Prices in ascending order
sorted_prices = tuple(sorted(prices))
print("Prices in ascending order:", sorted_prices)

# e) Number of costliest items sold
if len(prices) > 0:
    max_price = max(prices)
    count = prices.count(max_price)
    print("Number of costliest items sold:", count)✅ Lab Assignment – 1 (Tuple Operations)
# Taking input from user
nums = input("Enter integers separated by space: ")

# Converting input string to tuple of integers
t = tuple(map(int, nums.split()))

# a) Total number of items
print("Total number of items:", len(t))

# b) Last item
if len(t) > 0:
    print("Last item:", t[-1])
else:
    print("Tuple is empty")

# c) Reverse order
print("Tuple in reverse order:", t[::-1])

# d) Check if 5 is present
if 5 in t:
    print("Yes")
else:
    print("No")

# e) Remove first & last, sort remaining
if len(t) > 2:
    new_tuple = tuple(sorted(t[1:-1]))
    print("Sorted tuple after removing first and last:", new_tuple)
else:
    print("Not enough elements to remove first and last")
✅ Lab Assignment – 2 (Shop Price Analysis)
# Input prices
prices_input = input("Enter prices of items separated by space: ")

# Convert to tuple
prices = tuple(map(float, prices_input.split()))

# a) Total items sold
print("Total items sold:", len(prices))

# b) Cheapest item
if len(prices) > 0:
    print("Cheapest item price:", min(prices))
else:
    print("No items")

# c) Costliest item
if len(prices) > 0:
    print("Costliest item price:", max(prices))
else:
    print("No items")

# d) Prices in ascending order
sorted_prices = tuple(sorted(prices))
print("Prices in ascending order:", sorted_prices)

# e) Number of costliest items sold
if len(prices) > 0:
    max_price = max(prices)
    count = prices.count(max_price)
    print("Number of costliest items sold:", count)  
