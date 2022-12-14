package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type point struct {
	y int
	x int
}

func newPoint(x int, y int) *point {
	p := point{
		y: y,
		x: x,
	}
	return &p
}

var heightmap [][]int = make([][]int, 0)
var distances [][]int = make([][]int, 0)
var exploreQueue []*point = make([]*point, 0)
var start *point
var end *point

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
	for y := 0; scanner.Scan(); y++ {
		line := strings.Split(strings.Trim(scanner.Text(), "\n "), "")
		hRow := make([]int, len(line))
		dRow := make([]int, len(line))
		for x, c := range line {
			if c == "S" {
				start = &point{x: x, y: y}
				hRow[x] = 0
				dRow[x] = 0
			} else if c == "E" {
				end = &point{x: x, y: y}
				hRow[x] = 25
			} else {
				hRow[x] = int([]rune(c)[0] - 'a')
			}
			dRow[x] = -1
		}
		heightmap = append(heightmap, hRow)
		distances = append(distances, dRow)
	}

	// part 1
	distances[start.y][start.x] = 0
	exploreQueue = append(exploreQueue, start)
	for len(exploreQueue) > 0 {
		next := exploreQueue[0]
		exploreQueue = exploreQueue[1:]
		explore(next)
	}
	fmt.Println("Shortest distance from start to end:", distances[end.y][end.x])

	// part 2
	for y := 0; y < len(distances); y++ {
		for x := 0; x < len(distances[y]); x++ {
			distances[y][x] = -1 // reset the distances
		}
	}
	distances[end.y][end.x] = 0
	exploreQueue = append(exploreQueue, end)
	for len(exploreQueue) > 0 {
		next := exploreQueue[0]
		exploreQueue = exploreQueue[1:]
		explore2(next)
	}
}

func explore(p *point) {
	if p.x == end.x && p.y == end.y {
		exploreQueue = exploreQueue[:0]
		return
	}
	// check above
	if p.y > 0 && distances[p.y-1][p.x] == -1 && heightmap[p.y-1][p.x]-heightmap[p.y][p.x] <= 1 {
		exploreQueue = append(exploreQueue, newPoint(p.x, p.y-1))
		distances[p.y-1][p.x] = distances[p.y][p.x] + 1
	}
	// check right
	if p.x < len(distances[p.y])-1 && distances[p.y][p.x+1] == -1 && heightmap[p.y][p.x+1]-heightmap[p.y][p.x] <= 1 {
		exploreQueue = append(exploreQueue, newPoint(p.x+1, p.y))
		distances[p.y][p.x+1] = distances[p.y][p.x] + 1
	}
	// check down
	if p.y < len(distances)-1 && distances[p.y+1][p.x] == -1 && heightmap[p.y+1][p.x]-heightmap[p.y][p.x] <= 1 {
		exploreQueue = append(exploreQueue, newPoint(p.x, p.y+1))
		distances[p.y+1][p.x] = distances[p.y][p.x] + 1
	}
	// check left
	if p.x > 0 && distances[p.y][p.x-1] == -1 && heightmap[p.y][p.x-1]-heightmap[p.y][p.x] <= 1 {
		exploreQueue = append(exploreQueue, newPoint(p.x-1, p.y))
		distances[p.y][p.x-1] = distances[p.y][p.x] + 1
	}
}

func explore2(p *point) {
	if heightmap[p.y][p.x] == 0 {
		exploreQueue = exploreQueue[:0]
		fmt.Println("Shortest distance from end to lowest elevation:", distances[p.y][p.x])
		return
	}
	// check above
	if p.y > 0 && distances[p.y-1][p.x] == -1 && heightmap[p.y][p.x]-heightmap[p.y-1][p.x] <= 1 {
		exploreQueue = append(exploreQueue, newPoint(p.x, p.y-1))
		distances[p.y-1][p.x] = distances[p.y][p.x] + 1
	}
	// check right
	if p.x < len(distances[p.y])-1 && distances[p.y][p.x+1] == -1 && heightmap[p.y][p.x]-heightmap[p.y][p.x+1] <= 1 {
		exploreQueue = append(exploreQueue, newPoint(p.x+1, p.y))
		distances[p.y][p.x+1] = distances[p.y][p.x] + 1
	}
	// check down
	if p.y < len(distances)-1 && distances[p.y+1][p.x] == -1 && heightmap[p.y][p.x]-heightmap[p.y+1][p.x] <= 1 {
		exploreQueue = append(exploreQueue, newPoint(p.x, p.y+1))
		distances[p.y+1][p.x] = distances[p.y][p.x] + 1
	}
	// check left
	if p.x > 0 && distances[p.y][p.x-1] == -1 && heightmap[p.y][p.x]-heightmap[p.y][p.x-1] <= 1 {
		exploreQueue = append(exploreQueue, newPoint(p.x-1, p.y))
		distances[p.y][p.x-1] = distances[p.y][p.x] + 1
	}
}
