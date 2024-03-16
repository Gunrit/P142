from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
#browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
page = requests.get(START_URL)
soup = BeautifulSoup(page.text,"html.parser")

starTable = soup.find('table')
templist = []
tablerows = starTable[7].find_all('tr')
for tr in tablerows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    templist.append(row)
star_names = []
distance = []
mass = []
radius = []
for i in range(1,len(templist)):
    star_names.append(templist[i][0])
    distance.append(templist[i][5])
    mass.append(templist[i][8])
    radius.append(templist[i][9])
df = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns = ['Star Names','distance','Mass','Radius'])
print(df)
df.to_csv('Stars.csv')