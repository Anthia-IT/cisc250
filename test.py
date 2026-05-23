# Student Name:Anthia Gardner-Celestine
# Lab Title: Invoice Creator
# Date: 5/22/2026
# =============================================================================

# TASK 1: Nesting - Create a dictionary of dictionaries of the products being 
# purchased.

# table.
product_list = {
    "el2234" : { 
        "name" : "Head Phones", 
        "category" : "Electronics", 
        "price" : 19.99, 
        "quantity" : 2 
        },
    "sh9989" : {
        "name" : "Running Shoes",
        "category" : "Footwear",
        "price" : 99.99,
        "quantity": 1
    },
    "ap0098" : {
        "name" : "Smart Toaster",
        "category" : "Appliance",
        "price" : 130.00,
        "quantity" : 1

    },
    "cl3321" : {
        "name" : "Cotton Shirt",
        "category" : "Clothing",
        "price" : 10.00,
        "quantity" : 4
    },
    }


# Task 2.1: Create a dictionary to hold the customer data

customer_data = {
    "name" : "Hannah Davis",
    "Loyalty Tier" : "Gold"
}


# Task 2.2: Print a processing order statement using an f string

print(f"Processing order for {customer_data ['name']} [{customer_data['Loyalty Tier']} Tier member]...")


# Task 3: Loop through dictionary with match-case discount calculations

total = 0
for product_id, product_info in product_list.items():
    name = product_info["name"]
    category = product_info["category"]
    price = product_info["price"]
    quantity = product_info["quantity"]

    subtotal = price * quantity

    match category:
        case "Appliance" :
            discount_rate = 0.20
        case "Clothing" :
            discount_rate = 0.10
        case _:
            discount_rate = 0

    sales_discount = subtotal * discount_rate
    final_price = subtotal - sales_discount

    print(f"\nProduct: {name}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Discount: ${sales_discount:.2f}")
    print(f"Final Product Price: ${final_price:.2f}")

    total = total + final_price
          
# Task 4: Subtotals, membership discounts, and final invoice total
tier = customer_data["Loyalty Tier"]

if tier == "Platinum":
    member_discount_rate = 0.16

elif tier == "Gold":
    member_discount_rate = 0.11

elif tier == "Silver":
    member_discount_rate = 0.05

else:
    member_discount_rate = 0

member_discount = total * member_discount_rate

final_total = total - member_discount

print("\n----------------------")
print(f"Total After Discounts: ${total:.2f}")
print(f"Membership Discount: ${member_discount:.2f}")
print(f"Final Total Owed: ${final_total:.2f}")

