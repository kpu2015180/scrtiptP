from tkinter import*
import framework
import searchState
import bookMarkState
import pickle

class StartState:
    def goSearchState(self):
        self.window.destroy()
        framework.push_state(searchState.SearchState())
        pass
    def goBookMarkState(self):
        self.window.destroy()
        framework.push_state(bookMarkState.BookMarkState())

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
        
        Label(text="원 터치 벙커", font=('Times New Roman', 40)).pack()

        b = Button(self.window, text="지역검색", command=self.goSearchState, font=('Times New Roman', 15))
        b.place(x=100, y=130)

        d = Button(self.window, text="즐겨찾기", command=self.goBookMarkState, font=('Times New Roman', 15))
        d.place(x=100, y=200)
        mainloop()
        framework.quit()
    def exit(self):
        pass
