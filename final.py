from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from openpyxl import Workbook

def Data():
    final = []
    urls = ['http://www.ipaidabribe.com/reports/all?page=#gsc.tab=0']
    titles = []
    amount = []
    department = []
    transaction = []
    views = []
    city = []
    date = []
    count = 0
    for a in range(1, 100):
        a *= 10
        string = "http://www.ipaidabribe.com/reports/all?page=" + str(a)
        urls.append(string)
    for i in tqdm(urls):
        count += 1
        print('page' + str(count))
        response = requests.get(i)
        soup = BeautifulSoup(response.text, 'html.parser')

        for i in soup.find_all('h3'):
            z = i.get('class')
            if z is not None and z[0] == "heading-3":
                x = i.find('a').get('title')
                titles.append(x)

        for i in soup.find_all('li'):
            z = i.get('class')
            if z is not None and z[0] == "paid-amount":
                y = i.find('span')
                amount.append(y.text)

        for i in soup.find_all('li'):
            z = i.get('class')
            if z is not None and z[0] == "views":
                views.append(i.text)

        for i in soup.find_all('div'):
            z = i.get('class')
            if z is not None and z[0] == "key":
                c = i.find('a').get('title')
                city.append(c)

        for i in soup.find_all('li'):
            z = i.get('class')
            if z is not None and z[0] == "transaction":
                t = i.find('a').get('title')
                transaction.append(t)

        for i in soup.find_all('li'):
            z = i.get('class')
            if z is not None and z[0] == "name":
                t = i.find('a').get('title')
                department.append(t)

        for i in soup.find_all('li'):
            z = i.get('class')
            if z is not None and z[0] == "time-span":
                date.append(i.text)

    for i in range(0, 1000):
        temp = [date[i], titles[i], amount[i], department[i], transaction[i], views[i], city[i]]
        final.append(temp)

    return final

def Excel(data):
    book = Workbook()
    sheet = book.active
    headers = ['date', 'Title', 'Amount', 'Department', 'transaction','views','city',]
    sheet.append(headers)
    for i in data:
        sheet.append(i)
    book.save('Data_file.xlsx')

def Start():
    print('Getting data from website')
    data = Data()
    print('Got data, Appending in excel sheet')
    Excel(data)

Start()