import requests
import base64
import urllib.request
from bs4 import BeautifulSoup

print("Starting")
def Soup(url):
    with open('api.txt', 'r') as hfile:
        temp = hfile.read().split('\n')

    headers = {}
    for i in temp:
        key = i.split(':')[0]
        value = i.split(':')[1]
        value = value.strip()
        headers.update({key: value})

    with open('params.txt', 'r') as pfile:
        temp1 = pfile.read().split('\n')

    params = {}
    for i in temp1:
        key = i.split(':')[0]
        value = i.split(':')[1]
        value = value.strip()
        params.update({key: value})

    # url = 'https://www.upwork.com/ab/jobs/search/url?initial_request=true&per_page=10&sc=data-mining-management'
    request = urllib.request.Request(url)
    request.add_header('Accept', 'application/json')
    response =urllib.request.urlopen(url)
    apidata = response
    return apidata

print(Soup("https://www.upwork.com/ab/jobs/search/url?initial_request=true&per_page=10&sc=data-mining-management"))# print(hi)

