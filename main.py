import tkinter as tk
from datetime import datetime
import calendar
import requests


def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d/%m")
    current_weekday = calendar.day_name[datetime.now().weekday()]

    res = int(current_time[:2])
    to_dark_mode(res)

    time_label.config(text=current_time)
    date_label.config(text=current_date)
    weekday_label.config(text=current_weekday[:3])
        
    root.after(1000, update_time)
    
    
def update_weather():
    try:
        weather = requests.get(url="https://wttr.in/kyiv", params="format=1").text
        res = f"\n{weather[5:]}"
    except:
        res = "❌"
    
    weather_label.config(text=res)
    root.after(3600000, update_weather)
    
    
def to_dark_mode(res):
    if res >= 13 or res <=7:
        root.config(background="#404040")
        time_label.config(background="#404040")
        frame.config(background="#404040")
        date_label.config(background="#404040")
        weekday_label.config(background="#404040")
        weather_label.config(background="#404040")
    else:        
        root.config(background="#ffffff")
        time_label.config(background="#ffffff")
        frame.config(background="#ffffff")
        date_label.config(background="#ffffff")
        weekday_label.config(background="#ffffff")
        weather_label.config(background="#ffffff")
        
        
    
root = tk.Tk()
root.title("Clock")
root.geometry("1000x550")
root.resizable(True, True)

font_time = ("Helvetica", 190, "bold") 
font_date = ("Helvetica", 90)
font_weather = ("Helvetica", 90)


time_label = tk.Label(root, font=font_time, fg="black")
time_label.pack()

# ===================== BOTTOM THINGS ========================
frame = tk.Frame(root)
frame.pack()

date_label = tk.Label(frame, font=font_date, fg="black")
date_label.pack(side=tk.LEFT)

weekday_label = tk.Label(frame, font=font_date, fg="black")
weekday_label.pack(side=tk.LEFT, padx=80)

weather_label = tk.Label(frame, font=font_weather, fg="black")
weather_label.pack(side=tk.LEFT, padx=20)

update_time()
update_weather()

root.mainloop()