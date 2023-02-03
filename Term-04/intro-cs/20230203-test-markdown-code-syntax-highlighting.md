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
