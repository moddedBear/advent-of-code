package main

import (
	"bufio"
	"fmt"
	"os"
)

var root dir
var currentDir *dir

type file struct {
	name     string
	location *dir
	size     int
}

type dir struct {
	name   string
	files  map[string]*file
	dirs   map[string]*dir
	parent *dir
	size   int
}

func newDir(name string) dir {
	d := dir{name: name}
	return d
}

func newFile(name string, location *dir, size int) file {
	f := file{
		name:     name,
		location: location,
		size:     size,
	}
	return f
}

func parseCommand(line string) {

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

	}
}
