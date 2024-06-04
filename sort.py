items = [
    ("product1",10),
    ("product2",8),
    ("product3",12),
]
# print(items)

# def sort_items(item):
#     return item[1]

# items.sort(key=lambda item:item[1])
# # print(items)

# prices = []
# for item in items:
#     prices.append(item[1])

# prices = list(map(lambda item:item[1],items))
# print(prices)
prices =list(filter(lambda item:item[1]>=10,items))
print(prices)