package main

import (
	"fmt"
	"math/rand"
)

func main() {
	sum := 0.0
	for i := 0; i < 1000000*500; i++ {
		rand.NormFloat64()
	}
	fmt.Println(sum)
}
