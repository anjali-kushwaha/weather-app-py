import tkinter
import requests
from bs4 import BeautifulSoup
from tkinter import Label, mainloop
from tkinter import Tk
from PIL import ImageTk,Image

url="https://weather.com/en-IN/weather/today/l/d884bf8e15624162758659a71e31e084981e92c367a7bfa15c345c9b92d688c4"

master =Tk()
master.title("weaher APP")
master.config(bg="white")

img =Image.open("img.png")
img =img.resize((150,150))
img =ImageTk.PhotoImage(img)

def getWeather():
    page =requests.get(url)
    soup =BeautifulSoup(page.content,"html.parser")
    location =soup.find('h1',class_="CurrentConditions--location--kyTeL").text
    temperature=soup.find("span",class_="CurrentConditions--tempValue--3a50n").text 
    weatherPrediction=soup.find("span",class_="CurrentConditions--tempValue--3a50n").text
   
    locationLable.config(text=location)


locationLable =Label(master,font=("Calibri bold",20),bg="white")
locationLable.grid(row=0,sticky="N",pady=100)

tempratureLable =Label(master,font=("Calibri bold",70),bg="white")
tempratureLable.grid(row=0,sticky="w",pady=40)

Label(master,image=img,bg="white").grid(row=1,sticky="E")

weatherPredictionLable = Label(master,font=("Calibri bold",15),bg="white")
weatherPredictionLable.grid(row=2,sticky="w",padx=40)

getWeather()
master.mainloop()

