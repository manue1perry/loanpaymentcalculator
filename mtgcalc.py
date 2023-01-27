principal_str = input("How much did you or do you intend to borrow?\n")
annual_rate_str = input("What is the annual rate?\n")
years_str = input("What is the loan term?\n")
no_payments_made_str = input("Have you made any payments so far?\n")

principal = float(principal_str)
annual_rate = float(annual_rate_str)
years = float(years_str)
no_payments_made = float(no_payments_made_str)

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
monthly_payment = monthly_payment_calc(principal,monthly_rate,no_payments)
print("Your monthly payment is or will be ${monthly_payment}".format(monthly_payment=monthly_payment))

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
