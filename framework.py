import requests
from bs4 import BeautifulSoup
import pickle

class Shelter:
    def __init__(self,rddr,addr,fName,longtitude,latitude):
        self.rddr=rddr
        self.addr=addr
        self.facility_name=fName
        self.longtitude=longtitude
        self.latitude=latitude
        pass

running = None
stack = None
bookMarkList=[]



item_List=dict()
Graph_dict={"경기도":0,"서울특별시":0,"부산광역시":0,"제주특별자치도":0,"인천광역시":0,"전라남도":0,"대전광역시":0,
            "대구광역시":0,"경상북도":0,"경상남도":0,"울산광역시":0,"강원도":0,"충청남도":0,"전라북도":0,"충청북도":0
            ,"광주광역시":0,"세종특별자치시":0}
hp = 'http://apis.data.go.kr/1741000/CivilDefenseShelter2/getCivilDefenseShelterList?ServiceKey='
key = '7kFbpf%2FOn4bEVGtr6DnsLs5DEx6AUme9vmgM57bnM18GtwgQgxtIOhtSuZfl%2FAVo1iHH76tjDOR%2FuvRryGOj%2FA%3D%3D'
numOfRows = '&numOfRows=500'
pageNo = '&pageNo='  #1~18 까지 가능
type = '&type=xml'
flag = '&flag=Y'

#그래프 값 받고 0으로


for i in range(1,2):
    url = hp + key + pageNo + str(i) + type + numOfRows + flag
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.findAll('row')
    for item in items:
        s=item.find('sisul_addr').text
        s=s.split()
        if len(s) > 3:
            t1 = s[0]
            t2 = s[1]
            t3 = s[2]
            if not t1 in item_List.keys():
                item_List[t1]=dict()
            if not t2 in item_List[t1].keys():
                item_List[t1][t2] = dict()
            if not t3 in item_List[t1][t2].keys():
                item_List[t1][t2][t3] = list()
            item_List[t1][t2][t3].append(Shelter(item.find('sisul_rddr').text, item.find('sisul_addr').text, item.find('facility_name').text,
                                                    item.find('longitude').text, item.find('latitude').text))
            Graph_dict[t1] += 1



def change_state(state):
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].exit()
        # remove the current state
        stack.pop()
    stack.append(state)
    state.enter()



def push_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].exit()
    stack.append(state)
    state.enter()



def pop_state():
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].exit()
        # remove the current state
        stack.pop()

    # execute resume function of the previous state
    if (len(stack) > 0):
        stack[-1].enter()



def quit():
    global running
    running = False


def run(start_state):
    global running, stack
    running = True
    stack = [start_state]
    start_state.enter()


    while (running):
        pass
    # repeatedly delete the top of the stack
    while (len(stack) > 0):
        stack[-1].exit()
        stack.pop()
def save():
    f = open('즐겨찾기', 'wb')
    pickle.dump(bookMarkList,f)
    f.close()
    pass
def load():
    global bookMarkList
    f = open('즐겨찾기', 'rb')
    bookMarkList=pickle.load(f)
    f.close()
    pass



