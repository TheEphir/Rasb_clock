from bs4 import BeautifulSoup
import requests
import cairosvg

def get_weather_img_url():
    w_url = "https://www.wunderground.com/hourly/ua/kyiv"
    markup = requests.get(w_url).text
    soup = BeautifulSoup(markup, features="html.parser")
    res = soup.find(name="div", class_="small-2 columns fct-icon").findChild("img")["src"]
    return res[6:]


img = get_weather_img_url()

print(img)