import tkinter as tk
import requests
import cairosvg
from PIL import Image, ImageTk
from io import BytesIO
from bs4 import BeautifulSoup

IMAGES = [
    "https://static.vecteezy.com/system/resources/previews/008/296/267/non_2x/colorful-swirl-logo-design-concept-illustration-vector.jpg",
    "https://img.freepik.com/free-vector/bird-colorful-logo-gradient-vector_343694-1365.jpg",
    "https://png.pngtree.com/png-clipart/20190611/original/pngtree-wolf-logo-png-image_2306634.jpg",
    "https://img.freepik.com/free-vector/quill-pen-logo-template_23-2149852429.jpg?semt=ais_hybrid",
    ]

INDEX = 0

def update_weather_img_url():
    w_url = "https://www.wunderground.com/hourly/ua/kyiv"
    try:
        markup = requests.get(w_url).text
        soup = BeautifulSoup(markup, features="html.parser")
        res = soup.find(name="div", class_="small-2 columns fct-icon").findChild("img")["src"]
        svg_data = requests.get(f"http://{res [6:]}").content
        png_image = cairosvg.svg2png(svg_data)
        png_bytes = BytesIO(png_image)
        image = Image.open(png_bytes)
    except:
        image = Image.open("./a.jpg")
    return image



def test():
    try:
        w_url = "https://www.wunderground.com/hourly/ua/kyiv"
        markup = requests.get(w_url).text
        soup = BeautifulSoup(markup, features="html.parser")
        res = soup.find(name="div", class_="small-2 columns fct-icon").findChild("img")["src"]
        img_url = f"http://{res [6:]}" 
        png_image = cairosvg.svg2png(url=img_url)
        png_bytes = BytesIO(png_image)
        image = Image.open(png_bytes)
        return ImageTk.PhotoImage(image)
        #weather_img_label.config(image=tk_image)
    except:
        return


root = tk.Tk()

root.title("Часы")
root.geometry("1000x550")
root.resizable(True, True)

png_image = cairosvg.svg2png(url=update_weather_img_url())
tk_image = ImageTk.PhotoImage(update_weather_img_url())

weather_img_label = tk.Label(root, image=tk_image)
weather_img_label.pack()

#test()

root.mainloop()

