from tkinter import*
from tkinter import ttk
import framework
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
    def ma(self):
        print(12)
    def enter(self):
        self.window = Tk()
        self.window.title('SearchState')
        self.window.geometry('700x500')

        c1=ttk.Combobox(self.window,width=15,height=30,values=name)
        c1.place(x=70,y=50)
        c1.set("시")

        c2 = ttk.Combobox(self.window, width=15, height=30, values=name)
        c2.place(x=240, y=50)
        c2.set("군")

        c3 = ttk.Combobox(self.window, width=15, height=30, values=name, postcommand=self.ma)
        c3.place(x=410, y=50)
        c3.set("구")

        e1=Entry(self.window,width=50)
        e1.place(x=120,y=90)

        Button(self.window,command=self.searchA,text="  지역검색  ",bg="red").place(x=580,y=45)
        Button(self.window, command=self.searchD, text="  직접검색  ",bg='yellow').place(x=580, y=85)
        l1=Label(self.window,width=45,height=15,bg='white')
        l1.place(x=70,y=140)
        mainloop()
    def exit(self):
        self.window.destroy()
    def __del__(self):
        framework.pop_state()



