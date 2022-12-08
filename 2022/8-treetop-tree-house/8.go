package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type tree struct {
	height      int
	visible     bool
	scenicScore int
}

func newTree(height int) *tree {
	t := tree{
		height:      height,
		visible:     false,
		scenicScore: -1,
	}
	return &t
}

var forest [][]*tree = make([][]*tree, 0)
var yLen int

func main() {
	filename := os.Args[1]

	file, err := os.Open(filename)
	if err != nil {
		fmt.Printf("Couldn't open %v\n", filename)
		return
	}
	defer file.Close()

	// parse the input
	scanner := bufio.NewScanner(file)
	y := -1
	for scanner.Scan() {
		y++
		line := strings.Trim(scanner.Text(), "\n ")
		lineSlice := strings.Split(line, "")
		forest = append(forest, make([]*tree, len(lineSlice)))
		for x, v := range lineSlice {
			height, _ := strconv.Atoi(v)
			t := newTree(height)
			forest[y][x] = t
		}
	}
	yLen = y + 1

	// scan each row and column from each edge until trees are no longer visible
	for i := 0; i < yLen; i++ {
		scanRow(i)
	}
	for i := 0; i < len(forest[0]); i++ {
		scanCol(i)
	}

	// count number of visible trees and find scenic scores
	numVisible := 0
	maxScenicScore := 0
	for y := 0; y < yLen; y++ {
		for x, t := range forest[y] {
			if t.visible {
				fmt.Print("X")
				numVisible++
			} else {
				fmt.Print(".")
			}
			t.scenicScore = calcScenicScore(x, y)
			if t.scenicScore > maxScenicScore {
				maxScenicScore = t.scenicScore
			}
		}
		fmt.Print("\n")
	}
	fmt.Println("Trees visible:", numVisible)
	fmt.Println("Highest scenic score:", maxScenicScore)
}

func calcScenicScore(x int, y int) int {
	// look left
	left := 0
	if x > 0 {
		for r := x - 1; r >= 0; r-- {
			left++
			if forest[y][r].height >= forest[y][x].height {
				break
			}
		}
	}
	// look right
	right := 0
	if x < len(forest[y])-1 {
		for r := x + 1; r < len(forest[y]); r++ {
			right++
			if forest[y][r].height >= forest[y][x].height {
				break
			}
		}
	}
	// look up
	up := 0
	if y > 0 {
		for c := y - 1; c >= 0; c-- {
			up++
			if forest[c][x].height >= forest[y][x].height {
				break
			}
		}
	}
	// look down
	down := 0
	if y < yLen-1 {
		for c := y + 1; c < yLen; c++ {
			down++
			if forest[c][x].height >= forest[y][x].height {
				break
			}
		}
	}
	return left * right * up * down
}

func scanRow(y int) {
	// scan from left
	leftMaxHeight := -1
	for x := 0; x < len(forest[y])-1; x++ {
		thisTree := forest[y][x]
		if leftMaxHeight < thisTree.height {
			thisTree.visible = true
			leftMaxHeight = thisTree.height
		}
	}
	// scan from right
	rightMaxHeight := -1
	for x := len(forest[y]) - 1; x > 0; x-- {
		thisTree := forest[y][x]
		if rightMaxHeight < thisTree.height {
			thisTree.visible = true
			rightMaxHeight = thisTree.height
		}
		if rightMaxHeight == leftMaxHeight {
			break
		}
	}
}

func scanCol(x int) {
	// scan from top
	topMaxHeight := -1
	for y := 0; y < yLen-1; y++ {
		thisTree := forest[y][x]
		if topMaxHeight < thisTree.height {
			thisTree.visible = true
			topMaxHeight = thisTree.height
		}
	}
	// scan from bottom
	bottomMaxHeight := -1
	for y := yLen - 1; y > 0; y-- {
		thisTree := forest[y][x]
		if bottomMaxHeight < thisTree.height {
			thisTree.visible = true
			bottomMaxHeight = thisTree.height
		}
		if bottomMaxHeight == topMaxHeight {
			break
		}
	}
}
