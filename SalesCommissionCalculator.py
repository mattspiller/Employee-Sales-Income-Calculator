# Author: Matthew Spiller
# Date Modified: February 7, 2022

print("Please input monthly sales: ", end='')
monthly_sales = int(input())

if monthly_sales < 10000:
    admin_fee = 150
    commission_rate = 0.05
elif monthly_sales < 15000:
    admin_fee = 150
    commission_rate = 0.1
elif monthly_sales < 18000:
    admin_fee = 150
    commission_rate = 0.12
elif monthly_sales < 22000:
    admin_fee = 200
    commission_rate = 0.15
else:
    admin_fee = 200
    commission_rate = 0.16

print("Please input payment advance: ", end='')
payment_advance = int(input())

while payment_advance > 1500:
    print("Invalid: Payment advance cannot exceed $1500")
    print("Please input payment advance: ", end='')
    payment_advance = int(input())

# the amount of money made by a salesperson based on their sales, commission rate, admin fee, and payment advance
months_income = monthly_sales * commission_rate - admin_fee - payment_advance

if months_income < 0:
    print("This salesperson is in a loss position of " + str(months_income) + "$, which must be repaid to The Sales Company")
else:
    print("This salesperson's income for the month is $" + str(months_income))
