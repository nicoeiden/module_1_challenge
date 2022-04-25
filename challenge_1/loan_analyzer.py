
# coding: utf-8
import csv
from pathlib import Path



# Part 1

loan_costs = [500, 600, 200, 1000, 450]

# Calculates the number of loans in the list.
number_of_loans = len(loan_costs)
print(f" There are {number_of_loans} loans in the list.")

# Computes the sum of all the loans in the list.
total_loan_cost = sum(loan_costs)
print(f"The total of all loans in the list is {total_loan_cost}.")

# Calculates the average loan amount from the list.
average_loan_amount = total_loan_cost / number_of_loans
print(f"The average loan amount from the list is {average_loan_amount}.")



# Part 2

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Uses get() on the dictionary to extract the future value and months remaining on the loan, and then prints the values.
future_value = loan.get("future_value")
print(f"The future value of the loan is: {future_value}.")
remaining_months = loan.get("remaining_months")
print(f"There are {remaining_months} months remaining on the loan.")

# Sets the discount rate to 0.2, or 20%.
discount_rate = 0.2

# Uses the variables "future_value", "discount_rate", and "remaining_months" to calculate the present value of the loan.
present_value = future_value / (1 + discount_rate / 12) ** remaining_months

# Uses a conditional statement to evaluate whether the loan is worth it or not.
if (present_value >= loan["loan_price"]):
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price.")



# Part 3

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Defining a function "present_value_function" that calculates the present value of loans given three parameters: future value of the loan, months remaining in the loan, and the annual discount rate.
def present_value_function(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate / 12) ** remaining_months
    return present_value

# Setting annual discount rate equal to 0.2, or 20%.
annual_discount_rate = 0.2

# Using the newly-defined function to calculate the present value of the new loan.
new_loan_present_value = present_value_function(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)
print(f"The present value of the loan is: {new_loan_present_value}")



# Part 4

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Creating a empty list titled "inexpensive_list"
inexpensive_list = []

# Looping through the "loans" dictionary to find loans less than or equal to $500, and then appending them to the empty list "inexpensive_list"
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_list.append(loan["loan_price"])

# Print the `inexpensive_list`
print(inexpensive_list)



# Part 5

# Set the output header.
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set path to the new CSV file.
output_path = Path("inexpensive_loans.csv")

# Opens the new CSV file.
with open(output_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)

    # Uses a for loop to iterate through "inexpensive_list" and uses csvwriter to append the "loan.values()" to a row in the CSV file.
    for loan in inexpensive_list:
        csvwriter.writerow(loan.values())

