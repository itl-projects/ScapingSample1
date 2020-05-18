from selenium import webdriver


browser = webdriver.Chrome('E:\Final\merge\merge1\chromedriver.exe')
browser.get('https://www.shopclues.com/mobiles-smartphones.html?&page=1')
names=[]
data = browser.find_elements_by_xpath("//div[@class='row']")
# for i in data:
columnData = data.find_elements_by_xpath("//div[@class='column col3']")
for j in columnData:

    name = j.find_element_by_xpath("//span[@class='prod_name']")
    print(name.text)

# print(names)





