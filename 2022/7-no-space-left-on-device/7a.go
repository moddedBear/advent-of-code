package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var root *dir
var currentDir *dir

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
	d := dir{name: name}
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
	}
}
