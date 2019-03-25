import matplotlib.pyplot as plt
import math


# def generate_x():
#     i = -5
#     while i <= 5:
#         yield i
#         i += 0.1

# x = list(generate_x())

x = [i for i in range(1, 11)]
y = []

for i in range(1, 11):
    y.append(float(input(f'Unesite vrednost za {i} dan:')))


plt.scatter(x, y, c='blue', s=50, marker='x')
plt.plot(x, y, color='red', linewidth=1)

plt.xlabel('X data')
plt.ylabel('Y data')
plt.title('Example plot of sin function')

plt.show()
