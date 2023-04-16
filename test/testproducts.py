price_dozen = float(input("Enter the price of each dozen: "))

quantity_dozen = int(input("Enter the quantity of dozens of a product to purchase: "))

purchase_amount = price_dozen * quantity_dozen

if quantity_dozen > 3:
    discount_amount = purchase_amount * 0.15
    amount_to_pay = purchase_amount - discount_amount
    gift_units = quantity_dozen
else:
    discount_amount = purchase_amount * 0.1
    amount_to_pay = purchase_amount - discount_amount
    gift_units = 0

print(f"Initial purchase amount: ${purchase_amount:.2f}")
print(f"Discount amount: ${discount_amount:.2f}")
print(f"Amount to pay with discount: ${amount_to_pay:.2f}")
print(f"Gift units: {gift_units}")