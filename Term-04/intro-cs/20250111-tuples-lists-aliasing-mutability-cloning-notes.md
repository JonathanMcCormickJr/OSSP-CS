# Lecture 5: Tuples, Lists, Aliasing, Mutability, and Cloning



## Tuples

A tuple is a sequence of values. 

Tuples are immutable. 

```python 

my_tuple = (1, 2, 3, 4, 5)

empty_tuple = ()

```

In Python, a tuple may contain a mix of different types of values. 

```python

my_tuple = (1, 2, 3, 4, 5, 'a', 'b', 'c')

```

Using a particular index, we can access the value of a tuple. 

```python

my_tuple = (1, 2, 3, 4, 5, 'a', 'b', 'c')

print(my_tuple[0]) # 1

print(my_tuple[1]) # 2

print(my_tuple[2]) # 3

```

We can also slice a tuple. 

```python

my_tuple = (1, 2, 3, 4, 5, 'a', 'b', 'c')

print(my_tuple[0:3]) # (1, 2, 3)

```

A single value tuple must have a comma after the value. 

```python

my_tuple = (1,)

```

We can use tuples to return multiple values from a function. 

```python

def get_data():

    return (1, 2, 3)

data = get_data()

print(data) # (1, 2, 3)

```

## Lists

Much like tuples, lists are sequences of values. They are mutable. 

```python

my_list = [1, 2, 3, 4, 5]

empty_list = []

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

list_of_mixed_types = [1, 'a', 2, 'b', 3, 'c']

super_complicated_list = [1, [2, 3], [4, [5, 6, [7, 8, 9]]]]

```

Obviously, you are not allowed to index a list with a value outside of the range of the list. 

```python

my_list = [1, 2, 3, 4, 5]

print(my_list[5]) # IndexError

```

You can change the value of a list at a particular index. 

```python

my_list = [1, 2, 3, 4, 5]

my_list[0] = 100

print(my_list) # [100, 2, 3, 4, 5]

```

You can also slice a list. 

```python

my_list = [1, 2, 3, 4, 5]

print(my_list[0:3]) # [1, 2, 3]

```

It is considered more "pythonic" to iterate directly over the values of a list. 

```python

my_list = [1, 2, 3, 4, 5]

for value in my_list:

    print(value)

```

Example of non-pythonic code: 

```python

my_list = [1, 2, 3, 4, 5]

for i in range(len(my_list)):

    print(my_list[i])

```

We can append values to a list. 

```python

my_list = [1, 2, 3, 4, 5]

my_list.append(6)

print(my_list) # [1, 2, 3, 4, 5, 6]

```

We can concatenate lists. 

```python

my_list = [1, 2, 3, 4, 5]

my_list = my_list + [6, 7, 8]

print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]

```

We can delete items from lists. 

```python

my_list = [1, 2, 3, 4, 5]

del my_list[0]

my_list.remove(4)  # removes the first instance of the value 4

print(my_list) # [2, 3, 5]

del my_list[-1] # removes the last item in the list

print(my_list) # [2, 3]

```

Converting between strings and lists. 

```python

my_string = 'hello'

my_list = list(my_string)

print(my_list) # ['h', 'e', 'l', 'l', 'o']

my_string = ''.join(my_list)

print(my_string) # hello

```

Splitting a string into a list. 

```python

my_string = 'hello world'

my_list = my_string.split()

print(my_list) # ['hello', 'world']

```

Sort vs Sorted. 

```python

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

sorted_list = sorted(my_list)  # returns a new list

print(sorted_list) # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

my_list.sort()  # sorts the list in place

print(my_list) # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

```

## Aliasing

When two variables refer to the same object, they are said to be aliases. 

```python

a = [1, 2, 3]

b = a

print(a is b) # True

```

Cloning a list. 

```python

a = [1, 2, 3]

b = a[:]

print(a is b) # False

print(a == b) # True

```




 
