package main

import (
	"fmt"
	"time"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

func updateTime(clock *widget.Label) {
	var formatted string
	hour := time.Now().Hour()

	minute := time.Now().Minute()
	if minute < 10 {
		formatted = fmt.Sprintf("%v:0%v", hour, minute)
	} else {
		formatted = fmt.Sprintf("%v:%v", hour, minute)
	}

	clock.SetText(formatted)
}

func updateDate(curentDate *widget.Label) {
	yearDay := time.Now().YearDay()
	month := time.Now().Month()
	year := time.Now().Year()

	res := fmt.Sprintf("%v %v %v", yearDay, month, year)

	curentDate.SetText(res)
}

func main() {
	a := app.New()
	w := a.NewWindow("Clock")
	w.Resize(fyne.NewSize(800, 600))

	clock := widget.NewLabel("")
	clock.Resize(fyne.NewSize(800, 500))
	updateTime(clock)

	curentDate := widget.NewLabel("")
	curentDate.Move(fyne.NewPos(1, 500))
	updateDate(curentDate)

	w.SetContent(container.NewWithoutLayout(clock, curentDate))
	go func() {
		for range time.Tick(time.Minute) {
			updateTime(clock)
			updateDate(curentDate)
		}
	}()

	w.ShowAndRun()
}
