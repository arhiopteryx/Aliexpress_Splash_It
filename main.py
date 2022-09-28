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
LINK_HELP_FRIEND = 'https://a.aliexpress.com/_ms4PVig'  # Link to Bring Down the Price
LINK_MAIL = 'https://harakirimail.com/inbox/'

MAIL_NAME = 'arhiopteryx'   # Enter a unique login to which a new account will be registered
MAIL_NAME_CODE = '0n'   # Initial login uniqueness value
MAIL_SECOND_NAME = '@harakirimail.com'  # Will be added to the login to generate mail
PASSWORD_LABEL = 'genya1488'    #Enter the password for the created account


def funcReg(cod, browser, browserMail):

    #password
    try:        
        elem = browser.find_element(By.XPATH, '//*[@id="batman-dialog-wrap"]/div/div[2]/div[1]/div[2]/div/div/div/div[3]/span/span[1]/input')
        elem.send_keys(PASSWORD_LABEL)
    except:
        print("error click set password")

    #click reg new user
    try:        
        elem = browser.find_element(By.CLASS_NAME, 'cosmos-btn')
        elem.click()
        sleep(1)
    except:
        print('error click enter login and password')
        
    
    sleep(5)    #wait slide verification 
    
    try:     
        #frame_0 = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.ID, "baxia-dialog-content")))

        #to form slider
        frame_0 = browser.find_element(By.ID, 'baxia-dialog-content')
        browser.switch_to.frame(frame_0)
        print('Find Slider`s frame ')

        #find slider`s elements
        slider = browser.find_element(By.ID, "nc_1_n1z")       
        container = browser.find_element(By.ID, "nc_1__scale_text")   
        
        #try pull slider
        move = ActionChains(browser)
        move.click_and_hold(slider)
        move.move_by_offset(int(container.size['width']-slider.size['width']), 0).release().perform()
        

        #exit form frame
        browser.switch_to.default_content()  
        #again click reg new user  
        submit = browser.find_element(By.CLASS_NAME, 'cosmos-btn')
        submit.click()
        
    except:
        print("Slider non found")
    
    print("Get mail code")

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


    print(f"code = {textCode}")

    try:
        sleep(2)        
        elem = browser.find_element(By.XPATH, '//*[@id="batman-dialog-wrap"]/div/div[2]/div/div[2]/div/div/div/div[1]/input[1]')
        elem.send_keys(textCode[0])
        elem = browser.find_element(By.XPATH, '//*[@id="batman-dialog-wrap"]/div/div[2]/div/div[2]/div/div/div/div[1]/input[2]')
        elem.send_keys(textCode[1])
        elem = browser.find_element(By.XPATH, '//*[@id="batman-dialog-wrap"]/div/div[2]/div/div[2]/div/div/div/div[1]/input[3]')
        elem.send_keys(textCode[2])
        elem = browser.find_element(By.XPATH, '//*[@id="batman-dialog-wrap"]/div/div[2]/div/div[2]/div/div/div/div[1]/input[4]')
        elem.send_keys(textCode[3])
    except:
        print("error set mail code")
    try:        
        elem = browser.find_element(By.CLASS_NAME, 'cosmos-btn')
        elem.click()
        sleep(1)
    except:
        print('error confirm code')

    print("code input correct")
    sleep(10)


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
    mobileEmulation = {'deviceName': 'iPhone SE'}
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    options.add_argument(f"user-agent=Mozilla/5.0 (Android 11; Mobile; rv:83.0) Gecko/83.0 Firefox/83.0")
    options.add_argument('--allow-profiles-outside-user-dir')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('useAutomationExtension', False)
    #options.set_headless(True)
    #browser = webdriver.Chrome(options=options)
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(500, 500)


    browser.get(LINK_SET_CONFIG)
    for i in range(1000):
        try:
            mailCodeName = codeNam + str(i)
            browser.get('https://login.aliexpress.com/xman/xlogout.htm')
            sleep(1)
            browser.get(LINK_HELP_FRIEND)
            sleep(2)

            print(MAIL_NAME + mailCodeName + MAIL_SECOND_NAME + ':' + PASSWORD_LABEL + '----testing')

            try:        
                submit = browser.find_element(By.CLASS_NAME, 'rcButton--btnText--3M0lmD9')
                submit.click()
                sleep(5)
            except:
                print("error click help friend")

            try:        
                submit = browser.find_element(By.CLASS_NAME, 'rcButton--btnText--3M0lmD9')
                submit.click()
                sleep(5)
            except:
                print("error click help friend")
                
            try:        
                submit = browser.find_element(By.CLASS_NAME, 'scene-login-icon-more')
                submit.click()
                sleep(1)
            except:
                print("error click create new user")

            
            try:                    
                sleep(2)
                submit = browser.find_element(By.CLASS_NAME, 'cosmos-tabs-nav-item')
                submit.click()
                elem = browser.find_element(By.XPATH, '//*[@id="batman-dialog-wrap"]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/span[1]/span[1]/input')               
                elem.send_keys(MAIL_NAME + mailCodeName + MAIL_SECOND_NAME)
                funcReg(mailCodeName, browser, browserMail)
            except:
                print("error registration old")
            
            
            try:        
                submit = browser.find_element(By.CLASS_NAME, 'rcButton--btn--EMLV5lz')            
                submit.click()
                sleep(3)
            except:
                print("Click help Friend 1 error")
            try:        
                submit = browser.find_element(By.CLASS_NAME, 'rcButton--btn--EMLV5lz')            
                submit.click()
                sleep(3)
            except:
                print("Click help Friend 2 error")

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
