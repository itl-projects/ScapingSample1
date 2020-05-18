from bs4 import BeautifulSoup
import requests
import re
import datetime
from tqdm import tqdm
import time
from openpyxl import Workbook


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

# print(Soup('https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/'))

def Required_Data(soup):
    emails = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    x = tqdm(data=response.text, leave=False)
    new_emails = x.re.findall(r"^\d{5}$", response.text)
    emails.append(new_emails)
    return emails

def Excel(data):
    book = Workbook()
    sheet = book.active
    headers = ['a','b','c','d']
    sheet.append(headers)
    for i in data:
        sheet.append(i)
    book.save('nikita.xlsx')






