package main

/*
 * https://golang.org/pkg/
 */

import (
    "fmt"
    "math/cmplx"
    //"net"
    //"io"
)

type person struct {
    first_name  string
    last_name   string
    age         int
}

/*
 * basic types: 
 *              string, bool, int(int8, uint8 ...int64, uint64), float32,
 *              float64, complex64, complex128,
 *              byte alias uint8,
 *              rune alias int32, represents a Unicode code point
 * composite types:
 *              pointer, struct, function,
 *              container types (array, slice(like list in python),
 *                              map(like dict in python))
 *              channel, interface
 */

func main () {
    // automatically declare the right type
    x := 1
    y := 2
    //var x, y int = 1, 2
    fmt.Println(add(x,y))

    var z complex128 = cmplx.Sqrt(-5 + 12i)
    fmt.Printf("type: %T, value: %v\n", z, z)

    //int array
    int_a := [6]int{1,2,3,4,5,6}
    fmt.Println(int_a)

    //slice
    var s []int = int_a[1:4]
    fmt.Println(s)

	names := [4]string{
		"John",
		"Paul",
		"George",
		"Ringo",
	}
	fmt.Println(names)

	a := names[0:2]
	b := names[1:3]
	fmt.Println(a, b)

	b[0] = "XXX"
	fmt.Println(a, b)
	fmt.Println(names)

    slice_names := names[:]
	fmt.Println("slice names are ", slice_names)

    slice_names = append(slice_names, "Bo", "Bob")
	fmt.Println("after append slice names ", slice_names)

    //pointer
    p := &x
    fmt.Println(*p)
    *p = 6
    fmt.Println("this is new x", x)

    //struct
    fmt.Println(person{first_name:"bo", last_name:"tao", age:1})
    n_p := person{first_name:"bo", last_name:"tao", age:1}
    newPerson(n_p)
    //newPerson(&n_p)
    n_p.printAll()
    fmt.Println(n_p)
    //(&n_p).printAll()
}

//func (p *person) printAll() {
func (p person) printAll() {
    p.age = 5
    fmt.Println(p)
}

func newPerson (p person) {
//func newPerson (p *person) {
    p.age = 2
}

func add(x int, y int) int {
    return x+y
}
