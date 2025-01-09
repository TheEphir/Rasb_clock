package main

import (
	"image/color"
	"time"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/canvas"
	"fyne.io/fyne/v2/container"
)

func updateTime(curTime *canvas.Text) {
	curTime.Text = time.Now().Format("15:04:05")
	curTime.Refresh()
}

func main() {
	a := app.New()
	w := a.NewWindow("Clock test")
	w.Resize(fyne.NewSize(1024, 600))

	curTime := canvas.NewText(time.Now().Format("15:04:05"), color.Black)
	curTime.TextStyle = fyne.TextStyle{Symbol: true, Bold: true}
	curTime.TextSize = 250 // |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
	curTime.Move(fyne.NewPos(0, 0))

	curDate := canvas.NewText(time.Now().Format("Mon 02/Jan"), color.Black)
	curDate.TextSize = 60
	curDate.Move(fyne.NewPos(0, 400))

	w.SetContent(container.NewWithoutLayout(curTime, curDate))

	go func() {
		for {
			time.Sleep(time.Second)
			updateTime(curTime)
		}
	}()

	// cTime := time.Now().Format("15:04")
	// cDate := time.Now().Format("Mon 02/Jan")
	w.ShowAndRun()
}
