from ecommerce_utils import generate_invoice

cart = {
    "Laptop": 55000,
    "Phone": 30000,
    "Headphones": 2000
}

generate_invoice(cart, 10, 18)