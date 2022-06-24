package main
import "fmt"


// A simple program to take three numbers as input and output their word formats.
func outputNumWord(num int) {
    switch {
        case num<0 || num>10:
            fmt.Println("[ERROR: Input not in range 0-10]")
        case num==0:
            fmt.Println("Zero")
        case num==1:
            fmt.Println("One")
        case num==2:
            fmt.Println("Two")
        case num==3:
            fmt.Println("Three")
        case num==4:
            fmt.Println("Four")
        case num==5:
            fmt.Println("Five")
        case num==6:
            fmt.Println("Six")
        case num==7:
            fmt.Println("Seven")
        case num==8:
            fmt.Println("Eight")
        case num==9:
            fmt.Println("Nine")
        case num==10:
            fmt.Println("Ten")
    }
}

func main() {
    //your code goes here

    var num0 int
    fmt.Scanln(&num0)
    outputNumWord(num0)

    var num1 int
    fmt.Scanln(&num1)
    outputNumWord(num1)

    var num2 int
    fmt.Scanln(&num2)
    outputNumWord(num2)
    
}
