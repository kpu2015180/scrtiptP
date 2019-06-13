import gmail

from tkinter import*
from tkinter import ttk
#텔레그렘
import noti
import telepot
import time
from pprint import pprint
from datetime import date, datetime, timedelta

import framework
import pickle
import os
import folium
from selenium import webdriver

class readyTeleGram:
    def __init__(self):
        #self.window=Tk()
        #self.window.title('SearchState')
        #self.window.geometry('700x500')
        #Label(text="대피소",font=('Times New Roman',40)).pack()
        #mainloop()
        pass

    def enter(self):
        self.window = Tk()
        self.window.title('원 터치 벙커')
        self.window.geometry('300x300' )

        label = Label(self.window,bg='white')
        label.img = PhotoImage(file='Telegram_Main.png')
        label.config(image=label.img, compound='bottom')
        label.pack()



        bot = telepot.Bot(noti.TOKEN)
        pprint(bot.getMe())

        bot.message_loop(self.handle)
        mainloop()
        framework.pop_state()
    def exit(self):
        pass
    def __del__(self):
        pass

    def handle(self,msg):
        # 텔레그램에서 메세지를 캐치
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type != 'text':
            noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
            return

        text = msg['text']
        args = text.split(' ')
        print_cheak=False
        #if len(args) == 0:
            #return

        if len(args) == 3:
            if args[0] in framework.item_List.keys():
                if args[1] in framework.item_List[args[0]].keys():
                    if args[2] in framework.item_List[args[0]][args[1]].keys():
                        for i in framework.item_List[args[0]][args[1]][args[2]]:
                            map = 'https://www.google.com/search?q={0}+{1}&oq={0}+{1}&aqs=chrome..69i57.341j0j9&sourceid=chrome&ie=UTF-8'.format(
                                i.latitude, i.longtitude)
                            noti.sendMessage(chat_id, '{0}\n{1}\n{2}\n'.format(i.facility_name, i.rddr, map))
                            print_cheak = True
        elif len(args) == 1:
            if args[0] in framework.item_List.keys():
                for i in framework.item_List[args[0]].keys():
                    for j in framework.item_List[args[0]][i].keys():
                        for k in framework.item_List[args[0]][i][j]:
                            map = 'https://www.google.com/search?q={0}+{1}&oq={0}+{1}&aqs=chrome..69i57.341j0j9&sourceid=chrome&ie=UTF-8'.format(k.latitude,k.longtitude)
                            noti.sendMessage(chat_id, '{0}\n{1}\n{2}\n'.format(k.facility_name,k.rddr,map))
                            print_cheak = True

        elif len(args) == 2:
            if args[0] in framework.item_List.keys():
                if args[1] in framework.item_List[args[0]].keys():
                    for i in framework.item_List[args[0]][args[1]].keys():
                        for j in framework.item_List[args[0]][args[1]][i]:
                            map = 'https://www.google.com/search?q={0}+{1}&oq={0}+{1}&aqs=chrome..69i57.341j0j9&sourceid=chrome&ie=UTF-8'.format(
                                j.latitude, j.longtitude)
                            noti.sendMessage(chat_id, '{0}\n{1}\n{2}\n'.format(j.facility_name, j.rddr, map))
                            print_cheak=True

        if(print_cheak==False):
            noti.sendMessage(chat_id, '없는 지역입니다.\n시/도 구 동을 입력하세요.')


        elif(print_cheak==True):
            noti.sendMessage(chat_id, "찾은 대피소를 출력하였습니다.")
            print_cheak=False




