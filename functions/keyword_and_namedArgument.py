# keywords arguments

def get_total(price, qty=1, tax=0.2, discount=0):
    subtotal = price * qty * (1 - discount)
    total_tax = subtotal * (1 + tax)
    total = subtotal + total_tax
    print(total)
    return total

get_total(100,2,0.3,0.5)


# calling by name and order doesn't matter 
# when you calling by name
get_total(tax=0.3,price=100,discount=0.5,qty=2)