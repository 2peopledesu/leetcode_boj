package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

func main() {
	var left []int
	var right []int

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		var l, r int
		fmt.Sscanf(line, "%d %d", &l, &r)
		left = append(left, l)
		right = append(right, r)
	}

	sort.Ints(left)
	sort.Ints(right)

	sum := 0
	for i := 0; i < len(left); i++ {
		diff := right[i] - left[i]
		sum += int(math.Abs(float64(diff)))
	}

	fmt.Println(sum)
}