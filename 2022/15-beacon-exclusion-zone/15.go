package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type sensor struct {
	x      int
	y      int
	radius int
}

func newSensor(x int, y int, radius int) *sensor {
	s := sensor{
		x:      x,
		y:      y,
		radius: radius,
	}
	return &s
}

var sensors []*sensor = make([]*sensor, 0)
var grid map[int][]bool = make(map[int][]bool)

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Wrong number of arguments")
		return
	}
	filename := os.Args[1]
	checkRow, _ := strconv.Atoi(os.Args[2])

	file, err := os.Open(filename)
	if err != nil {
		fmt.Printf("Couldn't open %v\n", filename)
		return
	}
	defer file.Close()

	// parse the input
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.Split(strings.Trim(scanner.Text(), "\n "), " ")
		sensorX, sensorY := parseCoords(line[2], line[3])
		beaconX, beaconY := parseCoords(line[8], line[9])
		radius := int(math.Abs(float64(sensorX)-float64(beaconX)) + math.Abs(float64(sensorY)-float64(beaconY)))
		sensors = append(sensors, newSensor(sensorX, sensorY, radius))
	}

	for _, s := range sensors {
		for x := s.x - s.radius; x <= s.x+s.radius; x++ {
			yRadius := s.radius - int(math.Abs(float64(s.x-x)))
			for y := s.y - yRadius; y <= s.y+yRadius; y++ {

			}
		}
	}
}

func parseCoords(xStr string, yStr string) (x int, y int) {
	x, _ = strconv.Atoi(strings.Trim(xStr, "x=,"))
	y, _ = strconv.Atoi(strings.Trim(yStr, "y=:"))
	return
}
