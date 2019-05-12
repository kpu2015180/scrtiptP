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

    def enter(self):
        self.window = Tk()
        self.window.title('SearchState')
        self.window.geometry('700x500')

        C1=ttk.Combobox(self.window,width=15,height=30,values=name)
        C1.place(x=30,y=50)
        C1.set("지역")

        C1 = ttk.Combobox(self.window, width=15, height=30, values=name)
        C1.place(x=30, y=50)
        C1.set("지역")

        C1 = ttk.Combobox(self.window, width=15, height=30, values=name)
        C1.place(x=30, y=50)
        C1.set("지역")
        #Label(self.window,text="대피소", font=('Times New Roman', 40)).pack()
        mainloop()
    def exit(self):
        self.window.destroy()
    def __del__(self):
        framework.pop_state()



