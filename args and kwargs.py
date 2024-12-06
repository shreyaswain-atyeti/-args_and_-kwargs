def shopping_cart(*args, **kwargs):
    discount = kwargs.get('discount', 0)  
    delivery_charge = kwargs.get('delivery_charge', 50)
    promo_code = kwargs.get('promo_code', None)
    promo_code_deductions = {"SAVE10": 10, "SAVE20": 20}
    items_details = []
    subtotal = 0
    for item in args:
        name, price, quantity = item
        item_total = price * quantity
        subtotal += item_total
        items_details.append(f"  {name}: ${price} x {quantity} = ${item_total}")

    discount_amount = subtotal * (discount / 100)
    promo_code_discount = promo_code_deductions.get(promo_code, 0)
    if subtotal > 500:
        delivery_charge = 0
    total = subtotal - discount_amount - promo_code_discount + delivery_charge
    bill = "Detailed Bill:\nItems:\n"
    bill += "\n".join(items_details)
    bill += f"\nSubtotal: ${subtotal:.2f}"
    bill += f"\nDiscount ({discount}%): -${discount_amount:.2f}"
    if promo_code:
        bill += f"\nPromo Code ('{promo_code}'): -${promo_code_discount}"
    bill += f"\n{'Free Delivery' if delivery_charge == 0 else f'Delivery Charge: ${delivery_charge:.2f}'}"
    bill += f"\nTotal: ${total:.2f}"
    
    return bill

example_bill_1 = shopping_cart(
    ("Laptop", 1000, 1), 
    ("Mouse", 20, 2), 
    ("Keyboard", 50, 1),
    discount=10, 
    promo_code="SAVE10"
)
example_bill_2 = shopping_cart(
    ("Headphones", 100, 1), 
    ("Phone Case", 20, 2),
    discount=5
)
print("Customer 1:\n", example_bill_1)
print("\nCustomer 2:\n", example_bill_2)
