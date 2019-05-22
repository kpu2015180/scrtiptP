import requests
from bs4 import BeautifulSoup




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
hp = 'http://apis.data.go.kr/1741000/CivilDefenseShelter2/getCivilDefenseShelterList?ServiceKey='
key = '7kFbpf%2FOn4bEVGtr6DnsLs5DEx6AUme9vmgM57bnM18GtwgQgxtIOhtSuZfl%2FAVo1iHH76tjDOR%2FuvRryGOj%2FA%3D%3D'
numOfRows = '&numOfRows=1000'
pageNo = '&pageNo='  #1~18 까지 가능
type = '&type=xml'
flag = '&flag=Y'
for i in range(1,18):
    url = hp + key + pageNo + str(i) + type + numOfRows + flag
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.findAll('row')
    for item in items:
        s=item.find('sisul_addr').text
        s=s.split()
        if not s[0] in item_List.keys:
            item_List[s[0]]=dict()
        if not s[1] in item_List[s[0]].keys:
            item_List[s[0]][s[1]] = dict()
        if not s[2] in item_List[s[0]][s[1]].keys:
            item_List[s[0]][s[1]][s[2]] = []
        item_List[s[0]][s[1]][s[2]].append(Shelter(item.find('sisul_rddr').text, item.find('sisul_addr').text, item.find('facility_name').text,
                                                   item.find('longitude').text, item.find('latitude').text))



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




