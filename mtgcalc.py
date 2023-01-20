def monthly_payment_calc(principal,annual_rate,loan_term):
    no_payments = loan_term * 12
    monthly_rate = annual_rate / 12
    if annual_rate == 0:
        monthly_payment = principal/no_payments
    else:
        rP = monthly_rate * principal
        rN = (1 + monthly_rate)**(-1 * no_payments)
        monthly_payment = rP/(1-rN)

    return monthly_payment


