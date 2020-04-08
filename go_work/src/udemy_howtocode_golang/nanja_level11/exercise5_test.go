package main

import (
    "testing"
)

func TestFoo(t *testing.T) {
    var got int
    //got = 1
    if got != 0 {
        t.Errorf("foo should be 0, got %v", got)
    }
}
