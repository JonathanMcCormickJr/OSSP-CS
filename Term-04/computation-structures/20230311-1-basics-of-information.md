# 1 Basics of Information

Notes by Jonathan McCormick, Jr. 2023-03-11.

## 1.2.1What is Information?

What is "Information"? Data communicated or recieved that resolves the
most uncertainty about a particular fact or circumstance. 

Ex: in a standard card deck, "the card is a face card" is more 
informative than "the card is NOT the ace of spades". 


We will be working to use machines to work with information, and 
find ways to debug errors. 

## 1.2.2Quantifying Information

Claude Shannon, 1942 
![image](https://user-images.githubusercontent.com/67705789/224510286-38b81304-caa1-43e9-8f5a-bc9c40693280.png)

## 1.2.3Entropy

In information theory, the **entropy** H(X) is the average amount of 
information cointained in each piece of data received about the value of X.

The entropy H(X) is a LOWER BOUND on the number of bits we need to transmit in order to convey a given piece of information. 

### Worksheet problems 1: Information Content and Entropy

**A. You are given an unknown 3-bit binary number. You are then told that the binary
representation contains exactly two 1’s. How much information have you been given?**

While I might be tempted to hastily say "two bits", the reality is that I have not really been given that much info. So, let's use the formula `log2(1/p)`. 

First, we need to calculate `p`, which is the probability.

In a 3-bit number, out of all possible values, how much does the statement "2 bits are each `1`" actually narrow things down.

``` python
import math

x1 = 0b000
x2 = 0b001
x3 = 0b010
x4 = 0b011
x5 = 0b100
x6 = 0b101
x7 = 0b110
x8 = 0b111

# So...
n_of_x = 8

# Now, if we know that exactly 2 of the bits are 1's, that narrows us down to...
x4 = 0b011
x6 = 0b101
x7 = 0b110

m_of_x = 3

p = m_of_x / n_of_x

print(math.log2(1/p))  # = log2(8/3) bits or 1.4150374992788437

```

So, the amount of information you have been given is `log2(8/3)` bits or `1.4150374992788437` bits


**B. You are then given the additional information that the number is also odd. How much
additional information have you been given?**

``` python
import math

x4 = 0b011
x6 = 0b101
x7 = 0b110

n_of_x = 3

# If we have ADDITIONAL info that the num is also ODD...

x4 = 0b011
x6 = 0b101

m_of_x = 2

p = n_of_x / m_of_x

print(math.log2(p))  # log2(3/2) = 0.5849625007211562
```

So, we get `0.5849625007211562` bits of additional info. 


**C. A random variable X represents the outcome of flipping an unfair coin, where p(HEADS)
= 0.6. Please give the value for the entropy H(X). You may express your answer as a
numeric expression (i.e., you don’t have to actually do the arithmetic).**

`H(X) = (p1 * log2(1/p1)) + (p2 * log2(1/p2)) + ...`

Therefore, with 2 choices here is our table:
| choice | p | log2(1/p) |
|-|-|-|
| heads | 0.6 | 0.73696559... |
| tails | 0.4 | 1.321928... |

So, the average of these is `(0.6 * 0.73696559...) + (0.4 + 1.321928...)`, which equals about `0.9709505945`.


**D. A single decimal digit is chosen at random and you’re told that its value is 0 mod 3. How
much information have you learned about the digit?** 
**E. X is an unknown 8-bit binary number. You are given another 8-bit binary number,
10101100, and told that the Hamming distance between X and 10101100 is one. How
many bits of information about X have you been given? You can give a formula if you
wish.**
F. We wish to transmit messages comprised of the four symbols shown below with their
associated probabilities and 5-bit fixed-length encoding.

|Symbol | p(symbol) | encoding |
|---|-----|--------|
| α | 0.5 | 00000 |
| β | 0.125 | 11100 |
| γ | 0.25 | 11011 |
| δ | 0.125 | 10111 |

An unknown symbol is received and you are told it’s not δ. How much information have
you received?

G. When transmitting a message comprised of these four symbols with the probabilities as
given above, what is the expected amount information received when you are told the
next symbol in the message?
H. You are given an unknown 5-bit binary number. You are then told that the first and last
bits are the same. How much information have you been given?
I. I’ve randomly selected a letter from the alphabet and tell you that my selection is neither
“X”, “Y”, nor “Z”. How much information have I given you about my letter?
J. I make up a random 4-bit two’s complement number by flipping a fair coin to determine
each bit. You’re trying to guess the number. If I tell you that the number is positive (>
0), how many bits of information have I given you? Be precise; you may answer by a
formula or a number. 

## 1.2.4Encoding
## 1.2.5Fixed-length Encodings
## 1.2.6Signed Integers: 2’s complement
## 1.2.7Variable-length Encoding
## 1.2.8Huffman’s Algorithm
## 1.2.9Huffman Code
## 1.2.10Error Detection and Correction
## 1.2.11Error Correction
## 1.2.12Worked Examples
## » Entropy
