package main

import "fmt"

func main() {
  var x float32

  fmt.Scanln(&x) 
  
  // My first experience using the Switch/Case method instead of the if/elseif/else method. 
  switch {
    case x>0 && x<10:
      fmt.Println(x, "is a positive number less than 10.")
    case x >= 10:
      fmt.Println(x, "is too big.")
    case x<=0:
        fmt.Println(x, "is not a positive number.")
  }
}

