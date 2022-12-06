package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	filename := os.Args[1]

	file, err := os.Open(filename)
	if err != nil {
		fmt.Printf("Couldn't open %v\n", filename)
		return
	}
	defer file.Close()

	// parse crate stack
	var stacks [][]string = nil
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if stacks == nil {
			stacks = make([][]string, (len(line)+1)/4)
		}
		if _, err := strconv.Atoi(line[1:2]); line[1:2] != " " && err == nil {
			// done parsing the crate stack if a number is found
			break
		}
		for i := 0; i < (len(line)+1)/4; i++ {
			crate := line[i*4+1 : i*4+2]
			if crate != " " {
				stacks[i] = append(stacks[i], crate)
			}
		}
	}

	// run instructions
	for scanner.Scan() {
		line := scanner.Text()
		if len(line) == 0 || line[0:1] == "\n" {
			continue
		}
		lineSlice := strings.Split(line, " ")
		quantity, _ := strconv.Atoi(lineSlice[1])
		fromStack, _ := strconv.Atoi(lineSlice[3])
		fromStack--
		toStack, _ := strconv.Atoi(lineSlice[5])
		toStack--
		fmt.Printf("Moving %v from %v (%v) to %v (%v)\n", quantity, fromStack+1, strings.Join(stacks[fromStack], ""), toStack+1, strings.Join(stacks[toStack], ""))
		tempSlice := stacks[fromStack][:quantity]
		stacks[fromStack] = stacks[fromStack][quantity:]
		fmt.Printf("Grabbed %v\n", strings.Join(tempSlice, ""))
		stacks[toStack] = append(tempSlice, stacks[toStack]...)
		fmt.Printf("Moved %v from %v (%v) to %v (%v)\n\n", quantity, fromStack+1, strings.Join(stacks[fromStack], ""), toStack+1, strings.Join(stacks[toStack], ""))
	}

	// get answer
	var result []string
	for i, stack := range stacks {
		result = append(result, stack[0])
		fmt.Printf("%v: %v\n", i+1, strings.Join(stack, ""))
	}
	println(strings.Join(result, ""))
}
