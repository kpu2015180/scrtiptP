from tkinter import*
from tkinter import ttk
import framework
import pickle
name=['구로구','양천구','강북구','서남구']
class SearchState():
    def __init__(self):
        #self.window=Tk()
        #self.window.title('SearchState')
        #self.window.geometry('700x500')
        #Label(text="대피소",font=('Times New Roman',40)).pack()
        #mainloop()
        pass
    def searchD(self):
        pass
    def searchA(self):
        pass
    def addList(self):
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
        self.window.geometry('600x700' )
        f=open('시도구','rb')
        self.dic=pickle.load(f)
        f.close()

        self.start=False

        self.str1=StringVar()
        self.str2 = StringVar()
        self.str3 = StringVar()

        self.c1=ttk.Combobox(self.window,textvariable=self.str1,width=15,height=30,postcommand=self.func1,values=list(self.dic.keys()))
        self.c1.place(x=20,y=30)
        self.c1.set("시/도")

        self.c2 = ttk.Combobox(self.window,textvariable=self.str2, width=15, height=30,postcommand=self.func2)
        self.c2.place(x=170, y=30)
        self.c2.set("구/군")

        self.c3 = ttk.Combobox(self.window, textvariable=self.str3,width=15, height=30,postcommand=self.func3)
        self.c3.place(x=320, y=30)
        self.c3.set("읍/면/동")

        self.e1=Entry(self.window,width=50)
        self.e1.place(x=70,y=70)
        self.start=True
        Button(self.window,command=self.searchA,text="  지역검색  ",bg="red",font = ('현대하모니 L', 10, 'bold')).place(x=470,y=25)
        Button(self.window, command=self.searchD, text="  직접검색  ",bg='yellow',font = ('현대하모니 L', 10, 'bold')).place(x=470, y=65)
        self.frame=Frame(self.window,width=500,height=190,bg='white') #막대 그래프 그릴 프레입
        self.frame.place(x=50,y=100)
        #----------------------------------------------------------------------------------
        self.l1=Label(self.window,width=40,height=15,bg='white')      #지도
        self.l1.place(x=50,y=310)
        self.l2=Label(self.window,width=29,height=10,bg='white')      #선택된 대피소 정보란
        self.l2.place(x=345,y=310)
        Button(self.window,command=self.addList,width=16,height=2,text="즐겨찾기 추가",bg='green',font = ('현대하모니 L', 15, 'bold')).place(x=348,y=475) #즐겨찾기 버튼
        #----------------------------------------------------

        self.frame2=Frame(self.window,bg='white',width=380,height=100)
        self.frame2.place(x=50,y=550)
        self.scrollbar=Scrollbar(self.frame2)
        self.scrollbar.pack(side='left',fill="y")
        #self.listbox=Listbox(self.window,yscrollcommand=)
        mainloop()
        framework.pop_state()
    def exit(self):
        pass
    def __del__(self):
        pass



