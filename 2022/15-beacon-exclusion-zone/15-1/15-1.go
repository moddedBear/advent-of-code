package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"

	mapset "github.com/deckarep/golang-set/v2"
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

type point struct {
	x int
	y int
}

var sensors []*sensor = make([]*sensor, 0)
var beacons mapset.Set[point] = mapset.NewThreadUnsafeSet[point]()

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Wrong number of arguments")
		return
	}
	filename := os.Args[1]
	rowToCheck, _ := strconv.Atoi(os.Args[2])

	file, err := os.Open(filename)
	if err != nil {
		fmt.Printf("Couldn't open %v\n", filename)
		return
	}
	defer file.Close()

	// parse the input
	maxX := math.Inf(-1)
	minX := math.Inf(1)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.Split(strings.Trim(scanner.Text(), "\n "), " ")
		sensorX, sensorY := parseCoords(line[2], line[3])
		beaconX, beaconY := parseCoords(line[8], line[9])
		beacons.Add(point{beaconX, beaconY})
		radius := int(math.Abs(float64(sensorX)-float64(beaconX)) + math.Abs(float64(sensorY)-float64(beaconY)))
		sensors = append(sensors, newSensor(sensorX, sensorY, radius))

		if float64(sensorX+radius) > maxX {
			maxX = float64(sensorX + radius)
		}
		if float64(sensorX-radius) < minX {
			minX = float64(sensorX - radius)
		}
	}

	excluded := 0
	for x := int(minX); x <= int(maxX); x++ {
		if beacons.Contains(point{x, rowToCheck}) {
			continue
		}
		for _, s := range sensors {
			if int(math.Abs(float64(s.x-x))+math.Abs(float64(s.y-rowToCheck))) <= s.radius {
				excluded++
				break
			}
		}
	}
	fmt.Printf("%v positions in line %v where a beacon cannot be present.\n", excluded, rowToCheck)
}

func parseCoords(xStr string, yStr string) (x int, y int) {
	x, _ = strconv.Atoi(strings.Trim(xStr, "x=,"))
	y, _ = strconv.Atoi(strings.Trim(yStr, "y=:"))
	return
}
