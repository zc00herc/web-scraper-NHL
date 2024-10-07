import pandas
from tkinter import *

# URL Parameters
fromseason = 20202021
thruseason = 20202021
# 1 = preseason, 2 = Regular Season, 3 = playoffs
seasontype = 3
# All Strengths = all, Even Strength = ev, 5v5, 5v5 Score & Venue Adjusted = sva, Power Play=pp, 5 on 4 PP=5v4, Penalty Kill=pk, 4 on 5 PK=4v5, 3 on 3=3v3, With Empty Net=enf, Against Empty Net=ena
situation = 'pp'
# All=all, Tied=tied, Leading=u, Trailing=d, Within 1=w1, Up 1=u1, Down 1=d1
score = 'all'
# Goalie = g, individual = std, bios = bio, on-ice = oi
statgroup = 'std'
# Counts = n, rates = y, relative = r
rate = 'n'
# All = ALL, Anaheim = ANA, Atlanta = ATL, Boston = BOS, Carolina = CAR, Columbus = CBJ, Calgary = CGY, Chicago = CHI
# Colorado = COL, Dallas = DAL, Detroit = DET, Edmonton = EDM, Florida = FLA, Hartford = HFD, Los Angeles = LA
# Minnesota = MIN, Montreal = MTL, Nashville = NAS, New Jersey = NJ, NY Islanders = NYI, NY Rangers = NYR
# Ottawa = OTT, Philadelphia = PHI, Phoenix = PHX, Pittsburgh = PIT, Quebec = QUE, San Jose = SJ, St. Louis = STL
# Tampa Bay = TB, Toronto = TOR, Vancouver = VAN, Winnipeg = WPG, Washington = WSH
team = 'WPG'
# Skaters = S, Forwards = F, Center = C, Left Wing = L, Right Wing = R, Defensemen = D, Goalie = G
position = 'S'
# Home and Away = B, Home = H, Away = A
location = 'B'
# sets min time on ice to be included
toi = 0
# game range. None = none -> means all time, By Date = gpdate, games played team = gpteam.
# If by date, fd and td below need to be filled with from date and to date respectively
# or by games played team and tgp needs to be filled with number of team games
gpfilt = 'none'
fd = ''
td  = ''
tgp = ''
# splits players out by team they are playing for if they played for multiple teams
# Combine = single, Split = multi
lines = 'single'
# same list as above
draftteam = 'ALL'

# Lists
situations = ["All Strengths","Even Strength","5v5, 5v5 Score & Venue Adjusted","Power Play","5 on 4 PP=5v4, Penalty Kill","4 on 5 PK","3 on 3","With Empty Net","Against Empty Net"]
statgroups = ["Goalie", "Individual", "Bios", "On-ice"]
teams = ["All","Anaheim","Atlanta","Boston","Carolina","Columbus","Calgary","Chicago","Colorado","Dallas",
         "Detroit","Edmonton","Florida","Hartford","Los Angeles","Minnesota","Montreal","Nashville",
         "New Jersey","NY Islanders","NY Rangers","Ottawa","Philadelphia","Phoenix","Pittsburgh",
         "Quebec","San Jose","St. Louis","Tampa Bay","Toronto","Vancouver","Winnipeg","Washington"]
seasonyears = [2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
scores = ["All", "Tied", "Leading", "Trailing", "Within 1", "Up 1", "Down 1"]
positions = ["Skaters", "Forwards", "Center", "Left Wing", "Right Wing", "Defensemen", "Goalie"]

def radio_used():
    print(radio_state.get())

def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

def fetch_data():
    url = 'http://www.naturalstattrick.com/playerteams.php?fromseason={}&thruseason={}&stype={}&sit={}&score={}&stdoi={}&rate={}&team={}&pos={}&loc={}&toi={}&gpfilt={}&fd={}&td={}td&tgp={}&lines={}&draftteam={}'.format(
        fromseason, thruseason, seasontype, situation, score, statgroup, rate, team, position, location, toi, gpfilt,
        fd, td, tgp, lines, draftteam)
    df = pandas.read_html(url,header=0,index_col=0,na_values=["-"])[0]
    print(df)

window = Tk()
window.title("Data Selection")
window.config(width=500,height=500)

#Labels
fromseason = Label(text="From Season: ")
fromseason.grid(column=0,row=0)
toseason = Label(text="To Season: ")
toseason.grid(column=0,row=1)
seasontype = Label(text="Season Type: ")
seasontype.grid(column=0,row=3)
situation = Label(text="Situation: ")
situation.grid(column=0,row=4)
score = Label(text="Score: ")
score.grid(column=0,row=5)
statgroup = Label(text="Stat Groups: ")
statgroup.grid(column=0,row=6)
rate = Label(text="Rate: ")
rate.grid(column=0,row=7)
team = Label(text="Team: ")
team.grid(column=0,row=8)
position = Label(text="Position: ")
position.grid(column=0,row=9)
location = Label(text="Location: ")
location.grid(column=0,row=10)
toi = Label(text="TOI: ")
toi.grid(column=0,row=11)
range = Label(text="Data Range Type: ")
range.grid(column=0,row=12)
fromdate = Label(text="From Date: ")
fromdate.grid(column=0,row=13)
todate = Label(text="To Date: ")
todate.grid(column=0,row=14)
teamgamesplayed = Label(text="Team Games Played: ")
teamgamesplayed.grid(column=0,row=15)
multipleteams = Label(text="Total or Split: ")
multipleteams.grid(column=0,row=16)
draftteam = Label(text="Draft Team: ")
draftteam.grid(column=0,row=17)

#Data Entry
# Drop Downs
listbox = OptionMenu(window,StringVar(),*seasonyears)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=1,row=0)

listbox = OptionMenu(window,StringVar(),*seasonyears)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=1,row=1)

listbox = OptionMenu(window,StringVar(),*scores)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=1,row=5)

listbox = OptionMenu(window,StringVar(),*situations)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=1,row=4)

listbox = OptionMenu(window,StringVar(),*statgroups)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=1,row=6)

listbox = OptionMenu(window,StringVar(),*teams)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=1,row=8)

listbox = OptionMenu(window,StringVar(),*positions)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=1,row=9)



listbox = OptionMenu(window,StringVar(),*teams)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=1,row=17)


# Radio Buttons
radio_state = IntVar()
seasontype1 = Radiobutton(text="Pre Season", value=1, variable=radio_state, command=radio_used)
seasontype2 = Radiobutton(text="Regular Season", value=2, variable=radio_state, command=radio_used)
seasontype3 = Radiobutton(text="Playoffs", value=2, variable=radio_state, command=radio_used)
seasontype1.grid(column=1,row=3)
seasontype2.grid(column=2,row=3)
seasontype3.grid(column=3,row=3)

rate1 = Radiobutton(text="Count", value=1, variable=radio_state, command=radio_used)
rate2 = Radiobutton(text="Rate", value=2, variable=radio_state, command=radio_used)
rate3 = Radiobutton(text="Relative", value=2, variable=radio_state, command=radio_used)
rate1.grid(column=1,row=7)
rate2.grid(column=2,row=7)
rate3.grid(column=3,row=7)

location1 = Radiobutton(text="Home and Away", value=1, variable=radio_state, command=radio_used)
location2 = Radiobutton(text="Home", value=2, variable=radio_state, command=radio_used)
location3 = Radiobutton(text="Away", value=2, variable=radio_state, command=radio_used)
location1.grid(column=1,row=10)
location2.grid(column=2,row=10)
location3.grid(column=3,row=10)

range1 = Radiobutton(text="All time", value=1, variable=radio_state, command=radio_used)
range2 = Radiobutton(text="By Date", value=2, variable=radio_state, command=radio_used)
range3 = Radiobutton(text="Team Games Played", value=2, variable=radio_state, command=radio_used)
range1.grid(column=1,row=12)
range2.grid(column=2,row=12)
range3.grid(column=3,row=12)

split1 = Radiobutton(text="Group", value=1, variable=radio_state, command=radio_used)
split2 = Radiobutton(text="Split", value=2, variable=radio_state, command=radio_used)
split1.grid(column=1,row=16)
split2.grid(column=2,row=16)

#Entries
toi_entry = Entry(width=30)
#Add some text to begin with
toi_entry.insert(END, string="0")
#Gets text in entry
# print(entry.get())
toi_entry.grid(column=1,row=11)

tgp_entry = Entry(width=30)
#Add some text to begin with
tgp_entry.insert(END, string="0")
#Gets text in entry
# print(entry.get())
tgp_entry.grid(column=1,row=15)

# fromdate = Label(text="From Date: ")
# fromdate.grid(column=1,row=13)
# todate = Label(text="To Date: ")
# todate.grid(column=1,row=14)

# Button
submit = Button()
submit.config(text="Fetch Data",command=fetch_data)
submit.grid(column=0,row=18,columnspan=3)

# print(df)


window.mainloop()