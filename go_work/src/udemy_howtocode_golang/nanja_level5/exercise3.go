package main

import (
	"fmt"
)

type vehicle struct {
    doors   int
    color   string
}

type truck struct {
    vehicle
    fourWheel bool
}

type sedan struct {
    vehicle
    luxury  bool
}

func main() {

    p1 := truck {
        vehicle: vehicle {
            doors: 2,
            color: "white",
        },
        fourWheel: true,
    }


    p2 := sedan {
        vehicle: vehicle {
            doors: 4,
            color: "black",
        },
        luxury: true,
    }

    fmt.Println(p1)
    fmt.Println(p2)
}
