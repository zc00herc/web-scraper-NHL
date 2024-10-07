from bs4 import BeautifulSoup
import lxml
import requests
import pandas

URL = "https://www.naturalstattrick.com/playerteams.php?fromseason=20202021&thruseason=20202021&stype=2&sit=5v5&score=all&stdoi=oi&rate=n&team=ALL&pos=S&loc=B&toi=0&gpfilt=none&fd=&td=&tgp=410&lines=single&draftteam=ALL"
start = 0
table= []

df = pandas.read_html(URL,header=0,index_col=0,na_values=["-"])[0]
print(df)
