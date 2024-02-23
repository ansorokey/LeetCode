## Declaring Variables:
```py
a = 7
a = 8
b = "Reyes"
x = y = z = 0
i, j = 0, 0
```

## Special Variables
```py
# infinity
posInf = float('inf')
negInf = float('-inf')
```

## Printing:
```py
print(a, b, c)
```

## Iteration:
```py
# Ranges
for i in range(x):
    pass

for i in range(len(a)):
    pass

for i in range(start, stop, step):
    pass

# Items
for c in string:
    pass

for (x, y) in enum(iterable):
    pass
```

## Conditionals
```py
if a or b:
    pass

if a and b:
    pass

if not a:
    pass
```

## Strings
```py
# Split string on every char
a = [*string]

# Split string on specific char
b = string.split('x')
```

## Arrays(Lists)
```py
a = []

# of n length
b = [val] * n

# concatenation
c = [1] + [2] + [3]

# length
len(l)

# convert to a list
list(iterableObject)

# add to list
arr.append(x)

# remove from a list
arr.pop(optional_index)
```

## Comprehension
```py
a = [i for i in range(5)] # [1, 2, 3, 4, 5]

b = [x for x in numList if x % 2 == 0]

c = ['uppercase' if j.isUpper() else 'lowercase' for j in characters]
```

## Sets
```py
# Make a hashMap
newSet = {}

# Make a set
newSet = set()

# Add to a set
newSet.add(x)

# Remove from a set
newSet.remove(x)
```