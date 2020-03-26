package main

import "fmt"

type triangle struct{ heigth float64
                    base float64
                  }
type square struct{ sideLength float64}

type shape interface {
    getArea() float64
}

func main() {
    t := triangle{heigth: 3, base: 4}
    s := square{sideLength: 3}

    fmt.Println(printArea(t))
    fmt.Println(printArea(s))
}

func (t triangle) getArea() float64 {

    return 0.5*t.base*t.heigth
}

func (s square) getArea() float64 {

    return s.sideLength * s.sideLength
}

func printArea(s shape) float64 {
    return s.getArea()
}

