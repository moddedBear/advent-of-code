package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type sand struct {
	x int
	y int
}

func newSand() *sand {
	s := sand{
		x: sourceX,
		y: sourceY,
	}
	return &s
}

var grid [][]int = make([][]int, 0) // 0 = air, 1 = rock, sand = 2
var sourceX = 500
var sourceY = 0
var floorGap = 2
var active *sand
var restCount = 0

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Aren't you forgetting something?")
		return
	}
	filename := os.Args[1]

	file, err := os.Open(filename)
	if err != nil {
		fmt.Printf("Couldn't open %v\n", filename)
		return
	}
	defer file.Close()

	// parse the input
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		endpoints := strings.Split(strings.Trim(scanner.Text(), "\n "), " -> ")
		for i := 0; i < len(endpoints)-1; i++ {
			start := strings.Split(endpoints[i], ",")
			startX, _ := strconv.Atoi(start[0])
			startY, _ := strconv.Atoi(start[1])
			end := strings.Split(endpoints[i+1], ",")
			endX, _ := strconv.Atoi(end[0])
			endY, _ := strconv.Atoi(end[1])

			// resize grid if necessary
			for startY > len(grid)-1 || endY > len(grid)-1 {
				grid = append(grid, make([]int, sourceX*2))
			}

			// move along y-axis
			if startX == endX {
				if startY < endY {
					for y := startY; y <= endY; y++ {
						grid[y][startX] = 1
					}
				} else {
					for y := startY; y >= endY; y-- {
						grid[y][startX] = 1
					}
				}
			}
			// move along x-axis
			if startY == endY {
				if startX < endX {
					for x := startX; x <= endX; x++ {
						grid[startY][x] = 1
					}
				} else {
					for x := startX; x >= endX; x-- {
						grid[startY][x] = 1
					}
				}
			}
		}
	}

	// create floor
	for i := 0; i < floorGap; i++ {
		grid = append(grid, make([]int, sourceX*2))
	}
	for x := 0; x < len(grid[len(grid)-1]); x++ {
		grid[len(grid)-1][x] = 1
	}

	for tick() {
	}

	fmt.Println("Units of sand at rest:", restCount)
}

func tick() bool {
	if active == nil {
		active = newSand()
	}
	if grid[active.y+1][active.x] == 0 { // check down
		active.y++
	} else if grid[active.y+1][active.x-1] == 0 { // check down-left
		active.y++
		active.x--
	} else if grid[active.y+1][active.x+1] == 0 { // check down-right
		active.y++
		active.x++
	} else { // at rest
		grid[active.y][active.x] = 2
		restCount++
		if active.y == sourceY && active.x == sourceX {
			return false
		}
		active = newSand()
	}
	return true
}
