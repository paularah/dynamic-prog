package main

import (
	"fmt"
)

func main() {
	memo := make(map[int]int)
	fmt.Println(fib(50, memo))
}

// memoized fibonnaci
func fib(n int, memo map[int]int) int {
	if val, present := memo[n]; present {
		return val
	}
	if n == 0 {
		return 0
	}
	if n <= 2 {
		return 1
	}
	memo[n] = fib(n-1, memo) + fib(n-2, memo)
	return memo[n]
}
