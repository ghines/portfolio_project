# debt_payoff.py
# a credit card can have: name, min payment, balance, interest
# to calculate the interest portion balance * (interest / 12) 
# subtract the interest portion from the payment
# then subtract the payment from the balance

from datetime import datetime
from dateutil.relativedelta import relativedelta

debt_name = "my big fat debt"
min_payment = 50.00
interest = .12
balance = 500.00
month = 0
extra_pay = 00.00
starting_month = "Jun"
starting_year = 2024

def compute_payoff_month(starting_month, starting_year, month):
    initial_date_string = starting_month + " 1, " + str(starting_year)
    initial_date = datetime.strptime(initial_date_string, "%b %d, %Y")
    payoff_date = initial_date + relativedelta(months=+(month-1))
    return datetime.strftime(payoff_date, "%b %Y")


while balance > 0:
    month += 1
    # Compute interest portion
    interest_portion = balance * (interest/12)
    # compute how much to apply to balance
    payment = min_payment + extra_pay - interest_portion
    if payment > balance: payment = balance
    balance -= payment
    print(f"Month {month}: You paid ${payment:.2f} towards {debt_name}. Balance left is ${balance:.2f} Interest was: {interest_portion:.2f}") 


# Need to use month-1 below as the month is increased before the payment. 
print(f"Payoff date is {compute_payoff_month(starting_month, starting_year, (month-1))}")

