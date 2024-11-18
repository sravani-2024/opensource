X = int(input())
price_with_10_percent_discount = X * 0.9
price_with_flat_discount = X - 100

final_price = min(price_with_10_percent_discount, price_with_flat_discount)

print(final_price)
