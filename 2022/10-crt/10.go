package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var x = 1
var cycle = 1
var cyclesLeft = 0 // 0 if ready for another command, otherwise number of cycles til completion
var newX = x       // new value of x after command finishes
var commands [][]string = make([][]string, 0)
var signalSum = 0
var display [6][40]string

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
	for scanner.Scan() {
		command := strings.Split(strings.Trim(scanner.Text(), "\n "), " ")
		commands = append(commands, command)
	}

	for len(commands) > 0 {
		doCycle()
	}

	fmt.Println("Signal strength sum:", signalSum)
	render()
}

func doCycle() {
	if cyclesLeft == 0 { // ready for next command
		x = newX
		command := commands[0]
		commands = commands[1:]
		parseCommand(command)
	}
	monitorSignalStrength()
	draw()
	cycle++
	cyclesLeft--
}

func parseCommand(command []string) {
	if command[0] == "noop" {
		cyclesLeft = 1
		newX = x
	} else if command[0] == "addx" {
		v, _ := strconv.Atoi(command[1])
		newX = addx(v)
		cyclesLeft = 2
	}
}

func addx(v int) int {
	return x + v
}

func monitorSignalStrength() {
	if (cycle-20)%40 == 0 {
		signalStrength := cycle * x
		signalSum += signalStrength
	}
}

func draw() {
	pixelX := (cycle - 1) % 40
	pixelY := (cycle - 1) / 40
	if x-1 <= pixelX && pixelX <= x+1 {
		display[pixelY][pixelX] = "#"
	} else {
		display[pixelY][pixelX] = " "
	}
}

func render() {
	for _, line := range display {
		for _, pixel := range line {
			fmt.Print(pixel)
		}
		fmt.Print("\n")
	}
}
