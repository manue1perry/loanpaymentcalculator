def calculate(principal,anual_rate,loan_term):
    no_of_payments = loan_term * 12
    monthly_rate = anual_rate / 12
    if anual_rate is 0:
        monthly_payment = principal/no_of_payments
    else:
        monthly_payment = (principal * monthly_rate)/(1-(1+monthly_rate)**-1)
    return monthly_payment


print(calculate(200,000, 0.05,30))