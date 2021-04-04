import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys
from datetime import timedelta, date


def userInfo():
    myemail = ""
    mypassword = ""

    email = driver.find_element_by_xpath('//*[@id="emailaddress"]')
    email.send_keys(myemail)

    passwrd = driver.find_element_by_xpath('//*[@id="password"]')
    passwrd.send_keys(mypassword)

    time.sleep(2)

    login()

def login():
    try:
        loginButton = driver.find_element_by_xpath('//*[@id="loginButton"]')
        driver.execute_script("arguments[0].click();", loginButton)
    except:
        print('unable to log in')

    time.sleep(2)

    chooseDay()

def chooseDay():
    try:
        selectDayButton = driver.find_element_by_xpath('//*[@id="btn_date_select"]')
        driver.execute_script("arguments[0].click();", selectDayButton)
    except:
        print('unable to select day')
        driver.quit()
        driver.close()

    try:
        dateSelected = date.today() + timedelta(days=2)
        dayButton = driver.find_element_by_xpath('//*[@id="date_' + str(dateSelected) + '"]')
        driver.execute_script("arguments[0].click();", dayButton)
    except:
        print('date not there')
        driver.quit()
        driver.close()
    
    selectTime()

def selectTime():
    try:
        bookTimeSlots = driver.find_element_by_xpath("//*[contains(text(), 'at 4:00 PM')]")
        driver.execute_script("arguments[0].click();", bookTimeSlots)
    except:
        driver.quit()
        driver.close()

    confirmBooking()

def confirmBooking():
    try:
        bookyesButton = driver.find_element_by_xpath('//*[@id="dialog_book_yes"]')
        driver.execute_script("arguments[0].click();", bookyesButton)
    except:
        driver.quit()
        driver.close()

if __name__ == '__main__':
    # Load chrome
    driver = webdriver.Chrome()
    driver.get("https://myfit4less.gymmanager.com/portal/login.asp")

    time.sleep(2)

    userInfo()
    driver.quit()
    driver.close()

