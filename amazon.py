from sele import webdriver
import re
from bs4 import BeautifulSoup

browser = webdriver.Chrome('E:\Final\merge\merge1\chromedriver.exe')
browser.get('https://www.amazon.com/ap/register%3Fopenid.assoc_handle%3Dsmallparts_amazon%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fwww.smallparts.com%252Fsignin%26marketPlaceId%3DA2YBZOQLHY23UT%26clientContext%3D187-1331220-8510307%26pageId%3Dauthportal_register%26openid.mode%3Dcheckid_setup%26siteState%3DfinalReturnToUrl%253Dhttps%25253A%25252F%25252Fwww.smallparts.com%25252Fcontactus%25252F187-1331220-8510307%25253FappAction%25253DContactUsLanding%252526pf_rd_m%25253DA2LPUKX2E7NPQV%252526appActionToken%25253DlptkeUQfbhoOU3v4ShyMQLid53Yj3D%252526ie%25253DUTF8%252Cregist%253Dtrue')


# file = open('config.txt')
# lines = file.readlines()
name = 'niksi'
password = 'Lockdown2030$$'

browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[1]/input').send_keys(name)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[1]/input').send_keys(name)

continue_button = browser.find_element_by_xpath(
        '//*[@id="main-auth-card"]/form/div[1]/div/div/button')
continue_button.click()
browser.find_element_by_xpath('//*[@id="login_password"]').send_keys(password)
login_button = browser.find_element_by_xpath(
        '//*[@id="main-auth-card"]/form/div[2]/div/div/button')
login_button.click()
# browser.get('https://www.upwork.com/cat/developers/')
# src = browser.page_source
# soup = BeautifulSoup(src, "html.parser")
# print(soup)
