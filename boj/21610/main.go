package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	n, m int
	a    [][]int
	dx   = []int{0, -1, -1, -1, 0, 1, 1, 1}
	dy   = []int{-1, -1, 0, 1, 1, 1, 0, -1}
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	line, _ := reader.ReadString('\n')
	parts := strings.Split(strings.TrimSpace(line), " ")
	n, _ = strconv.Atoi(parts[0])
	m, _ = strconv.Atoi(parts[1])

	a = make([][]int, n)
	for i := 0; i < n; i++ {
		line, _ = reader.ReadString('\n')
		nums := strings.Split(strings.TrimSpace(line), " ")
		a[i] = make([]int, n)
		for j := 0; j < n; j++ {
			a[i][j], _ = strconv.Atoi(nums[j])
		}
	}

	clouds := make([][]bool, n)
	for i := 0; i < n; i++ {
		clouds[i] = make([]bool, n)
	}
	clouds[n-1][0] = true
	clouds[n-1][1] = true
	clouds[n-2][0] = true
	clouds[n-2][1] = true

	movedClouds := make([][]bool, n)
	for i := 0; i < n; i++ {
		movedClouds[i] = make([]bool, n)
	}

	for i := 0; i < m; i++ {
		line, _ = reader.ReadString('\n')
		parts = strings.Split(strings.TrimSpace(line), " ")
		d, _ := strconv.Atoi(parts[0])
		s, _ := strconv.Atoi(parts[1])
		d--

		for r := 0; r < n; r++ {
			for c := 0; c < n; c++ {
				movedClouds[r][c] = false
			}
		}

		for r := 0; r < n; r++ {
			for c := 0; c < n; c++ {
				if clouds[r][c] {
					nr := (r + dx[d]*s%n) % n
					nc := (c + dy[d]*s%n) % n
					if nr < 0 {
						nr = (nr + n) % n
					}
					if nc < 0 {
						nc = (nc + n) % n
					}
					movedClouds[nr][nc] = true
					a[nr][nc]++
				}
			}
		}

		for r := 0; r < n; r++ {
			for c := 0; c < n; c++ {
				clouds[r][c] = false
			}
		}

		for r := 0; r < n; r++ {
			for c := 0; c < n; c++ {
				if movedClouds[r][c] {
					count := 0
					if r-1 >= 0 && c-1 >= 0 && a[r-1][c-1] > 0 {
						count++
					}
					if r-1 >= 0 && c+1 < n && a[r-1][c+1] > 0 {
						count++
					}
					if r+1 < n && c-1 >= 0 && a[r+1][c-1] > 0 {
						count++
					}
					if r+1 < n && c+1 < n && a[r+1][c+1] > 0 {
						count++
					}
					a[r][c] += count
				}
			}
		}

		for r := 0; r < n; r++ {
			for c := 0; c < n; c++ {
				if a[r][c] >= 2 && !movedClouds[r][c] {
					clouds[r][c] = true
					a[r][c] -= 2
				}
			}
		}
	}

	totalWater := 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			totalWater += a[i][j]
		}
	}
	fmt.Fprintln(writer, totalWater)
}