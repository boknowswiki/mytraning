package main

import (
	"fmt"
)

func main() {
    x := map[string][]string {
        `bond_james`: []string{`Shaken, not stirred`, `Martinis`, `Women`},
        `moneypenny_miss`: []string{`James Bond`, `Literature`, `Computer Science`},
        `no_dr`: []string{`Being evil`, `Ice cream`, `Sunsets`},
    }

    fmt.Println(x)

    x[`harry_poter`] = []string {`abc`, `def`, `ghi`}

    delete(x, `bond_james`)

    for k, v := range x {
        fmt.Println(k, v)
        for i, vv := range v {
            fmt.Println(i, vv)
        }
    }

}
