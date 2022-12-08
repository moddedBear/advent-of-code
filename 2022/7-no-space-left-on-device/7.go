package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

var root *dir
var currentDir *dir
var part1 int = 0
var part2 int = math.MaxInt

type file struct {
	name     string
	location *dir
	size     int
}

func newFile(name string, location *dir, size int) *file {
	f := file{
		name:     name,
		location: location,
		size:     size,
	}
	return &f
}

type dir struct {
	name   string
	files  map[string]*file
	dirs   map[string]*dir
	parent *dir
	size   int
}

func newDir(name string) *dir {
	d := dir{
		name:  name,
		files: make(map[string]*file),
		dirs:  make(map[string]*dir),
	}
	return &d
}

func Cd(d string) {
	if d == ".." {
		currentDir = currentDir.parent
	} else if d == "/" {
		if root == nil {
			root = newDir(d)
		}
		currentDir = root
	} else {
		// assuming dir already created
		currentDir = currentDir.dirs[d]
	}
}

func parseFile(lineSlice []string) {
	if lineSlice[0] == "dir" {
		d := newDir(lineSlice[1])
		d.parent = currentDir
		currentDir.dirs[lineSlice[1]] = d
	} else {
		size, _ := strconv.Atoi(lineSlice[0])
		f := newFile(lineSlice[1], currentDir, size)
		currentDir.files[lineSlice[1]] = f
	}
}

// recursively calculates and saves size of a directory
func findSize(d *dir) int {
	result := 0
	for _, v := range d.dirs {
		result += findSize(v)
	}
	for _, v := range d.files {
		result += v.size
	}
	d.size = result
	return result
}

// finds answers for part1 and part2
func solve(d *dir, spaceToFree int) {
	for _, v := range d.dirs {
		solve(v, spaceToFree)
	}
	// part 1
	if d.size <= 100000 {
		part1 += d.size
	}
	// part 2
	if d.size >= spaceToFree && d.size < part2 {
		part2 = d.size
	}
}

func main() {
	filename := os.Args[1]

	file, err := os.Open(filename)
	if err != nil {
		fmt.Printf("Couldn't open %v\n", filename)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.Trim(scanner.Text(), "\n ")
		lineSlice := strings.Split(line, " ")
		if lineSlice[0] == "$" {
			if lineSlice[1] == "cd" {
				Cd(lineSlice[2])
			}
		} else {
			parseFile(lineSlice)
		}
	}

	// dfs to find size
	findSize(root)
	spaceToFree := 30000000 - (70000000 - root.size)
	solve(root, spaceToFree)
	fmt.Printf("Part 1: %v\nPart 2: %v\n", part1, part2)
}
