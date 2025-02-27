import tkinter as tk
from datetime import datetime
from bs4 import BeautifulSoup
import calendar
import requests
import cairosvg
from PIL import Image, ImageTk
from io import BytesIO


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
    
    w_url = "https://www.wunderground.com/hourly/ua/kyiv"
    try:
        markup = requests.get(w_url).text
        soup = BeautifulSoup(markup, features="html.parser")
        res = soup.find(name="div", class_="small-2 columns fct-icon").findChild("img")["src"]
        img_url = f"http://{res [6:]}" 
        png_image = cairosvg.svg2png(url=img_url)
        png_bytes = BytesIO(png_image)
        image = Image.open(png_bytes)
        tk_image = ImageTk.PhotoImage(image)
        weather_img_label.config(image=tk_image)
    except:
        weather_img_label.config(text="X")
    
    res = f"{weather[5:-2]}"
    weather_label.config(text=res)
    root.after(3600000, update_weather)
    

root = tk.Tk()

# def update_weather_img():
#     w_url = "https://www.wunderground.com/hourly/ua/kyiv"
#     try:
#         markup = requests.get(w_url).text
#         soup = BeautifulSoup(markup, features="html.parser")
#         res = soup.find(name="div", class_="small-2 columns fct-icon").findChild("img")["src"]
#         img_url = f"http://{res [6:]}" 
#         png_image = cairosvg.svg2png(url=img_url)
#         png_bytes = BytesIO(png_image)
#         image = Image.open(png_bytes)
#         tk_image = ImageTk.PhotoImage(image)
#         weather_img_label.config(image=tk_image)
#     except:
#         weather_img_label.config(text="X")
#     root.after(3600000, update_weather_img)
    
    
root.title("Часы")
root.geometry("1000x550")
root.resizable(True, True)

font_time = ("Helvetica", 190, "bold") 
font_date = ("Helvetica", 80)
font_weather = ("Helvetica", 80)

time_label = tk.Label(root, font=font_time, fg="black")
time_label.pack()

frame = tk.Frame(root)
frame.pack(pady=30)

date_label = tk.Label(frame, font=font_date, fg="#3b3b3b")
date_label.pack(side=tk.LEFT)

weekday_label = tk.Label(frame, font=font_date, fg="#3b3b3b")
weekday_label.pack(side=tk.LEFT, padx=40)

weather_img_label = tk.Label(frame, image=None)
weather_img_label.pack(side=tk.LEFT)

weather_label = tk.Label(frame, font=font_weather, fg="#3b3b3b")
weather_label.pack(side=tk.LEFT)

update_time()
update_weather()
# update_weather_img()

root.mainloop()

