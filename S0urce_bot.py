#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Blowfish, Ericuis"
__copyright__ = "Copyright 2019, Polarised"
__credits__ = ["Blowfish", "Ericuis"]

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Blowfish"


from PIL import Image
import io
import requests
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import time

def hacking():
    wait = WebDriverWait(driver, 0)
    
    while True:
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tool-type"]/img')))
            img_url = driver.find_element_by_xpath('//*[@id="tool-type"]/img')
            if img_url.get_attribute("src") == 'http://s0urce.io/client/img/words/template.png':
                continue
            print('[URL]{}'.format(img_url.get_attribute("src")))
            time.sleep(0.5)
            try:
                envoyer = driver.find_element_by_id('tool-type-word').send_keys(find_word(img_url.get_attribute("src")),Keys.ENTER)
            except KeyError:
                print("[+]Hacking Finished")
        except (TimeoutException,ElementNotInteractableException):
            print('Not found')

def find_word(url):
    with open('Dico.txt') as dico:
        lines = dico.readlines()
    dico = {}
    for i in lines:
        key = i[:i.find('=')]
        val = i[i.find('=')+1:]
        dico[key]=val.replace('\n','')
        
    print('[WORD]{}'.format(dico[url]))
    return dico[url]

        
driver = webdriver.Chrome()
driver.get("http://s0urce.io")
login_form = driver.find_element_by_id('login-input').send_keys( "Blowfish#6201" )
check_tuto = driver.find_element_by_id('checkbox-tutorial').click()
login      = driver.find_element_by_id('login-play').click()
hacking()




