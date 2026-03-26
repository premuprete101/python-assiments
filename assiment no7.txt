Practical No: 7

Lab Assignment-1

Create a Menu Driven application "CALC" by implemnting different functions for the following basic operations:

a) Addition

b) Subtraction

c) Multiplication

d) Division

e) Modulus

# Functions for operations
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def mod(a, b):
    if b != 0:
        return a % b
    else:
        return "Cannot perform modulus by zero"

# Menu-driven program
while True:
    print("\n--- CALC MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("Exiting Calculator...")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(a, b))
    elif choice == 2:
        print("Result:", sub(a, b))
    elif choice == 3:
        print("Result:", mul(a, b))
    elif choice == 4:
        print("Result:", div(a, b))
    elif choice == 5:
        print("Result:", mod(a, b))
    else:
        print("Invalid choice")

LA2

Lab Assignment-2

Create a Menu Driven program for showing details of a Bank Account by implementaing different functions for the

following:

a) Display the current Balance

b) Mechanism to Deposit an amount

c) Mechanism to Withdraw an amount

# Initial balance
balance = 0

# Functions
def display_balance():
    print("Current Balance:", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited Successfully")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Amount Withdrawn Successfully")
    else:
        print("Insufficient Balance")

# Menu-driven program
while True:
    print("\n--- BANK MENU ---")
    print("1. Display Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Thank you!")
        break

    if choice == 1:
        display_balance()
    elif choice == 2:
        amt = float(input("Enter amount to deposit: "))
        deposit(amt)
    elif choice == 3:
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)
    else:
        print("Invalid choice")
