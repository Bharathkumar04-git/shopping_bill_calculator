def calculate_total(price, quantity):
    return round(float(price) * int(quantity), 2)

def menu():
    print("\n--- Shopping Bill Calculator ---")
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))
        if price < 0 or quantity < 0:
            print("Price and quantity must be positive values.")
            return
        
        total = calculate_total(price, quantity)
        print(f"Total Bill: ${total}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    menu()
