numbers = range(10)
# prices = []
# for number in numbers:
#     if number % 2==0:
#         prices.append(number)
#
# print(prices)

# prices = list(filter(lambda number:number %2==0,numbers))
# print(prices)

prices = [number for number in numbers if number % 2 == 0]
print(prices)