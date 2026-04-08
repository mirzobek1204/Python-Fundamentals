def calculate_item_total(quantity,unit_price):
    total_price=quantity*unit_price
    return total_price
def apply_bulk_discount(total,quantity):
    if quantity>=10:
        total=total*0.1
        return total
    elif quantity>=5:
        total=total*0.05
        return total   
    else:
        return 0.0 
def calculate_tax(subtotal,tax_rate):
    tax_amount=subtotal*tax_rate
    return tax_amount
def is_eligible_for_free_shipping(subtotal):
    return subtotal>=50
print("SHOPPING CART CALCULATOR")
print("============================================") 
def process_order(item_name, quantity, unit_price, tax_rate):

    print(f"Order Receipt for :{item_name}")
    print(f"  Quantity:{quantity} @ ${unit_price:.2f} each")
    item_total=calculate_item_total(quantity,unit_price)
    print(f"  Item total:${item_total:.2f}")
    discount=apply_bulk_discount(item_total, quantity)
    print(f"  Bulk discount:$-{discount:.2f}")
    subtotal=item_total-discount
    print(f"  Subtotal:${subtotal:.2f}")
    tax_amount=subtotal*tax_rate/100
    print(f"  Tax(8%):${tax_amount:.2f}")
    Final=subtotal+tax_amount
    print(f"  Final Total:${Final:.2f}")
    if subtotal>=50:
        print("Free shipping")
    else:
        result=50-subtotal
        print(f"  Need ${result:.2f} more for free shipping")
        print("-"*38)
process_order("Notebooks",12, 3.50, 8)
process_order("Pens",6 ,1.25,8)
process_order("Paper",3 ,4.99,8)  
