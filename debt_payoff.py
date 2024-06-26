# debt_payoff.py
# a credit card can have: name, min payment, balance, interest
# to calculate the interest portion balance * (interest / 12) 
# subtract the interest portion from the payment
# then subtract the payment from the balance

# to add: Read debt info from file
# handle multiple debts


from datetime import datetime
from dateutil.relativedelta import relativedelta

debt_name = input("Name of debt: ")
min_payment = float(input("Enter minimum payment: "))
balance = float(input("Enter balance: "))
interest = input("Enter APR as decimal (Default is 0): ")
if interest.strip() == '':
    interest = 0
else:
    interest = float(interest)
extra_pay = input("Enter how much extra to pay each month (Default is 0): ")
if extra_pay.strip() == '':
    extra_pay = 0
else:
    extra_pay = float(extra_pay)
starting_date = input("Enter first payment date. Use 3 character month abbreviation, and year. (ie. Sep 2024): ")
starting_month = starting_date.split()[0]
starting_year = int(starting_date.split()[1])

month = 0


def compute_payoff_month(starting_month, starting_year, month):
    initial_date_string = starting_month + " 1, " + str(starting_year)
    initial_date = datetime.strptime(initial_date_string, "%b %d, %Y")
    payoff_date = initial_date + relativedelta(months=+(month))
    return datetime.strftime(payoff_date, "%b %Y")


total_payments = 0
total_interest = 0
while balance > 0:
    month += 1
    # Compute interest portion
    interest_portion = balance * (interest/12)
    # compute how much to apply to balance
    full_payment = min_payment + extra_pay
    payment = full_payment - interest_portion
    if payment > balance: payment = balance
    balance -= payment
     
    print(f"{debt_name} - Payment amount: ${full_payment:.2f}, of which ${payment:.2f} was applied to the balance, and ${interest_portion:.2f} was interest. Balance left: ${balance:.2f}")
    total_payments += payment
    total_interest += interest_portion

# Need to use month-1 below as the month is increased before the payment. 
print(f"Payoff date is {compute_payoff_month(starting_month, starting_year, (month-1))}")
print(f"A total of ${total_payments + total_interest:.2f} was paid to {debt_name}, of which ${total_interest:.2f} was interest.")

