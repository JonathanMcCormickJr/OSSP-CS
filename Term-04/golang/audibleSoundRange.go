package main

import "fmt"

func main() {
  var f int  // frequency
  fmt.Scanln(&f)
  /* This is a simple program to determine 
  whether a given sound frequency (Hz) is 
  Audible, Infrasound, or Ultrasound.
  https://en.wikipedia.org/wiki/Audio_frequency
  
  This micro-project done in the course of 
  studying via Sololearn's Go course. 
  */
  switch {
    case f<0:
      fmt.Println("ERROR: Input is less than 0.")
    case f<20:
      fmt.Println("Infrasound")
    case f>20000:
      fmt.Println("Ultrasound")
    case f<20000 && f>20:
      fmt.Println("Audible")
    default:
      fmt.Println("Error")
    
  }
  
}
