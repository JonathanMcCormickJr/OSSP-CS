# Reading Notes

## TITLE: Computer Design and Architecture
by L. Howard Pollard
U of New Mexico

Book (c) 1990


## 1 Intro

Computers are used in basically every area of human life. 

Computer design is heavily reliant on electrical engineering  && computer science principles.

The power to drive a system must itself be carefully
1. transported
2. converted
3. isolated (from noise) and
4. delivered to the active devices in the system.

Functionality and reliability are super important, so it is critical that steps be taken to avoid noise from drowning out our signals.

Computers (at least classical computers) are limited in their capacity. When using computers for math, it is important to know whether or 
not the computer will be able to handle the entire math operation without introducing unacceptable errors. I have personally experienced this with some math programming operations in Python.

#### Aspects of Computer Engineering
1. Designing arithmetic elements in a system,
2. Creating system instructions,
3. Interconnction of specialized units to form the system,
4. Define and control data flow between different parts of the systems,
5. Techniques to communicate between computer and other devices (discs, tapes, terminals, etc.)

For this book, computer design issues will be address and tradeoffs will be evaluated. 

### 1.1 Early Computational Devices

Necessity is the mother of invention.

Computers were created to solve math problems. 

As techniques were explored, new ideas continued to emerge. 

The computers that we have are constantly being adapted and expanded to perform more tasks. 

#### Blaise Pascal's ~1642 mechanical counter

Could
* add
* subtract

Used a wheel for each digit and rotated wheels to add/subtract.

#### Gottfried Leibniz's 1671 mechanical calculating system

Could
* add 
* subtract
* multiplication
* division

Arguably the first 4-function calculator.

#### Jacquard Loom 1801

Weaving machine with patterns determined by punched cards

#### Charles Babbage's ~1823 Difference Engine

Could 
* generate math tables via addition

#### Babbage & Lovelace's never-fully-built Analytical Engine

* Very similar to modern computers
* Used punched cards

{Operation Cards}  {Variable Cards}

  went to ~~~~~~~~ went to 

{The Mill (ALU)} <-data-> {The Store (Memory)} --> {Printer & Card Punch}



#### 1890 US Census 

Herman Hollerith's card tabulating machine was used to process census data. 

1911 - Hollerith forms Tabulating Machine Company, which eventually joined forces with others
to form IBM.

Card systems have a hayday.

#### Konrad Zuse, late 1930s

* Created several models of electromechanical computational systems
* Mechanical relay
* Binary number system
* Z1 was first model.
* Z3 (completed in 1941)
  * Perhaps the first program-controlled general-purpose computer.
  * Input via punched tape
* Most machines destroyed during bombing of Berlin.
* Despite later support from IBM & Remington Rand, his efforts did not have huge influence on later computer developments.

#### Howard Aiken 

* 1939 dev started 
* 1944 Mark I became operational 
* Info stored in wheels like Babbage's machines
* Computational system made of relays
* Could store 72 23-digit decimal nums.
* instructions were fed via punched paper tape. 

#### John V. Atanasoff's machine 1937-42

* Perhaps 1st electronic computer system.
* performed gaussian elimination solutions for sets of equations.
* Totally electronic.
* Used capacitors (RAM-style) to store info with semiconductor tech.
* Binary number system
* separate logic, memory, and I/O portions.
* The punched card I/O system gave an error ~1/10,000 operations. This was bad (duh).
* WWII halted progress on this particular computer.


### 1.2 The Computer Generations: Technology and Innovation

A useful way to view the computer systems evolution is to group them into "Generations", as shown below.

Each generation shares not only some sense of time period in history, but also of computing capabilities and characteristics. 

#### 1.2.1 The first generation (??-1953)



