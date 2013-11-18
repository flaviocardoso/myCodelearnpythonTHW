def hotel_cost(nights):
    return nights * 140

bill = hotel_cost(5)

def add_monthly_interest(balance):
    month = 0.15 / 12
    tax = 1 + month
    return balance * tax

def make_payment(payment, balance):
    result = balance - payment
    return add_monthly_interest(result)
	
    
new_bill = make_payment(bill/2, bill)    

print "You still owe: {}".format(make_payment(100, new_bill))     
    
	
    
   