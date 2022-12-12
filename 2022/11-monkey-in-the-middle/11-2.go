package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const ROUND_LIMIT = 10000

type monkey struct {
	items     []int
	inspected int      // count of number of items inspected
	operation []string // list of operands and operators
	test      int      // the number to test divisibility with
	ifTrue    int      // the monkey to throw to if test passes
	ifFalse   int      // the monkey to throw to otherwise
}

func newMonkey(items []int, operation []string, test int, ifTrue int, ifFalse int) *monkey {
	m := monkey{
		items:     items,
		inspected: 0,
		operation: operation,
		test:      test,
		ifTrue:    ifTrue,
		ifFalse:   ifFalse,
	}
	return &m
}

var barrel []*monkey = make([]*monkey, 0)
var cycleLength int = 1

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
	var items []int
	var operation []string
	var test int
	var ifTrue int
	var ifFalse int
	for scanner.Scan() {
		line := strings.Split(strings.Trim(scanner.Text(), "\n "), ": ")
		if line[0] == "Starting items" {
			itemsStrings := strings.Split(line[1], ", ")
			items = make([]int, len(itemsStrings))
			for i, item := range itemsStrings {
				items[i], _ = strconv.Atoi(item)
			}
		} else if line[0] == "Operation" {
			operation = strings.Split(line[1], " ")[2:]
		} else if line[0] == "Test" {
			test, _ = strconv.Atoi(strings.Split(line[1], " ")[2])
			cycleLength = cycleLength * test
		} else if line[0] == "If true" {
			ifTrue, _ = strconv.Atoi(strings.Split(line[1], " ")[3])
		} else if line[0] == "If false" {
			ifFalse, _ = strconv.Atoi(strings.Split(line[1], " ")[3])
			// create monkey knowing this is the last note
			m := newMonkey(items, operation, test, ifTrue, ifFalse)
			barrel = append(barrel, m)
		}
	}

	for i := 0; i < ROUND_LIMIT; i++ {
		doRound()
	}

	sort.Slice(barrel, func(i, j int) bool {
		return barrel[i].inspected > barrel[j].inspected
	})
	fmt.Println("Monkey business:", barrel[0].inspected*barrel[1].inspected)
}

func doRound() {
	for _, m := range barrel {
		for len(m.items) > 0 {
			item := m.items[0]
			// inspect item
			worryLevel := calcHighWorryLevel(item, m.operation)
			if worryLevel < item {
				fmt.Println("WORRY LEVELS OVERFLOWED")
			}
			worryLevel = worryLevel % cycleLength
			m.inspected++
			// throw item
			if worryLevel%m.test == 0 {
				barrel[m.ifTrue].items = append(barrel[m.ifTrue].items, worryLevel)
			} else {
				barrel[m.ifFalse].items = append(barrel[m.ifFalse].items, worryLevel)
			}
			m.items = m.items[1:]
		}
	}
}

func calcHighWorryLevel(oldLevel int, operator []string) int {
	var op1 int
	var op2 int
	if operator[0] == "old" {
		op1 = oldLevel
	} else {
		op1, _ = strconv.Atoi(operator[0])
	}
	if operator[2] == "old" {
		op2 = oldLevel
	} else {
		op2, _ = strconv.Atoi(operator[2])
	}
	if operator[1] == "+" {
		return op1 + op2
	} else {
		return op1 * op2
	}
}
