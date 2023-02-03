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

## COBOL

```
IDENTIFICATION DIVISION.
PROGRAM-ID. HELLO-WORLD.
PROCEDURE DIVISION.
    DISPLAY "Hello, World!".
    STOP RUN.
```

``` cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. HELLO-WORLD.
PROCEDURE DIVISION.
    DISPLAY "Hello, World!".
    STOP RUN.
```

## Binary
```
01001000 01100101 01101100 01101100 01101111 00101100 00101111 00101111 00101110 00101100 01100100 00100001
```
``` binary
01001000 01100101 01101100 01101100 01101111 00101100 00101111 00101111 00101110 00101100 01100100 00100001
```
So...it looks like Binary is not supported. 
![image](https://user-images.githubusercontent.com/67705789/216690975-efbd9f8d-44ec-4b65-aab1-282a61ff3f55.png)


## Assembly
```
.data
number db 0
result db 0
.code
main proc
    mov edx, 0   ; initialize edx register
    mov ecx, 0   ; initialize ecx register
    mov eax, 10  ; read number into eax register
    mov ebx, 0   ; initialize ebx register
    int 0x80     ; system call to read number from user
    mov [number], al ; save number entered by user
    mov eax, [number] ; load number into eax register
    dec eax      ; decrease number by 1
    mov [result], al ; store result in result
    mov ebx, 1   ; initialize ebx to 1
    loop:
        cmp eax, 0 ; compare eax to 0
        je endloop ; jump to endloop if equal
        mul ebx     ; multiply ebx by eax
        dec eax     ; decrease eax by 1
        jmp loop    ; jump to loop
    endloop:
        mov [result], bl ; store result in result
        mov eax, 4   ; specify system call number (sys_write)
        mov ebx, 1   ; specify file descriptor (stdout)
        mov ecx, result ; specify address of message to write
        mov edx, 1   ; specify length of message
        int 0x80     ; initiate system call
    mov eax, 1    ; specify system call number (sys_exit)
    xor ebx, ebx  ; exit status
    int 0x80      ; initiate system call
main endp
end main
```

``` assembly
.data
number db 0
result db 0
.code
main proc
    mov edx, 0   ; initialize edx register
    mov ecx, 0   ; initialize ecx register
    mov eax, 10  ; read number into eax register
    mov ebx, 0   ; initialize ebx register
    int 0x80     ; system call to read number from user
    mov [number], al ; save number entered by user
    mov eax, [number] ; load number into eax register
    dec eax      ; decrease number by 1
    mov [result], al ; store result in result
    mov ebx, 1   ; initialize ebx to 1
    loop:
        cmp eax, 0 ; compare eax to 0
        je endloop ; jump to endloop if equal
        mul ebx     ; multiply ebx by eax
        dec eax     ; decrease eax by 1
        jmp loop    ; jump to loop
    endloop:
        mov [result], bl ; store result in result
        mov eax, 4   ; specify system call number (sys_write)
        mov ebx, 1   ; specify file descriptor (stdout)
        mov ecx, result ; specify address of message to write
        mov edx, 1   ; specify length of message
        int 0x80     ; initiate system call
    mov eax, 1    ; specify system call number (sys_exit)
    xor ebx, ebx  ; exit status
    int 0x80      ; initiate system call
main endp
end main
```

## Golang

Traveling Salesman

```
package main

import (
	"fmt"
	"math"
)

type Point struct {
	x float64
	y float64
}

func distance(a, b Point) float64 {
	dx := a.x - b.x
	dy := a.y - b.y
	return math.Sqrt(dx*dx + dy*dy)
}

func main() {
	points := []Point{
		{100.42, -2482.0},
		{248.3, 305.2},
		{-1894.0, 3.0},
		{-1.0, 5.0},
		{1000.0, -20.0},
	}

	n := len(points)
	visited := make([]bool, n)
	path := make([]int, n)

	path[0] = 0
	visited[0] = true
	for i := 1; i < n; i++ {
		best := -1
		for j := 0; j < n; j++ {
			if visited[j] {
				continue
			}
			if best == -1 || distance(points[path[i-1]], points[j]) < distance(points[path[i-1]], points[best]) {
				best = j
			}
		}
		path[i] = best
		visited[best] = true
	}

	letters := []string{"A", "B", "C", "D", "E"}
	for _, index := range path {
		fmt.Print(letters[index], " -> ")
	}
	fmt.Println(letters[0])
}
```
``` go
package main

import (
	"fmt"
	"math"
)

type Point struct {
	x float64
	y float64
}

func distance(a, b Point) float64 {
	dx := a.x - b.x
	dy := a.y - b.y
	return math.Sqrt(dx*dx + dy*dy)
}

func main() {
	points := []Point{
		{100.42, -2482.0},
		{248.3, 305.2},
		{-1894.0, 3.0},
		{-1.0, 5.0},
		{1000.0, -20.0},
	}

	n := len(points)
	visited := make([]bool, n)
	path := make([]int, n)

	path[0] = 0
	visited[0] = true
	for i := 1; i < n; i++ {
		best := -1
		for j := 0; j < n; j++ {
			if visited[j] {
				continue
			}
			if best == -1 || distance(points[path[i-1]], points[j]) < distance(points[path[i-1]], points[best]) {
				best = j
			}
		}
		path[i] = best
		visited[best] = true
	}

	letters := []string{"A", "B", "C", "D", "E"}
	for _, index := range path {
		fmt.Print(letters[index], " -> ")
	}
	fmt.Println(letters[0])
}
```

## BASH

```
#!/bin/bash

# number of cities
n=10

# generate random coordinates for cities
for i in $(seq 1 $n)
do
  x=$((RANDOM % 100))
  y=$((RANDOM % 100))
  echo $x $y
done > cities.txt

# calculate distances between cities
for i in $(seq 1 $n)
do
  for j in $(seq $i $n)
  do
    if [ $i -ne $j ]
    then
      x1=$(awk 'NR=='$i' {print $1}' cities.txt)
      y1=$(awk 'NR=='$i' {print $2}' cities.txt)
      x2=$(awk 'NR=='$j' {print $1}' cities.txt)
      y2=$(awk 'NR=='$j' {print $2}' cities.txt)
      d=$(echo "sqrt(($x2-$x1)^2+($y2-$y1)^2)" | bc -l)
      echo $i $j $d
    fi
  done
done > distances.txt

# generate random solution
solution=$(for i in $(seq 1 $n)
do
  echo $i
done | shuf | tr '\n' ' ')

# calculate total distance of solution
total_distance=0
for i in $(seq 1 $(($n-1)))
do
  j=$(($i+1))
  c1=$(echo $solution | awk '{print $'$i'}')
  c2=$(echo $solution | awk '{print $'$j'}')
  distance=$(awk '$1=='$c1' && $2=='$c2' {print $3}' distances.txt)
  total_distance=$(echo "$total_distance + $distance" | bc -l)
done

# add distance from last to first city
c1=$(echo $solution | awk '{print $'$n'}')
c2=$(echo $solution | awk '{print $1}')
distance=$(awk '$1=='$c1' && $2=='$c2' {print $3}' distances.txt)
total_distance=$(echo "$total_distance + $distance" | bc -l)

# print solution and total distance
echo "Solution: $solution"
echo "Total distance: $total_distance"
```
``` bash
#!/bin/bash

# number of cities
n=10

# generate random coordinates for cities
for i in $(seq 1 $n)
do
  x=$((RANDOM % 100))
  y=$((RANDOM % 100))
  echo $x $y
done > cities.txt

# calculate distances between cities
for i in $(seq 1 $n)
do
  for j in $(seq $i $n)
  do
    if [ $i -ne $j ]
    then
      x1=$(awk 'NR=='$i' {print $1}' cities.txt)
      y1=$(awk 'NR=='$i' {print $2}' cities.txt)
      x2=$(awk 'NR=='$j' {print $1}' cities.txt)
      y2=$(awk 'NR=='$j' {print $2}' cities.txt)
      d=$(echo "sqrt(($x2-$x1)^2+($y2-$y1)^2)" | bc -l)
      echo $i $j $d
    fi
  done
done > distances.txt

# generate random solution
solution=$(for i in $(seq 1 $n)
do
  echo $i
done | shuf | tr '\n' ' ')

# calculate total distance of solution
total_distance=0
for i in $(seq 1 $(($n-1)))
do
  j=$(($i+1))
  c1=$(echo $solution | awk '{print $'$i'}')
  c2=$(echo $solution | awk '{print $'$j'}')
  distance=$(awk '$1=='$c1' && $2=='$c2' {print $3}' distances.txt)
  total_distance=$(echo "$total_distance + $distance" | bc -l)
done

# add distance from last to first city
c1=$(echo $solution | awk '{print $'$n'}')
c2=$(echo $solution | awk '{print $1}')
distance=$(awk '$1=='$c1' && $2=='$c2' {print $3}' distances.txt)
total_distance=$(echo "$total_distance + $distance" | bc -l)

# print solution and total distance
echo "Solution: $solution"
echo "Total distance: $total_distance"
```
