import requests
import base64
import json
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
    response = requests.get(url=url, headers=headers, params=params)
    print(response.text)

# print(Soup("https://www.upwork.com/ab/jobs/search/url?initial_request=true&per_page=10&sc=data-mining-management"))

def season():
    urls = []
    x = 1811468
    for i in range(0, 21):
        x -= 2
        string = "https://vgls.betradar.com/vfl/feeds/?/srvgdemonstrator/en/Europe:Berlin/gismo/stats_season_fixtures2/" + str(x)
        urls.append(string)
        print(len(urls))
    return urls

print(season())