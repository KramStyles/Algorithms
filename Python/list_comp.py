"""Shoprite supermarket has an existing way of calculating the amount of items purchased by 
their customer, but all of a sudden the Nigeria government created a new policy that the (VAT)
 value added tax of 7.5 should be added on all the items. As a developer, 
 Shoprite supermarket asked for your help to automate their existing machine to be add
  VAT to all the items bought.
Lastly the price of item that is <= #50, VAT should be exempted i.e
 VAT should not be charged on that item.
Solve this problem using list comprehensions."""

def shop_with_vat(priceLst):
    pass

prices = [12, 34, 5545, 223, 2233, 221, 484, 84884, 829]
emp = []
for x in prices:
    if x > 50:
        emp.append(round((7.5/100)*x + x))
    else:
        emp.append(x)


emp2 = [item_price if item_price < 50 else round((7.5/100) * item_price + item_price) for item_price in prices]
