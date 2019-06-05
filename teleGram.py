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
        today = date.today()
        current_month = today.strftime('%Y%m')

        print('[', today, ']received token :', noti.TOKEN)

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

        if len(args) == 0:
            return

        if len(args) == 3:
            if args[0] in framework.item_List.keys():
                if args[1] in framework.item_List[args[0]].keys():
                    if args[2] in framework.item_List[args[0]][args[1]].keys():
                        for i in framework.item_List[args[0]][args[1]][args[2]]:
                            noti.sendMessage(chat_id, '{0}'.format(i.rddr))
        elif len(args) == 1:
            if args[0] in framework.item_List.keys():
                for i in framework.item_List[args[0]].keys():
                    for j in framework.item_List[args[0]][i].keys():
                        for k in framework.item_List[args[0]][i][j]:
                            noti.sendMessage(chat_id, '{0}'.format(i.rddr))

        elif len(args) == 2:
            if args[0] in framework.item_List.keys():
                if args[1] in framework.item_List[args[0]].keys():
                    for i in framework.item_List[args[0]][args[1]].keys():
                        for j in framework.item_List[args[0]][args[1]][i]:
                            noti.sendMessage(chat_id, '{0}'.format(i.rddr))
        else:
            noti.sendMessage(chat_id, '모르는 명령어입니다.\n시/도 구 동을 입력하세요.')


        noti.sendMessage(chat_id, '대피소를 찾는중입니다.')




