# This is to test Markdown's capability for syntax highlighting for code snippets.

```
print("Text")

num = int(input())  # This is the number of Fibonacci digits the user wants to be generated.

sequence = [0, 1, 1]  # This is to get the sequence started.
num -= 3  # This is to correct for the initial sequence specified in the above line. 

def fibonacci(n):
    n1 = sequence[-2]
    n2 = sequence[-1]
    sequence.append(n1+n2)

    n -= 1
    if n > 0:
        fibonacci(n)
		
fibonacci(num)

for number in sequence:
    print(number)
```

``` python
print("Text")

num = int(input())  # This is the number of Fibonacci digits the user wants to be generated.

sequence = [0, 1, 1]  # This is to get the sequence started.
num -= 3  # This is to correct for the initial sequence specified in the above line. 

def fibonacci(n):
    n1 = sequence[-2]
    n2 = sequence[-1]
    sequence.append(n1+n2)

    n -= 1
    if n > 0:
        fibonacci(n)
		
fibonacci(num)

for number in sequence:
    print(number)
```
