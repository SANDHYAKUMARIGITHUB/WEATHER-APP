import tkinter as tk
import requests
#from tkinter import font
from tkinter.constants import W
#from typing import Collection
from PIL import Image,ImageTk   #pip install pillow
root=tk.Tk()

root.title("WEATHER APP")
root.geometry("600x500")
#keys = cdc8ef406a2a0388db67f9c95b057ee8 
# API URL : api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def format_response(weather):
    try:
        city=weather['name']
        condition=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str='city:%s\nCondition:%s\nTemperature:%s'%(city,condition,temp)
    except:
        find_str="There was a problem retrieving that information"    
    return final_str    


def get_weather(city):
    weather_keys='cdc8ef406a2a0388db67f9c95b057ee8'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_keys,'q':city,'units':'imperial'}
    response=requests.get(url,params)
    #print(response.json())
    weather=response.json()
    #print(weather['name'])
    #print(weather['weather'][0]['description'])
    #print(weather['main']['temp'])

    result['text']=format_response(weather)

    
img=Image.open('./bg.png.jpeg')
img=img.resize((600,500),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)

bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

heading_title=tk.Label(bg_lbl,text='Earth including work 200,000 cities!',fg='brown',bg='white',font=('times new roman',18,'bold'))
heading_title.place(x=80,y=18)

frame_one=tk.Frame(bg_lbl,bg="#42c2f4",bd=5)
frame_one.place(x=80,y=70,width=470,height=50)

txt_box=tk.Entry(frame_one,font=('timesnnew roman',25),width=17)
txt_box.grid(row=0,column=0,sticky=W)

btn=tk.Button(frame_one,text='GET WEATHER',fg='dark green',font=('times nnew roman',12,'bold'),command=lambda: get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=10)

frame_two=tk.Frame(bg_lbl,bg="#42c2f4",bd=5)
frame_two.place(x=80,y=130,width=470,height=230)


result=tk.Label(frame_two,font=40,bg='white',justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)



root.mainloop()