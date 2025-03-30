package main

import (
	"fmt"
)

func rgbToHsv(r, g, b int) (float64, float64, float64) {

	maxVal := max(max(r, g), b)
	minVal := min(min(r, g), b)
	
	v := float64(maxVal)
	
	var s float64
	if maxVal == 0 {
		s = 0
	} else {
		s = 255.0 * float64(maxVal-minVal) / float64(maxVal)
	}
	
	var h float64
	if maxVal == minVal {
		h = 0
	} else if maxVal == r {
		h = 60.0 * float64(g-b) / float64(maxVal-minVal)
	} else if maxVal == g {
		h = 120.0 + 60.0*float64(b-r)/float64(maxVal-minVal)
	} else {
		h = 240.0 + 60.0*float64(r-g)/float64(maxVal-minVal)
	}
	
	if h < 0 {
		h += 360.0
	}
	
	return h, s, v
}

func isTruePurple(h, s, v float64, hRange, sRange, vRange [2]int) bool {
	hLo, hHi := float64(hRange[0]), float64(hRange[1])
	sLo, sHi := float64(sRange[0]), float64(sRange[1])
	vLo, vHi := float64(vRange[0]), float64(vRange[1])
	
	return (hLo <= h && h <= hHi) && (sLo <= s && s <= sHi) && (vLo <= v && v <= vHi)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	var hLo, hHi int
	var sLo, sHi int
	var vLo, vHi int
	var r, g, b int
	
	fmt.Scan(&hLo, &hHi)
	fmt.Scan(&sLo, &sHi)
	fmt.Scan(&vLo, &vHi)
	fmt.Scan(&r, &g, &b)
	
	h, s, v := rgbToHsv(r, g, b)
	
	if isTruePurple(h, s, v, [2]int{hLo, hHi}, [2]int{sLo, sHi}, [2]int{vLo, vHi}) {
		fmt.Println("Lumi will like it.")
	} else {
		fmt.Println("Lumi will not like it.")
	}
}