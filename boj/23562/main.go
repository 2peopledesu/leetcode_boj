package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func isInRange(y, x, k, n, m int) bool {
	return y >= 0 && y+3*k-1 < n && x >= 0 && x+3*k-1 < m
}

func calculateCost(y, x, k, a, b int, graph []string) int {
	cost := 0
	
	for i := 0; i < len(graph); i++ {
		for j := 0; j < len(graph[0]); j++ {
			isBlack := graph[i][j] == '#'
			
			inShape := false
			
			if i >= y && i < y+k && j >= x && j < x+3*k {
				inShape = true
			}
			
			if i >= y+k && i < y+2*k && j >= x && j < x+k {
				inShape = true
			}
			
			if i >= y+2*k && i < y+3*k && j >= x && j < x+3*k {
				inShape = true
			}
			
			if inShape && !isBlack {
				cost += a
			}

			if !inShape && isBlack {
				cost += b
			}
		}
	}
	
	return cost
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, m int
	fmt.Fscan(reader, &n, &m)

	var a, b int
	fmt.Fscan(reader, &a, &b)

	graph := make([]string, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &graph[i])
	}

	fmt.Println(graph)

	minCost := math.MaxInt32

	maxK := min(n, m) / 3
	for k := 1; k <= maxK; k++ {
		for y := 0; y <= n-3*k; y++ {
			for x := 0; x <= m-3*k; x++ {
				if isInRange(y, x, k, n, m) {
					cost := calculateCost(y, x, k, a, b, graph)
					minCost = min(minCost, cost)
				}
			}
		}
	}

	fmt.Fprintln(writer, minCost)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}