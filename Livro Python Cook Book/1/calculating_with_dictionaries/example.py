# example.py
#
# Example of calculating with dictionaries

prices = {'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75 }


# Find min and max price
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))



print('Preço Mínimo:', min_price)
print('Preço Máximo:', max_price)

print('\n')


print('Preços Ordenados:')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
    print('    ', name, price)


