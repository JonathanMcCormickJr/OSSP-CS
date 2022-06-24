package main

import "fmt"

func main() {
  //  Increments a number and adds it to a snowball-style result.
    /* The reason that starting incrementGen produces the same end result 
    when it is either a 0 or a 1 is because the 0 (which 
    contributes nothing) is added at the floor, while the ceiling 
    remains at the same height. That results in the range being 
    the same except for a zero being added at the floor, which
    does not change the end result.*/

  fmt.Println("INCREMENT STARTING AT 0:\n")
  
  incrementGen := 0  // Increment generation level
  res := 0  // Result
  for incrementGen <= 20 {
      fmt.Println("increment generation:", incrementGen)
      fmt.Println("result:", res, "\n")
    res += incrementGen
    incrementGen++
  }
  fmt.Println("FINAL RESULT 0:", res) 

  fmt.Println("\n\n--------------------\n\nINCREMENT STARTING AT 1:\n")

  incrementGen1 := 1
  res1 := 0 
  for incrementGen1 <= 20 {
      fmt.Println("increment generation:", incrementGen1)
      fmt.Println("res1:", res1, "\n")
    res1 += incrementGen1
    incrementGen1++
  }
  fmt.Println("FINAL RESULT 1:", res1) 
}
