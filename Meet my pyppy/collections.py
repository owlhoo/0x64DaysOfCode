from collections import Counter, namedtuple, deque


# SPHINX is a tool that generates html based docs for py projects based on docstrings i.e.   """ docstring """

def hello():
    """ Function that prints hello world """
    print('Hello, world!')


print('The documentation: ' + str(hello.__doc__))

# counter

counts = Counter('hello world')

print(counts)
print('Character l appeared ' + str(counts['l']) + ' times.')

for pair in counts:
    print('Character "' + str(pair) + '" appeared ' + str(counts[pair]) + ' time(s).')

# named tuples

Person = namedtuple('Person', 'age, height, name')

john = Person(10, 105, 'John')
josh = Person(height=105, age=10, name='Josh')
print(john, josh)
for attribute in john:
    print(attribute, end=' ')
print()

# deque

deck = deque('argument')
for val, index in enumerate(deck):
    print(str(val) + ' ' + str(index))


deck.extend(' is invalid.')
print(deck)

deck.appendleft('Your ')
print(''.join(deck))

deck.rotate(5)
print(''.join(deck))

help(hello)
