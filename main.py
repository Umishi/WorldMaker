# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:39:43 2021

@author: Kaito Takasugi
"""
import random
import tkinter
from PIL import ImageTk


window = tkinter.Tk()
window.geometry("1280x960")
window.title("World_Settings")


window.canvas = tkinter.Canvas(window)
window.canvas.pack(
    expand = True,
    fill = tkinter.BOTH
    )

window.photo_image_1 = ImageTk.PhotoImage(file = "Title.png")
window.photo_image_2 = ImageTk.PhotoImage(file = "Result.png")

window.update()
canvas_width = window.canvas.winfo_width()
canvas_height = window.canvas.winfo_height()

window.canvas.create_image(
    canvas_width / 2,
    canvas_height / 2,
    image=window.photo_image_1
        
    )



def wordchoice():

 read = open("wordlist.txt", "r", encoding="utf-8")
 word_list = read.readlines()
 window.canvas.create_image(
    canvas_width / 2,
    canvas_height / 2,
    image=window.photo_image_2        
    )
            
 n = 3
 final_list = []
               
 final_list = random.sample(word_list, n)  
                     
 label_1 = tkinter.Label(
         window,
         font = ("System","50"),  
         background = "#ffffff",
         foreground = "#708090",
         text = final_list[0].replace("\n","")
                     )
 label_1.place(
         x = 190,
         y = 740, 
                     )
 label_2 = tkinter.Label(
         window,
         font = ("System","50"), 
         background = "#ffffff",
         foreground = "#708090",
         text = final_list[1].replace("\n","")
                     )
 label_2.place(
         x = 520,
         y = 740, 
                     )
 label_3 = tkinter.Label(
         window,
         font = ("System","50"),  
         background = "#ffffff",
         foreground = "#708090",
         text = final_list[2].replace("\n","")
                     )
 label_3.place(
         x = 850,
         y = 740, 
                     )
 def erace():
    label_1.place_forget()
    label_2.place_forget()
    label_3.place_forget()
    
    
 button_1.place_forget()
 button_2 = tkinter.Button(
     window,
    text = "実行",
    font = ("System","30"),
    foreground = "#ffffff",
    activeforeground = "#ffffff",
    background = "#708090",
    activebackground = "#add8e6",
    command = lambda:[erace(),wordchoice()]
    )
 button_2.place(
    x = 1050,
    y = 520,   
    )
    
 read.close()
 

    

button_1 = tkinter.Button(
    window,
    text = "実行",
    font = ("System","30"),
    foreground = "#ffffff",
    activeforeground = "#ffffff",
    background = "#708090",
    activebackground = "#add8e6",
    command = wordchoice
    )
button_1.place(
    x = 1050,
    y = 520,   
    )


            
window.mainloop()
