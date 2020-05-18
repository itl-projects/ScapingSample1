from bs4 import BeautifulSoup
import requests

def Scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def urls():
    urls =[]
    i = 0
    for a in range(0,6):
        i += 1
        string = "https://www.shopclues.com/mobiles-smartphones.html?&page=" + str(i)
        urls.append(string)
    return urls



def data():
    data=[]
    links = urls()
    for i in links:
        soupData = Scrape(i)
        for i in soupData.find_all('div'):
            if i.get('class') is None or i.get('class') == 'column col3':
                for x in i.find_all('span'):
                    if x.get('class') is not None or x.get('class') == 'p_price':
                        data.append(x.text)

    return data


print(data())