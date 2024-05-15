# debt_payoff.py
# a credit card can have: name, min payment, balance, interest
# to calculate the interest portion balance * (interest / 12) 
# subtract the interest portion from the payment
# then subtract the payment from the balance
debt_name = "my big fat debt"
min_payment = 50.00
interest = .12
balance = 500.00
month = 0
extra_pay = 50.00

while balance > 0:
    month += 1
    # Compute interest portion
    interest_portion = balance * (interest/12)
    # compute how much to apply to balance
    payment = min_payment + extra_pay - interest_portion
    if payment > balance: payment = balance
    balance -= payment
    print(f"Month {month}: You paid ${payment:.2f} towards {debt_name}. Balance left is ${balance:.2f} Interest was: {interest_portion:.2f}") 

print("All done")
