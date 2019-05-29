from tkinter import*
from tkinter import ttk

import requests
from bs4 import BeautifulSoup

import framework
import pickle
import os
import folium
from selenium import webdriver

import gmail


class BookMarkState:
    def __init__(self):
        #self.window=Tk()
        #self.window.title('SearchState')
        #self.window.geometry('700x500')
        #Label(text="대피소",font=('Times New Roman',40)).pack()
        #mainloop()
        pass
    def deleteList(self):
        if self.listbox.size():
            n = self.listbox.curselection()
            shelter = framework.bookMarkList[n[0]]
            self.listbox.delete(n[0])
            framework.bookMarkList.remove(shelter)
        pass

    def sendMail(self):
        if self.listbox.size():
            n = self.listbox.curselection()
            shelter = framework.bookMarkList[n[0]]
            gmail.sendMail(shelter, self.e.get())

    def selectValue(self):
        if self.listbox.size():
            n=self.listbox.curselection()
            shelter=framework.bookMarkList[n[0]]
            i=shelter.rddr.index('(')
            self.l1.configure(text='시설명:'+str(shelter.facility_name)+'\n-도로명 주소-\n'+shelter.rddr[0:i]+'\n'+shelter.rddr[i:]+'\n-지번주소-\n'+shelter.addr)

            lat = float(shelter.latitude)
            lon = float(shelter.longtitude)
            map_osm = folium.Map(location=[lat, lon], zoom_start=17)
            folium.Marker([lat, lon], popup='Shild').add_to(map_osm)
            map_osm.save('ShildMap.html')
            tmpurl = 'file:///' + os.getcwd() + '/ShildMap.html'
            options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(chrome_options=options)
            driver.get(tmpurl)
            driver.save_screenshot("Shild.png")

            driver.close()
            Map = PhotoImage(file="Shild.png")
            self.L2.configure(image=Map)
            self.L2.image = Map
            pass

    def enter(self):
        self.window = Tk()
        self.window.title('SearchState')
        self.window.geometry('600x600' )

        Photo = PhotoImage(file="Map_Main.png")
        self.L2=Label(self.window,width=500,height=250,image=Photo,bg='white')  #지도
        self.L2.place(x=50,y=250)
        #----------------------------------------------------------------------------------
        self.l1=Label(self.window,width=70,height=7,bg='white')      #정보란
        self.l1.place(x=50,y=120)
        #--------------------------------------------------------------------------------------------
        Button(self.window,command=self.sendMail,width=16,height=2,text="메일 보내기",bg='green',font = ('현대하모니 L', 15, 'bold')).place(x=308,y=510) #메일 보내기 버튼
        self.e=Entry(self.window,width=30)
        self.e.place(x=88,y=530)
        #----------------------------------------------------
            # 검색 후 결과값을 출력하는 리스트 박스
        self.frame2=Frame(self.window,bg='white',width=400,height=100)
        self.frame2.place(x=50,y=15)
        self.scrollbar=Scrollbar(self.frame2)
        self.scrollbar.pack(side='right',fill="y")
        self.listbox=Listbox(self.frame2,width=45,height=5,borderwidth=7,relief='ridge',yscrollcommand=self.scrollbar.set)
        
        self.listbox.pack(side='left')
        self.scrollbar["command"]=self.listbox.yview
        i=0
        for item in framework.bookMarkList:
            self.listbox.insert(i,item.addr)
            i+=1
        #--------------------------------------------------------
        Button(self.window, command=self.selectValue, width=14, height=1, text="선택", bg='gray',   #결과 값 선택 버튼
               font=('현대하모니 L', 12, 'bold')).place(x=400, y=15)  # 즐겨찾기 버튼
        Button(self.window, command=self.deleteList, width=14, height=1, text="즐겨찾기 삭제", bg='gray', #즐겨찾기 버튼
               font=('현대하모니 L', 12, 'bold')).place(x=400, y=60)  # 즐겨찾기 버튼
        mainloop()
        framework.pop_state()
    def exit(self):
        pass
    def __del__(self):
        pass



