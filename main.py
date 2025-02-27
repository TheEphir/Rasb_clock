# DARK MODE

import tkinter as tk
from datetime import datetime
import calendar
import requests

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d/%m")
    current_weekday = calendar.day_name[datetime.now().weekday()]
    
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    weekday_label.config(text=current_weekday[:3])
    
    root.after(1000, update_time)
    
def update_weather():
    try:
        weather = requests.get(url="https://wttr.in/kyiv", params="format=1").text
    except:
        weather = "❌"
    
    res = f"{weather[0]}\n{weather[5:]}"
    weather_label.config(text=res)
    root.after(3600000, update_weather)
    

root = tk.Tk()
root.title("Часы")
root.geometry("1000x550")
root.resizable(True, True)
root.config(background="#404040")

font_time = ("Helvetica", 190, "bold") 
font_date = ("Helvetica", 80)
font_weather = ("Helvetica", 60)


time_label = tk.Label(root, font=font_time, fg="black")
time_label.pack()
time_label.config(background="#404040")

frame = tk.Frame(root)
frame.pack()

date_label = tk.Label(frame, font=font_date, fg="black")
date_label.pack(side=tk.LEFT)
date_label.config(background="#404040", highlightcolor="#404040")

weekday_label = tk.Label(frame, font=font_date, fg="black")
weekday_label.pack(side=tk.LEFT, padx=80)
weekday_label.config(background="#404040")

weather_label = tk.Label(frame, font=font_weather, fg="black")
weather_label.pack(side=tk.LEFT, padx=20)

update_time()
update_weather()

root.mainloop()