import requests
from tkinter import *
from bs4 import BeautifulSoup
from tkinter import Tk, Label, Frame, messagebox, Entry
from PIL import Image, ImageTk
from datetime import datetime

window = Tk()

window.title("Weather Forecasting Application")
window.config(bg="white")
window.geometry("700x450")


img = Image.open(r"C:\Users\sunda\OneDrive\Documents\CODSOFT_PROJECTS\Weather-1024.webp")
img = img.resize((150, 150))
photo = ImageTk.PhotoImage(img) 

image_label = Label(window, image=photo, bg="white")


title_label = Label(window, text="Weather Application", font=("calibri bold", 24), bg="white")


def get_weather_details():
    city = city_input.get()
    api_key = '8d1a9765e0d745c9800fe3a1194cec3a'
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
    if weather_data.status_code == 200:
        temp = weather_data.json()['main']['temp']
        humid = weather_data.json()['main']['humidity']
        wind_speed = weather_data.json()['wind']['speed']
        desc = weather_data.json()['weather'][0]['description']

        temp_field.insert(0, '{:.2f}'.format(temp) + " F")
        humid_field.insert(0, str(humid) + " %")
        wind_field.insert(0, '{:.2f}'.format(wind_speed) + " m/s")
        desc_field.insert(0, str(desc))
    else:
        messagebox.showerror("Error", "City Not Found. Enter a valid city name")
        city_input.delete(0, END)


def reset():
    city_input.delete(0, END)
    humid_field.delete(0, END)
    wind_field.delete(0, END)
    desc_field.delete(0, END)
    temp_field.delete(0, END)


border_color = "royal blue4"
border_width = 2

city_label = Label(window, text="Enter City Name : ", font=("calibri bold", 20),   highlightbackground=border_color, highlightcolor=border_color, highlightthickness=border_width)
city_input = Entry(window, width=24, font=12, relief=GROOVE, bd=3,   highlightbackground="black", highlightcolor="black", highlightthickness=1)

btn_submit = Button(window, text="Get Weather", width=10, font=12, bg="lime green", command=get_weather_details)
btn_reset = Button(window, text="Reset", width=10, font=12, bg="lime green", command=reset)

temp_label = Label(window, text="Temperature : ", font=("calibri bold", 20),   highlightbackground=border_color, highlightcolor=border_color, highlightthickness=border_width)
humid_label = Label(window, text="Humidity : ", font=("calibri bold", 20),    highlightbackground=border_color, highlightcolor=border_color, highlightthickness=border_width)
wind_label = Label(window, text="Wind Speed : ", font=("calibri bold", 20),   highlightbackground=border_color, highlightcolor=border_color, highlightthickness=border_width)
desc_label = Label(window, text="Description : ", font=("calibri bold", 20),   highlightbackground=border_color, highlightcolor=border_color, highlightthickness=border_width)


temp_field = Entry(window, width=24, font=12, bd=3,   highlightbackground="black", highlightcolor="black", highlightthickness=1)
humid_field = Entry(window, width=24, font=12, bd=3,    highlightbackground="black", highlightcolor="black", highlightthickness=1)
wind_field = Entry(window, width=24, font=12, bd=3,   highlightbackground="black", highlightcolor="black", highlightthickness=1)
desc_field = Entry(window, width=24, font=12, bd=3,   highlightbackground="black", highlightcolor="black", highlightthickness=1)


title_label.grid(row=0, column=0, columnspan=3, pady=(20, 10), sticky="NSEW")
image_label.grid(row=1, column=0, columnspan=3, pady=10, sticky="NSEW")

city_label.grid(row=2, column=0, padx=5, pady=5, sticky="E")
city_input.grid(row=2, column=1, padx=5, pady=5, columnspan=2, sticky="W")

btn_submit.grid(row=3, column=0, padx=5, pady=5, sticky="E")
btn_reset.grid(row=3, column=1, padx=5, pady=5, sticky="W")

temp_label.grid(row=4, column=0, padx=5, pady=5, sticky="E")
temp_field.grid(row=4, column=1, padx=5, pady=5, columnspan=2, sticky="W")

humid_label.grid(row=5, column=0, padx=5, pady=5, sticky="E")
humid_field.grid(row=5, column=1, padx=5, pady=5, columnspan=2, sticky="W")

wind_label.grid(row=6, column=0, padx=5, pady=5, sticky="E")
wind_field.grid(row=6, column=1, padx=5, pady=5, columnspan=2, sticky="W")

desc_label.grid(row=7, column=0, padx=5, pady=5, sticky="E")
desc_field.grid(row=7, column=1, padx=5, pady=5, columnspan=2, sticky="W")


for i in range(3):
    window.columnconfigure(i, weight=1)
for i in range(8):
    window.rowconfigure(i, weight=1)


window.image = photo

window.mainloop()
