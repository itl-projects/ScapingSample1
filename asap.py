 from bs4 import BeautifulSoup
import requests
import datetime


def Soup(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # return soup
    except:
        with open('exceptions.txt', 'a') as File:
            now = datetime.datetime.now()
            str = f"Could not get the url, {now}"
            File.write(str)
    return soup

def Data(soup):
    names = []
    for n in soup.find_all('div'):
        x = n.get("class")
        if x is not None and x == "dirl_info":
            names.append(n.text)
            print(names)


def Start(url):
    print('getting soup')
    soup = Soup('https://www.localfirst.com/directory/listing')
    print("getting data")
    data = Data(soup)




print(Start('https://www.localfirst.com/directory/listing'))