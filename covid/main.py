import pync
import requests
from bs4 import BeautifulSoup
def getData(url):
    r=requests.get(url)
    return  r.text
if __name__ == '__main__':
    myHtmlData =getData('https://www.worldometers.info/coronavirus/country/india/')

    #print(myHtmlData)
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    #print(soup.prettify())
    cases=soup.find_all("div", class_="maincounter-number")[0]
    totalcase=cases.get_text()
    deaths=soup.find_all("div", class_="maincounter-number")[1]
    totaldeaths=deaths.get_text()
    recovered=soup.find_all("div", class_="maincounter-number")[2]
    totalrecoverd=recovered.get_text()
    print((totalrecoverd))

notification_title="Covid-19 Status (Source: worldometer)"
notification_text=f"Total Case:{totalcase} \n Deaths : {totaldeaths} \n Recovered : {totalrecoverd}"
pync.notify("Let's stop virus together", title="COVID daily report",  execute='say "Covid is spreading and you should take care and dont go outside"')
pync.notify(notification_text,title="Covid-19 Status (Source: worldometer)",open='http://localhost:3000/')
#https://www.worldometers.info/coronavirus/country/india/




