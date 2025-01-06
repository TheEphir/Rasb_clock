package main

import (
	"fmt"
	"time"
)

func main() {
	for {
		year := time.Now().Year()
		month := time.Now().Month()
		yearDay := time.Now().YearDay()
		fmt.Printf("%v %v %v\n", yearDay, month, year)

		hour := time.Now().Hour()
		minute := time.Now().Minute()

		fmt.Printf("%v:%v/n", hour, minute)

		time.Sleep(time.Second)
	}
}
