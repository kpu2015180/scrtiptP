import gmail

from tkinter import*
from tkinter import ttk


import framework
import pickle
import os
import folium
from selenium import webdriver

class readyTeleGram:
    def __init__(self):
        #self.window=Tk()
        #self.window.title('SearchState')
        #self.window.geometry('700x500')
        #Label(text="대피소",font=('Times New Roman',40)).pack()
        #mainloop()
        pass

    def enter(self):
        self.window = Tk()
        self.window.title('원 터치 벙커')
        self.window.geometry('300x300' )
        mainloop()
        framework.pop_state()
    def exit(self):
        pass
    def __del__(self):
        pass



