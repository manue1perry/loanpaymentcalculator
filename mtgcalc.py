principal = 200000
annual_rate = 0.05
years = 30
no_payments_made = 15

no_payments = years * 12
monthly_rate = annual_rate / 12

def monthly_payment_calc(principal,monthly_rate,no_payments):
    
    if monthly_rate == 0:
        monthly_payment = principal/no_payments
    else:
        rP = monthly_rate * principal
        rN = (1 + monthly_rate)**(-1 * no_payments)
        monthly_payment = rP/(1-rN)
    
    return monthly_payment

#test
monthly_payment = monthly_payment_calc(principal,annual_rate,no_payments)
print("Your monthly payment will be {monthly_payment}".format(monthly_payment=monthly_payment))

def interest(principal, monthly_rate, monthly_payment, no_payments_made, no_payments):
    
    total_interest = no_payments * monthly_payment - principal

    rpc = principal * monthly_rate - monthly_payment
    rn = (1 + monthly_rate)**(no_payments_made)
    cn = monthly_payment * no_payments_made
    cumilitive_interest = rpc*(rn-1)/monthly_rate + cn
    
    return total_interest, cumilitive_interest

#test
total_interest, cumilitive_interest = interest(principal, monthly_rate, monthly_payment, no_payments_made, no_payments)
print("You have paid ${interest} in interest so far.".format(interest=cumilitive_interest))
print("Your total interest at the end of the loan term will be ${tot_int}".format(tot_int = total_interest))
