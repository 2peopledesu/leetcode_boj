package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var dx = []int{1, 0, -1, 0}
var dy = []int{0, 1, 0, -1}

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Split(bufio.ScanWords)
    writer := bufio.NewWriter(os.Stdout)
    defer writer.Flush()

    n := readInt(scanner)
    m := readInt(scanner)

    board := make([][]int, n)
    acs := [][2]int{}
    for i := 0; i < n; i++ {
        board[i] = make([]int, m)
        for j := 0; j < m; j++ {
            board[i][j] = readInt(scanner)
            if board[i][j] == 9 {
                acs = append(acs, [2]int{i, j})
            }
        }
    }

    visited := make([][]bool, n)
    for i := 0; i < n; i++ {
        visited[i] = make([]bool, m)
    }

    count := 0
    for _, ac := range acs {
        y, x := ac[0], ac[1]
        if !visited[y][x] {
            visited[y][x] = true
            count++
        }
        
        for dir := 0; dir < 4; dir++ {
            wind(y, x, dir, board, visited, n, m, &count)
        }
    }

    fmt.Fprintln(writer, count)
}

func readInt(scanner *bufio.Scanner) int {
    scanner.Scan()
    val, _ := strconv.Atoi(scanner.Text())
    return val
}

func isIn(y, x, n, m int) bool {
    return y >= 0 && y < n && x >= 0 && x < m
}

func wind(y, x, dir int, board [][]int, visited [][]bool, n, m int, count *int) {
    for {
        y += dy[dir]
        x += dx[dir]
        
        if !isIn(y, x, n, m) {
            break
        }
        
        if !visited[y][x] {
            visited[y][x] = true
            *count++
        }
        
        objectType := board[y][x]
        
        if objectType == 1 {
            if dir == 0 || dir == 2 {
                break
            }
        } else if objectType == 2 {
            if dir == 1 || dir == 3 {
                break
            }
        } else if objectType == 3 {
            if dir == 0 {
                dir = 3
            } else if dir == 1 {
                dir = 2
            } else if dir == 2 {
                dir = 1
            } else {
                dir = 0
            }
        } else if objectType == 4 {
            if dir == 0 {
                dir = 1
            } else if dir == 1 {
                dir = 0
            } else if dir == 2 {
                dir = 3
            } else {
                dir = 2
            }
        } else if objectType == 9 {
            continue
        }
    }
}