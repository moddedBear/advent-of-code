package main

import (
	"bufio"
	"fmt"
	"os"

	mapset "github.com/deckarep/golang-set/v2"
)

func main() {
	filename := os.Args[1]

	file, err := os.Open(filename)
	if err != nil {
		fmt.Printf("Couldn't open %v\n", filename)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var lookback []rune
	var set mapset.Set[rune]
	for scanner.Scan() {
		line := []rune(scanner.Text())
		beginning := 13
		for i := 0; i < len(line); i++ {
			beginning++
			lookback = line[i : i+14]
			set = mapset.NewThreadUnsafeSet(lookback...)
			if set.Cardinality() == 14 {
				println(beginning)
				break
			}
		}
	}
}
