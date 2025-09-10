def apply_dicount(price: int, discount_percent: int) -> int:
    return price - ( price * ( discount_percent / 100 ) )

def add_gst(price: int, gst_percent: int = 18) -> int:
    return price + (price * ( gst_percent / 100 ))

def generate_invoice(cart: dict, discount_percent: int = 0, gst_percent: int = 18):
    print("-----------------------Invoice-------------------------")
    subtotal: int = 0
    for item, price in cart.items():
        print(f"{item}: ₹{price}")
        subtotal += price
    
    print("--------------------------------")
    print(f"Subtotal: ₹{subtotal}")
    discounted_price = apply_dicount(subtotal, discount_percent)
    print(f"After 10% /discount: ₹{discounted_price}")
    print(f"After 18% GST: ₹{add_gst(discounted_price, gst_percent)}")
    print("--------------------------------")
    
    print("Thank you for shopping with us")