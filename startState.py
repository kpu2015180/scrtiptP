from tkinter import*
import framework
import searchState


class StartState:
    def goSearchState(self):

        framework.push_state(searchState.SearchState())
        pass
    def goBookMarkState(self):
        self.exit()
        self.window.destroy()

        pass
    def __init__(self):

        #self.window=Tk()
        #self.window.geometry('300x300')
        #self.window.title('ShelterFinder')
        #Label(text="대피소",font=('Times New Roman',40)).pack()

        #b = Button(self.window, text="지역검색",command=self.goSearchState,font=('Times New Roman',15))
        #b.place(x=100,y=130)


        #d = Button(self.window, text="즐겨찾기", command=self.goBookMarkState, font=('Times New Roman', 15))
        #d.place(x=100, y=200)
        pass





    def enter(self):
        self.window = Tk()
        self.window.geometry('300x300')
        self.window.title('StartState')
        Label(text="대피소", font=('Times New Roman', 40)).pack()

        b = Button(self.window, text="지역검색", command=self.goSearchState, font=('Times New Roman', 15))
        b.place(x=100, y=130)

        d = Button(self.window, text="즐겨찾기", command=self.goBookMarkState, font=('Times New Roman', 15))
        d.place(x=100, y=200)
        mainloop()

    def exit(self):
        self.window.destroy()
        pass
