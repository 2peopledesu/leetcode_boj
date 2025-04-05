package main

import (
	"fmt"
)

type Pos struct {
	x, y int
}

var (
	n, m     int
	board    [][]byte
	red, blu Pos
	hole     Pos
	dx       = []int{0, 1, 0, -1}
	dy       = []int{1, 0, -1, 0}
	dir      = []byte{'R', 'D', 'L', 'U'}
)

func main() {
	fmt.Scan(&n, &m)

	board = make([][]byte, n)
	for i := 0; i < n; i++ {
		var row string
		fmt.Scan(&row)
		board[i] = []byte(row)
		
		for j := 0; j < m; j++ {
			if board[i][j] == 'R' {
				red = Pos{i, j}
				board[i][j] = '.'
			} else if board[i][j] == 'B' {
				blu = Pos{i, j}
				board[i][j] = '.'
			} else if board[i][j] == 'O' {
				hole = Pos{i, j}
			}
		}
	}

	result, path := bfs()
	if result == -1 {
		fmt.Println(-1)
	} else {
		fmt.Println(result)
		fmt.Println(path)
	}
}

func bfs() (int, string) {
	visited := make(map[string]bool)
	
	type State struct {
		red, blu Pos
		depth    int
		path     string
	}
	
	queue := []State{{red, blu, 0, ""}}
	
	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]
		
		if curr.depth > 10 {
			continue
		}
		
		if curr.red.x == hole.x && curr.red.y == hole.y {
			return curr.depth, curr.path
		}
		
		key := fmt.Sprintf("%d,%d,%d,%d", curr.red.x, curr.red.y, curr.blu.x, curr.blu.y)
		if visited[key] {
			continue
		}
		visited[key] = true
		
		for i := 0; i < 4; i++ {
			nRed, nBlu := tilt(curr.red, curr.blu, i)
			
			if nBlu.x == hole.x && nBlu.y == hole.y {
				continue
			}
			
			if nRed.x == curr.red.x && nRed.y == curr.red.y && 
			   nBlu.x == curr.blu.x && nBlu.y == curr.blu.y {
				continue
			}
			
			queue = append(queue, State{nRed, nBlu, curr.depth + 1, curr.path + string(dir[i])})
		}
	}
	
	return -1, ""
}

func tilt(r, b Pos, direction int) (Pos, Pos) {
	redFirst := true
	if direction == 0 && r.y < b.y {
		redFirst = false
	} else if direction == 1 && r.x < b.x {
		redFirst = false
	} else if direction == 2 && r.y > b.y {
		redFirst = false
	} else if direction == 3 && r.x > b.x {
		redFirst = false
	}
	
	nRed, nBlu := r, b
	
	if redFirst {
		nRed = moveMarble(r, direction, b, hole)
		nBlu = moveMarble(b, direction, nRed, hole)
		if nBlu.x == hole.x && nBlu.y == hole.y {
			return nRed, nBlu
		}
		if nRed.x == hole.x && nRed.y == hole.y {
			return nRed, nBlu
		}
		if nRed.x == nBlu.x && nRed.y == nBlu.y {
			if direction == 0 {
				nBlu.y--
			} else if direction == 1 {
				nBlu.x--
			} else if direction == 2 {
				nBlu.y++
			} else {
				nBlu.x++
			}
		}
	} else {
		nBlu = moveMarble(b, direction, r, hole)
		if nBlu.x == hole.x && nBlu.y == hole.y {
			return nRed, nBlu
		}
		nRed = moveMarble(r, direction, nBlu, hole)
		if nRed.x == hole.x && nRed.y == hole.y {
			return nRed, nBlu
		}
		if nRed.x == nBlu.x && nRed.y == nBlu.y {
			if direction == 0 {
				nRed.y--
			} else if direction == 1 {
				nRed.x--
			} else if direction == 2 {
				nRed.y++
			} else {
				nRed.x++
			}
		}
	}
	
	return nRed, nBlu
}

func moveMarble(marble Pos, direction int, other Pos, hole Pos) Pos {
	nx, ny := marble.x, marble.y
	
	for {
		nx += dx[direction]
		ny += dy[direction]
		
		if board[nx][ny] == '#' {
			return Pos{nx - dx[direction], ny - dy[direction]}
		}
		
		if nx == hole.x && ny == hole.y {
			return Pos{nx, ny}
		}
		
		if nx == other.x && ny == other.y && other.x != hole.x && other.y != hole.y {
			return Pos{nx - dx[direction], ny - dy[direction]}
		}
	}
}