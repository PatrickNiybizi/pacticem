numbers = [1,1,2,3,4,4,5]
first = set(numbers)
print(first)
second = {1,5}
second.add(5)
second.remove(5)

print(first | second)
print(first & second)
print(first - second)