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

        c3 = ttk.Combobox(self.window, width=15, height=30, values=name)
        c3.place(x=410, y=50)
        c3.set("구")

        
        Button(self.window,command=self.searchD,text="  검색  ").place(x=580,y=45)

        #Label(self.window,text="대피소", font=('Times New Roman', 40)).pack()
        mainloop()
    def exit(self):
        self.window.destroy()
    def __del__(self):
        framework.pop_state()



