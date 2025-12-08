#7.	Convert a list of prices into prices with 20% tax added using map().
list_of_prices = [1,2,3,4,5,6,7,8,9,10]
tax_20 = map(lambda x : x + x * 0.2, list_of_prices)
print(tuple(tax_20))