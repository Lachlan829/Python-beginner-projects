value1 = float(input("Please input the price of your item:\n"))
value2 = int(input("Please input the quantity of your item\n"))

unit_price = value1
quantity = value2
sales_tax_rate = .04
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax

s_subtotal = "$" + f"{subtotal:,.2f}"
s_sales_tax = "$" + f"{sales_tax:,.2f}"
s_total = "$" + f"{total:,.2f}"

output = f"""
Subtotal:   {s_subtotal:>9}
Sales Tax:  {s_sales_tax:>9}
Total:      {s_total:>9}
"""

print(output)
