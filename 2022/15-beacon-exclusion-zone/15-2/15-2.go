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
	searchRange, _ := strconv.Atoi(os.Args[2])

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

	for y := 0; y <= searchRange; y++ {
		for x := 0; x <= searchRange; x++ {
			if beacons.Contains(point{x, y}) {
				continue
			}
			if result, s := isInRange(x, y); result {
				x = s.radius - int(math.Abs(float64(s.y-y))) + s.x
			} else {
				fmt.Printf("x=%v, y=%v\n", x, y)
				fmt.Println(x*4000000 + y)
				return
			}
		}
	}

}

func parseCoords(xStr string, yStr string) (x int, y int) {
	x, _ = strconv.Atoi(strings.Trim(xStr, "x=,"))
	y, _ = strconv.Atoi(strings.Trim(yStr, "y=:"))
	return
}

func isInRange(x int, y int) (bool, *sensor) {
	for _, s := range sensors {
		if int(math.Abs(float64(s.x-x))+math.Abs(float64(s.y-y))) <= s.radius {
			return true, s
		}
	}
	return false, nil
}
