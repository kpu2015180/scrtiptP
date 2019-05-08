from tkinter import*



class mainState:
    def goSearchState(self):
        self.exit()
        self.window.destroy()
        searchState()
        pass
    def goBookMarkState(self):

        pass
    def __init__(self):

        self.window=Tk()
        self.window.geometry('300x300')
        self.window.title('ShelterFinder')
        Label(text="대피소",font=('Times New Roman',40)).pack()

        b = Button(self.window, text="지역검색",command=self.goSearchState,font=('Times New Roman',15))
        b.place(x=100,y=130)


        d = Button(self.window, text="즐겨찾기", command=self.goBookMarkState, font=('Times New Roman', 15))
        d.place(x=100, y=200)




        mainloop()
        print(12)
    pass
    def exit(self):
       pass

class searchState():
    def __init__(self):
        self.window=Tk()
        self.window.title('SearchState')
        self.window.geometry('700x500')
        Label(text="대피소",font=('Times New Roman',40)).pack()



        mainloop()
        print(3)
    pass




mainState()