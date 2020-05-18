from bs4 import BeautifulSoup
import requests


url='https://www.shopclues.com/mobiles-smartphones.html?'
data=[]
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
for i in soup.find_all('div'):
    if i.get('class') is None or i.get('class')[0]=='row':
        for x in i.find_all('div'):
            if x.get('class') is not None or x.get('class')[0]=='column col3':
                for i in x.find('span'):
                    if i.get('class') is not None and i.get('class')[0]=='prod_name':
                        print(i.text)
                # z = i.find('span').get('class')
                # if z is not None and z=='prod_name':
                #     print(z.text)






