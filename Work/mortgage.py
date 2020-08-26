# mortgage.py
#
# Exercise 1.7

extra_payment_start_month = int(input('Month to start extra payments'))
extra_payment_end_month = int(input('Month to end extra payments'))
extra_payment = int(input('Extra payment amount ($)'))

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
i = 0
while principal > 0:
    current_payment = payment
    if extra_payment_end_month > i >= extra_payment_start_month:
        current_payment = current_payment + extra_payment
    principal = principal * (1 + rate / 12) - current_payment
    if principal < 0:
        current_payment = current_payment + principal
        principal = 0
    total_paid = total_paid + current_payment
    i = i + 1
    print(f'{i:5} ${total_paid:6.2f} ${principal:6.2f}')

print(f'Total paid: {total_paid:0.2f}')
print(f'Months: {i}')