# This is to test Markdown's capability for syntax highlighting for code snippets.
## Python
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

## HTML
```
<!DOCTYPE html>
<html>
<body>

<h1>Heading</h1>

<p>Here is a paragraph</p>

<h2>Here is an unordered list in order</h2>
<ul>
	<li>Item0</li>
    <li>Item1</li>
    <li>Item2</li>
    <li>Item3</li>
</ul>

</body>
</html>
```

``` html
<!DOCTYPE html>
<html>
<body>

<h1>Heading</h1>

<p>Here is a paragraph</p>

<h2>Here is an unordered list in order</h2>
<ul>
	<li>Item0</li>
    <li>Item1</li>
    <li>Item2</li>
    <li>Item3</li>
</ul>

</body>
</html>
```

## JavaScript

```
var xhr = new XMLHttpRequest();
xhr.open("GET", "https://example.com", true);
xhr.onreadystatechange = function() {
  if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
    console.log(xhr.responseText);
  }
};
xhr.send();
```

``` javascript
var xhr = new XMLHttpRequest();
xhr.open("GET", "https://example.com", true);
xhr.onreadystatechange = function() {
  if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
    console.log(xhr.responseText);
  }
};
xhr.send();
```
