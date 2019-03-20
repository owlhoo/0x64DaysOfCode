number = -1024

num2 = int('1111111111', 2)         # convert to int from base 2
print(bin(number))

number = number << 1
print(number)
print(bin(number))

number = ~number
print(number)
print(bin(number))
