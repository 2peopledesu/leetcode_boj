package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)

	n := readInt(scanner)
	m := readInt(scanner)

	p := make([]int, n)
	for i := 0; i < n; i++ {
		p[i] = readInt(scanner)
	}

	sumOver2 := 0
	countOver2 := 0
	for _, pi := range p {
		if pi >= 2 {
			sumOver2 += pi
			countOver2++
		}
	}
	avg := 0.0
	if countOver2 > 0 {
		avg = float64(sumOver2) / float64(countOver2)
	}

	invalid := false
	for _, pi := range p {
		if float64(pi) <= avg && pi > m {
			invalid = true
			break
		}
	}
	if invalid {
		fmt.Println(-1)
		return
	}

	counts := make([]int, m)
	delta := make([]int, m+1)
	sumFull := 0
	overCount := 0

	for _, pi := range p {
		if float64(pi) <= avg {
			if pi == 0 {
				continue
			}
			q := pi / m
			r := pi % m
			sumFull += q
			if r > 0 {
				delta[0]++
				delta[r]--
			}
		} else {
			if pi >= 1 {
				overCount++
			}
		}
	}

	current := 0
	for i := 0; i < m; i++ {
		current += delta[i]
		counts[i] = sumFull + current
	}

	if overCount > 0 {
		counts[0] += overCount
	}

	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for i, c := range counts {
		if i > 0 {
			fmt.Fprint(writer, " ")
		}
		fmt.Fprint(writer, c)
	}
	fmt.Fprintln(writer)
}

func readInt(scanner *bufio.Scanner) int {
	scanner.Scan()
	val, _ := strconv.Atoi(scanner.Text())
	return val
}