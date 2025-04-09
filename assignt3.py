def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Calculate discount amount
        discount_amount = price * (discount_percent / 100)
        # Return price after discount
        return price - discount_amount
    else:
        # Return original price if discount is less than 20%
        return price

# Get input from user
try:
    original_price = float(input("Enter the original price: "))
    discount = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount)
    
    # Print result
    if discount >= 20:
        print(f"Final price after {discount}% discount: ${final_price:.2f}")
    else:
        print(f"No discount applied (less than 20%). Original price: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numerical values")