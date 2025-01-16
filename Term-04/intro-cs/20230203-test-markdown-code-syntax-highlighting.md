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
Traveling salesman
```
IDENTIFICATION DIVISION.
PROGRAM-ID. TRAVELING-SALESMAN.
DATA DIVISION.
WORKING-STORAGE SECTION.
01  DISTANCES PIC 9(4) OCCURS 10 TIMES INDEXED BY I.
01  CITIES PIC 9(2) OCCURS 10 TIMES.
01  TOUR PIC 9(2) OCCURS 10 TIMES.
01  CITY-COUNT PIC 9(2) VALUE 10.
01  MIN-DISTANCE PIC 9(4).
01  MIN-CITY PIC 9(2).
01  TOTAL-DISTANCE PIC 9(8) VALUE 0.
01  I PIC 9(2).
01  J PIC 9(2).
01  K PIC 9(2).
PROCEDURE DIVISION.
BEGIN.
    PERFORM INITIALIZE-DATA.
    PERFORM NEAREST-NEIGHBOR.
    PERFORM CALCULATE-TOTAL-DISTANCE.
    DISPLAY "Tour: ".
    PERFORM DISPLAY-TOUR.
    DISPLAY "Total Distance: " TOTAL-DISTANCE.
    STOP RUN.
INITIALIZE-DATA.
    MOVE 0 TO I.
    PERFORM VARYING J FROM 1 BY 1 UNTIL J > CITY-COUNT
        MOVE J TO CITIES(J)
        PERFORM VARYING K FROM 1 BY 1 UNTIL K > CITY-COUNT
            IF J = K
                MOVE 0 TO DISTANCES(J,K)
            ELSE
                COMPUTE DISTANCES(J,K) = FUNCTION RANDOM(100) + 1
            END-IF
        END-PERFORM
    END-PERFORM.
    MOVE 1 TO TOUR(1)
    MOVE 1 TO I
    PERFORM VARYING J FROM 2 BY 1 UNTIL J > CITY-COUNT
        MOVE 0 TO MIN-DISTANCE
        PERFORM VARYING K FROM 1 BY 1 UNTIL K <= CITY-COUNT
            IF K NOT = TOUR(J-1)
                IF MIN-DISTANCE = 0 OR DISTANCES(TOUR(J-1),K) < MIN-DISTANCE
                    MOVE DISTANCES(TOUR(J-1),K) TO MIN-DISTANCE
                    MOVE K TO MIN-CITY
                END-IF
            END-IF
        END-PERFORM
        MOVE MIN-CITY TO TOUR(J)
    END-PERFORM.
NEAREST-NEIGHBOR.
    MOVE 1 TO I
    PERFORM VARYING J FROM 2 BY 1 UNTIL J <= CITY-COUNT
        MOVE 0 TO MIN-DISTANCE
        PERFORM VARYING K FROM J TO CITY-COUNT
            IF K NOT = TOUR(J)
                IF MIN-DISTANCE = 0 OR DISTANCES(TOUR(J),K) < MIN-DISTANCE
                    MOVE DISTANCES(TOUR(J),K) TO MIN-DISTANCE
                    MOVE K TO MIN-CITY
                END-IF
            END-IF
        END-PERFORM
        IF MIN-CITY NOT = 0
            MOVE MIN-CITY TO TOUR(J)
        END-IF
    END-PERFORM.
CALCULATE-TOTAL-DISTANCE.
    MOVE 0 TO TOTAL-DISTANCE
    PERFORM VARYING I FROM 1 BY 1 UNTIL I = CITY-COUNT
        COMPUTE TOTAL-DISTANCE = TOTAL-DISTANCE + DISTANCES(TOUR

```

``` cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. TRAVELING-SALESMAN.
DATA DIVISION.
WORKING-STORAGE SECTION.
01  DISTANCES PIC 9(4) OCCURS 10 TIMES INDEXED BY I.
01  CITIES PIC 9(2) OCCURS 10 TIMES.
01  TOUR PIC 9(2) OCCURS 10 TIMES.
01  CITY-COUNT PIC 9(2) VALUE 10.
01  MIN-DISTANCE PIC 9(4).
01  MIN-CITY PIC 9(2).
01  TOTAL-DISTANCE PIC 9(8) VALUE 0.
01  I PIC 9(2).
01  J PIC 9(2).
01  K PIC 9(2).
PROCEDURE DIVISION.
BEGIN.
    PERFORM INITIALIZE-DATA.
    PERFORM NEAREST-NEIGHBOR.
    PERFORM CALCULATE-TOTAL-DISTANCE.
    DISPLAY "Tour: ".
    PERFORM DISPLAY-TOUR.
    DISPLAY "Total Distance: " TOTAL-DISTANCE.
    STOP RUN.
INITIALIZE-DATA.
    MOVE 0 TO I.
    PERFORM VARYING J FROM 1 BY 1 UNTIL J > CITY-COUNT
        MOVE J TO CITIES(J)
        PERFORM VARYING K FROM 1 BY 1 UNTIL K > CITY-COUNT
            IF J = K
                MOVE 0 TO DISTANCES(J,K)
            ELSE
                COMPUTE DISTANCES(J,K) = FUNCTION RANDOM(100) + 1
            END-IF
        END-PERFORM
    END-PERFORM.
    MOVE 1 TO TOUR(1)
    MOVE 1 TO I
    PERFORM VARYING J FROM 2 BY 1 UNTIL J > CITY-COUNT
        MOVE 0 TO MIN-DISTANCE
        PERFORM VARYING K FROM 1 BY 1 UNTIL K <= CITY-COUNT
            IF K NOT = TOUR(J-1)
                IF MIN-DISTANCE = 0 OR DISTANCES(TOUR(J-1),K) < MIN-DISTANCE
                    MOVE DISTANCES(TOUR(J-1),K) TO MIN-DISTANCE
                    MOVE K TO MIN-CITY
                END-IF
            END-IF
        END-PERFORM
        MOVE MIN-CITY TO TOUR(J)
    END-PERFORM.
NEAREST-NEIGHBOR.
    MOVE 1 TO I
    PERFORM VARYING J FROM 2 BY 1 UNTIL J <= CITY-COUNT
        MOVE 0 TO MIN-DISTANCE
        PERFORM VARYING K FROM J TO CITY-COUNT
            IF K NOT = TOUR(J)
                IF MIN-DISTANCE = 0 OR DISTANCES(TOUR(J),K) < MIN-DISTANCE
                    MOVE DISTANCES(TOUR(J),K) TO MIN-DISTANCE
                    MOVE K TO MIN-CITY
                END-IF
            END-IF
        END-PERFORM
        IF MIN-CITY NOT = 0
            MOVE MIN-CITY TO TOUR(J)
        END-IF
    END-PERFORM.
CALCULATE-TOTAL-DISTANCE.
    MOVE 0 TO TOTAL-DISTANCE
    PERFORM VARYING I FROM 1 BY 1 UNTIL I = CITY-COUNT
        COMPUTE TOTAL-DISTANCE = TOTAL-DISTANCE + DISTANCES(TOUR

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
