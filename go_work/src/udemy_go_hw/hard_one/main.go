package main

import (
    "fmt"
    "os"
    "io"
)

func main() {
    //fmt.Println(os.Args[1])
    f_name := os.Args[1]
    file, err := os.Open(f_name)
    if err != nil {
        fmt.Println("Open file", f_name, "error", err)
        os.Exit(1)
    }

    data := make([]byte, 10000)
    count, err := file.Read(data)
    if err != nil {
        fmt.Println("Read file", f_name, "error", err)
        file.Close()
        os.Exit(1)
    }

    fmt.Printf("read %d bytes: %q\n", count, data[:count])

    file.Seek(0, 0)

    io.Copy(os.Stdout, file)

    file.Close()
}
