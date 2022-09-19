import shelve
from time import sleep
import random
from urllib import request
import requests
import pandas as pd


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from threading import Thread, Barrier

from bs4 import BeautifulSoup as bs

LINK_SET_CONFIG = 'https://login.aliexpress.com/setCommonCookie.htm?currency=USD&region=UA&bLocale=en_US&site=glo&return=https://www.aliexpress.com'
LINK_HELP_FRIEND = 'https://a.aliexpress.com/_uQVeli'# Ссылка на Сбей цену
LINK_MAIL = 'https://harakirimail.com/inbox/'

MAIL_NAME = 'login' # Введите уникальный логин, на который будет регестрироваться новый аккаунт 
MAIL_NAME_CODE = '01' # Начальное значение уникальности логина
MAIL_SECOND_NAME = '@harakirimail.com'#  Будет добавляться к логину для формирования почты
PASSWORD_LABEL = 'password'# Введите пароль на создаваемый аккаунт

# Не нужное
'''
#создаем объект браузера
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")
options.add_argument('--allow-profiles-outside-user-dir')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option('useAutomationExtension', False)
options.set_headless(True)
browserMail = webdriver.Chrome(options=options)
#browserMail.set_window_size(600, 600)


#создаем объект браузера
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent=Mozilla/5.0 (Android 11; Mobile; rv:83.0) Gecko/83.0 Firefox/83.0")
options.add_argument('--allow-profiles-outside-user-dir')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option('useAutomationExtension', False)
#options.set_headless(True)
#browser = webdriver.Chrome(options=options)
#browser = webdriver.Chrome(options=options)
#browser.set_window_size(600, 600)
'''

def funcReg(cod, browser, browserMail):

        


    try:        
        elem = browser.find_element(By.XPATH, "//*[@id=\"root\"]/div[2]/div[1]/div[2]/div[1]/div/div/div[4]/span/span[1]/input")
        elem.send_keys(PASSWORD_LABEL)
    except:
        print("error 1")

    try:        
        elem = browser.find_element(By.CLASS_NAME, 'comet-btn')
        elem.click()
        sleep(1)
    except:
        print('error 2')

    print("pochta")

    sleep(6)
    browserMail.get(LINK_MAIL + MAIL_NAME + cod)
    elems = browserMail.find_elements_by_xpath("//a[@href]")
    linkCurMail = ''
    for elem in elems:
        if 'email' in elem.get_attribute("href"):
            linkCurMail = elem.get_attribute("href")
            break

    browserMail.get(linkCurMail)

    textCode = browserMail.find_element(By.CLASS_NAME, 'code').text


    print("cod poluchen")


    try:
        sleep(2)        
        elem = browser.find_element(By.XPATH, "//*[@id=\"root\"]/div[2]/div/div[2]/div[1]/div/div/div[1]/input[1]")
        elem.send_keys(textCode[0])
        elem = browser.find_element(By.XPATH, "//*[@id=\"root\"]/div[2]/div/div[2]/div[1]/div/div/div[1]/input[2]")
        elem.send_keys(textCode[1])
        elem = browser.find_element(By.XPATH, "//*[@id=\"root\"]/div[2]/div/div[2]/div[1]/div/div/div[1]/input[3]")
        elem.send_keys(textCode[2])
        elem = browser.find_element(By.XPATH, "//*[@id=\"root\"]/div[2]/div/div[2]/div[1]/div/div/div[1]/input[4]")
        elem.send_keys(textCode[3])
    except:
        print("error 3")
    try:        
        elem = browser.find_element(By.CLASS_NAME, 'comet-btn')
        elem.click()
        sleep(1)
    except:
        print('error 2')

    print("cod vveden")
    sleep(8)


def funcThread(barrier, codeNam):
    
    #создаем объект браузера
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")
    options.add_argument('--allow-profiles-outside-user-dir')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('useAutomationExtension', False)
    # options.set_headless(True)
    options.add_argument("--headless")  #для работы в безоконном режиме, необходимо для удаленного сервера
    browserMail = webdriver.Chrome(options=options)
    #browserMail.set_window_size(500, 500)


    #создаем объект браузера
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent=Mozilla/5.0 (Android 11; Mobile; rv:83.0) Gecko/83.0 Firefox/83.0")
    options.add_argument('--allow-profiles-outside-user-dir')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('useAutomationExtension', False)
    #options.set_headless(True)
    #browser = webdriver.Chrome(options=options)
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(500, 500)

    for i in range(1000):
        try:
            mailCodeName = codeNam + str(i)
            browser.get('https://login.aliexpress.com/xman/xlogout.htm')
            browser.get(LINK_SET_CONFIG)
            sleep(1)
            browser.get(LINK_HELP_FRIEND)
            sleep(2)

            print(MAIL_NAME + mailCodeName + MAIL_SECOND_NAME + ':' + PASSWORD_LABEL + '----testing')

            try:        
                submit = browser.find_element(By.CLASS_NAME, 'Button--btnContent--267BC7F')
                submit.click()
                sleep(1)
            except:
                print("error help")

            try:        
                submit = browser.find_element(By.CLASS_NAME, 'comet-tabs-nav-item')
                submit.click()
                sleep(1)
            except:
                print("error reg")

            
            try:        
                elem = browser.find_element(By.XPATH, "//*[@id=\"root\"]/div[2]/div[1]/div[2]/div[1]/div/div/div[3]/span[1]/span[1]/input")
                
                elem.send_keys(MAIL_NAME + mailCodeName + MAIL_SECOND_NAME)
            except:
                print("error 1")

            checkCode = True
            while(checkCode):
                funcReg(mailCodeName, browser, browserMail)
                try:
                    checkCode = browser.find_element(By.CLASS_NAME, 'comet-btn')
                except:
                    checkCode = False
            
            try:        
                #sleep(5)
                submit = browser.find_element(By.CLASS_NAME, 'Button--btnContent--267BC7F')
                submit.click()
            except:
                print("error help")

            f = open('accounts.txt' , 'a')
            f.write(MAIL_NAME + mailCodeName + MAIL_SECOND_NAME + ':' + PASSWORD_LABEL + '\n')
            f.close()
        
        except:
            print(MAIL_NAME + mailCodeName + MAIL_SECOND_NAME + ':' + PASSWORD_LABEL + 'error')

        

number_of_threads = 2# Работа в 2 потока
barrier = Barrier(number_of_threads)
threads = []

threads = []

i = 0

for _ in range(number_of_threads):
    t = Thread(target=funcThread, args=(barrier, str(i)+'q3thread')) 
    i = i+1
    t.start()
    threads.append(t)

for t in threads:
    t.join()
