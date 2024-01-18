characters = ['a', 'B', 'c', 'D']

c = ['uppercase' if j.isupper() else 'lowercase' for j in characters]

print(c)