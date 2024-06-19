def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))


final_price = calculate_discount(original_price, discount_percent)
100
if final_price == original_price:
    print(f"No discount applied. Final price: ${final_price:.2f}")
else:
    print(f"Discount applied. Final price after {discount_percent}% discount: ${final_price:.2f}")
