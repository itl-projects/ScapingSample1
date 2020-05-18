import requests
import json

proxies= {'http':'http://175.111.129.124'}
url = 'https://www.geeksforgeeks.org/'

response = requests.get(url, proxies=proxies)
print(response.text)














