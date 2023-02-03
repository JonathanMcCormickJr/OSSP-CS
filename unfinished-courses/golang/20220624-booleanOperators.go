package main

import "fmt"

func main() {
  x := 42
  y := 8
    
  // logical AND
  fmt.Println(x!=y && x<=y)
    
  // logical OR
  fmt.Println(x!=y || x<=y)

  // logical XOR (X || Y) && !(X && Y)
  cond0 := x!=y
  cond1 := x>=y
  fmt.Println((cond0 || cond1) && !(cond0 && cond1))
    
  // logical NOT
  fmt.Println(!(x>y))
}
