from bs4 import BeautifulSoup
import lxml
import requests
import pandas

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
statgroups = 'g'
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

URL = 'http://www.naturalstattrick.com/playerteams.php?fromseason={}&thruseason={}&stype={}&sit={}&score={}&stdoi={}&rate={}&team={}&pos={}&loc={}&toi={}&gpfilt={}&fd={}&td={}td&tgp={}&lines={}&draftteam={}'.format(
 fromseason, thruseason, seasontype, situation, score, statgroups, rate, team, position, location, toi, gpfilt, fd, td, tgp, lines, draftteam)

print(URL)

start = 0
table= []

df = pandas.read_html(URL,header=0,index_col=0,na_values=["-"])[0]
print(df)
