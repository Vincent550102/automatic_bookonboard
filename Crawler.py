# coding=UTF-8

import pickle
import logging
import requests
import json
import argparse
import html5lib

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep

class Crawler():
    def __init__(self):
        self.lb = 0
        self.rb = 5
        self.URL = 'https://sschool.tp.edu.tw/library/Login.action?schNo=323302'
        self.FLOW = 8000812
        self.TITLE = 'chromebook A-C214-{}/279-{}(背包*1、變壓器*1、電源線*1)'#005 #726
        #chromebook A-C214-005/279-726
        self.FV_TITLE = 259
        self.SV_TITLE = 980

    def awake_driver(self):
        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--log-level=3')
        # options.add_argument('--headless')
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.URL)

    def run(self):
        self.awake_driver()
        self.driver.find_element_by_id('coocLogin').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/button[1]').click()
        sleep(1)
        self.driver.find_element_by_id('username').send_keys('YCSH10700025')
        self.driver.find_element_by_id('password').send_keys('064795')
        self.driver.find_element_by_id('btnLogin').click()
        sleep(2)
        self.driver.find_element_by_id('sysMenu-E圖書館系統').click()
        sleep(0.5)
        self.driver.find_element_by_id('sysMenu-E圖書館系統-02書目管理').click()
        sleep(0.5)
        self.driver.find_element_by_id('div-sysMenu-E圖書館系統-02書目管理').click()
        sleep(3)
        for i in range(self.lb,self.rb):
            Ntitle = self.TITLE.format(str(self.FV_TITLE+i).zfill(3),str(self.SV_TITLE+i))
            Nflow = str(self.FLOW+i)
            print('Entering\nFLOW : {} | TITLE : {} ...\n'.format(Nflow,Ntitle))
            self.driver.find_element_by_id('ui-id-10').click()
            sleep(0.5)
            self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[4]/td/div/div[4]/table/tbody/tr[1]/td/input[1]').clear()
            self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[4]/td/div/div[4]/table/tbody/tr[1]/td/input[1]').send_keys(Nflow+'\n')
            sleep(0.5)
            self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[4]/td/div/div[4]/table/tbody/tr[2]/td/div/div[5]/div/table/tbody/tr/td[1]/table/tbody/tr/td[1]/div/span').click()
            sleep(0.5)
            self.driver.find_element_by_id('bookInfo.titleProper').send_keys(Ntitle)
            self.driver.find_element_by_id('bookInfo.dataTypeMark').send_keys('IT')
            sleep(0.5)
            self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/a[1]'))
            sleep(3)
            self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[4]/td/div/form[1]/div[1]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[3]/td/div/div/div[5]/div/table/tbody/tr/td[1]/table/tbody/tr/td[1]/div/span'))
            sleep(1)
            self.driver.find_element_by_id('bookItem.itemNo').clear()
            self.driver.find_element_by_id('bookItem.itemNo').send_keys(Nflow)
            self.driver.find_element_by_id('bookItem.collectionType').send_keys('I')
            self.driver.find_element_by_id('bookItem.circulateId').send_keys('I')
            self.driver.find_element_by_id('bookItem.itemPlace').send_keys('1')
            sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/a[1]').click()
            sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]/input[1]').click()
            sleep(0.5)
            print('Enter Complete : FLOW {}'.format(Nflow))
        sleep(2)
        print('\ncomplete a loop\n------------\n\n')
        self.lb=self.rb
        self.rb=self.lb+5
        self.driver.close()
        self.driver.quit()






if __name__ == "__main__":
    crawler = Crawler()
    for _ in range(4):
        crawler.run()