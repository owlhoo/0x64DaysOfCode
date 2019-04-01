import copy

array = ['world!', 'Hello, ']
copied = array[:]                                          # shallow copy

print(f'I am copied list "{copied}"')
print(f'I am copied and reversed list "{copied[::-1]}"')

deep_copied = copy.deepcopy(array)                          # deep copy i.e. not only references
print(f'I am deep copied list "{deep_copied}"')
print(f'and now reversed too""{deep_copied[::-1]}')


another_array = ['he', ' world!']
another_array[0] = 'Hello, '
print(''.join(another_array))

