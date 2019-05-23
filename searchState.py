from tkinter import*
from tkinter import ttk


import framework
import pickle
import os
import folium
from selenium import webdriver

class SearchState:
    def __init__(self):
        #self.window=Tk()
        #self.window.title('SearchState')
        #self.window.geometry('700x500')
        #Label(text="대피소",font=('Times New Roman',40)).pack()
        #mainloop()
        pass
    def searchA(self):
        t1 = self.str1.get()
        t2 = self.str2.get()
        if self.str1.get() == '시/도':
            return
        self.itemList.clear()
        if self.str3.get()!='읍/면/동':
            for i in framework.item_List[t1][t2][self.str3.get()]:
                self.itemList.append(i)
        elif self.str2.get() == '구/군':
            for i in framework.item_List[t1].keys():
                for j in framework.item_List[t1][i].keys():
                    for k in framework.item_List[t1][i][j]:
                        self.itemList.append(k)
        elif self.str3.get()=='읍/면/동':
            for i in framework.item_List[t1][t2].keys():
                for j in framework.item_List[t1][t2][i]:
                    self.itemList.append(j)


        self.updateListbox()
        pass
    def searchD(self):
        s=self.e1.get()
        s=s.split()
        if len(s)==0:
            return
        self.itemList.clear()
        if len(s)==3:
            if s[0] in framework.item_List.keys():
                if s[1] in framework.item_List[s[0]].keys():
                    if s[2] in framework.item_List[s[0]][s[1]].keys():
                        for i in framework.item_List[s[0]][s[1]][s[2]]:
                            self.itemList.append(i)
        elif len(s)==1:
            if s[0] in framework.item_List.keys():
                for i in framework.item_List[s[0]].keys():
                    for j in framework.item_List[s[0]][i].keys():
                        for k in framework.item_List[s[0]][i][j]:
                            self.itemList.append(k)

        elif len(s)==2:
            if s[0] in framework.item_List.keys():
                if s[1] in framework.item_List[s[0]].keys():
                    for i in framework.item_List[s[0]][s[1]].keys():
                        for j in framework.item_List[s[0]][s[1]][i]:
                            self.itemList.append(j)

        self.updateListbox()


        pass
    def addList(self):
        if self.listbox.size():
            n = self.listbox.curselection()
            shelter = self.itemList[n[0]]
            if not framework.bookMarkList.count(shelter):
                framework.bookMarkList.append(shelter)
            pass
    def sendMail(self):
        pass
    def selectValue(self):
        if self.listbox.size():
            n=self.listbox.curselection()
            shelter=self.itemList[n[0]]
            i=shelter.rddr.index('(')
            self.l1.configure(text='시설명:'+str(shelter.facility_name)+'\n-도로명 주소-\n'+shelter.rddr[0:i]+'\n'+shelter.rddr[i:]+'\n-지번주소-\n'+shelter.addr)
        map_osm = folium.Map(location=[shelter.latitude, shelter.longtitude], zoom_start=17)

        pass
    def updateListbox(self):
        i=0
        if self.listbox.size():
            self.listbox.delete(0,self.listbox.size())
        for item in self.itemList:
            self.listbox.insert(i,item.addr)
            i+=1
        pass
    def func1(self):
        self.c2.set('구/군')
        self.c3.set('읍/면/동')
    def func2(self):
        if self.start:
            self.c2.configure(values=list(self.dic[self.str1.get()].keys()))
            self.c2['values']=list(self.dic[self.str1.get()].keys())
            self.c3.set('읍/면/동')
        pass
    def func3(self):
        if self.start:
            if self.str1.get() != '시/도':
                self.c3.configure(values=list(self.dic[self.str1.get()][self.str2.get()]))
                self.c3['values'] = list(self.dic[self.str1.get()][self.str2.get()])
        pass
    def enter(self):
        self.window = Tk()
        self.window.title('SearchState')
        self.window.geometry('1200x700' )
        f=open('시도구','rb')
        self.dic=pickle.load(f)
        f.close()
        self.itemList=[]

        self.start=False

        self.str1=StringVar()
        self.str2 = StringVar()
        self.str3 = StringVar()

        self.c1=ttk.Combobox(self.window,textvariable=self.str1,width=13,height=30,postcommand=self.func1,values=list(self.dic.keys()))
        self.c1.place(x=50,y=30)                 # 시/도 콤보박스
        self.c1.set("시/도")

        self.c2 = ttk.Combobox(self.window,textvariable=self.str2, width=13, height=30,postcommand=self.func2)
        self.c2.place(x=190, y=30)              #구/군 콤보박스
        self.c2.set("구/군")

        self.c3 = ttk.Combobox(self.window, textvariable=self.str3,width=13, height=30,postcommand=self.func3)
        self.c3.place(x=330, y=30)              #읍/면/동 콤보박스
        self.c3.set("읍/면/동")

        self.e1=Entry(self.window,width=50)    #직접 검색란
        self.e1.place(x=70,y=70)
        self.start=True
        Button(self.window,command=self.searchA,text="  지역검색  ",bg="red",font = ('현대하모니 L', 10, 'bold')).place(x=470,y=25)
        Button(self.window, command=self.searchD, text="  직접검색  ",bg='yellow',font = ('현대하모니 L', 10, 'bold')).place(x=470, y=65)
        self.frame=Frame(self.window,width=500,height=190,bg='white') #막대 그래프 그릴 프레입
        self.frame.place(x=50,y=100)
        #----------------------------------------------------------------------------------
        self.l1=Label(self.window,width=40,height=15,bg='white')      #선택된 대피소 정보란
        self.l1.place(x=50,y=310)
        self.l2=Label(self.window,width=80,height=42,bg='white')      #지도
        self.l2.place(x=615,y=25)
        Button(self.window,command=self.sendMail,width=16,height=2,text="메일 보내기",bg='green',font = ('현대하모니 L', 15, 'bold')).place(x=348,y=415) #메일 보내기 버튼
        #----------------------------------------------------
            # 검색 후 결과값을 출력하는 리스트 박스
        self.frame2=Frame(self.window,bg='white',width=400,height=100)
        self.frame2.place(x=50,y=550)
        self.scrollbar=Scrollbar(self.frame2)
        self.scrollbar.pack(side='right',fill="y")
        self.listbox=Listbox(self.frame2,width=45,height=5,borderwidth=7,relief='ridge',yscrollcommand=self.scrollbar.set)
        
        self.listbox.pack(side='left')
        self.scrollbar["command"]=self.listbox.yview
        #--------------------------------------------------------
        Button(self.window, command=self.selectValue, width=14, height=1, text="선택", bg='gray',   #결과 값 선택 버튼
               font=('현대하모니 L', 12, 'bold')).place(x=400, y=550)  # 즐겨찾기 버튼
        Button(self.window, command=self.addList, width=14, height=1, text="즐겨찾기 추가", bg='gray', #즐겨찾기 버튼
               font=('현대하모니 L', 12, 'bold')).place(x=400, y=595)  # 즐겨찾기 버튼
        mainloop()
        framework.pop_state()
    def exit(self):
        pass
    def __del__(self):
        pass



