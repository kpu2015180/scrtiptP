from tkinter import*
import framework
import searchState
import bookMarkState
import pickle
import teleGram
class StartState:
    def goSearchState(self):
        self.window.destroy()
        framework.push_state(searchState.SearchState())
        pass
    def goBookMarkState(self):
        self.window.destroy()
        framework.push_state(bookMarkState.BookMarkState())
    def TeleGramState(self):
        self.window.destroy()
        framework.push_state(teleGram.readyTeleGram())
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



        label=Label(self.window,text="원 터치 벙커", font=('Times New Roman', 40),bg='white')
        label.img =PhotoImage(file ='Shild_Main_Map.png')
        label.config(image=label.img,compound='bottom')
        label.pack()

        Start=PhotoImage(file='Start_icon.png')
        b = Button(label,command=self.goSearchState ,width=100,height=40,image=Start)
        b.place(x=95, y=60)
        BookmarkStart = PhotoImage(file='bookmark_Start.png')
        d = Button(label, text="즐겨찾기", command=self.goBookMarkState,width=140,height=40,image=BookmarkStart)
        d.place(x=0, y=250)
        TelegramStart = PhotoImage(file='Telegram_icon.png')
        tb=Button(label,text="텔레그렘",command=self.TeleGramState,width=145,height=40,image=TelegramStart)
        tb.place(x=145,y=250)
        mainloop()
        framework.quit()
    def exit(self):
        pass
