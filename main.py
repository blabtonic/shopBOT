#!/usr/bin/env python
import time
import sys
import requests
from bs4 import BeautifulSoup
from splinter import Browser

#Config#
product = "lia9ben4m" #copy and past last part of URL here
shopURL = "http://www.supremenewyork.com/shop/all"
mainURL = "http://www.supremenewyork.com" 
checkoutURL = "https://www.supremenewyork.com/checkout"
sizeOption = "Medium"

# Fill out your information here 
name = "Doug Sander"
email = "dsander1982@gmail.com"
tel = "905 555 8224"
address = "87 Free street"
city = "Brampton"
postcode = "L6B 2J1" 
state = "ON" #ex TWO CAPITAL LETTERS
country = "CANADA" #ex ALL CAPS
cctype = "Visa" #CREDIT CARD TYPE ex Visa Mastercard American Express
ccnumber = "00000000000000000000000" #CREDIT CARD NUMBER
ccexpmonth = "01" #EXPIRE MONTH ex 04
ccexpyear = "2019" #EXPIRE YEAR ex 2019
cccvvcc = "000" #CVS ex 194

#Functions#
def main():
    r = requests.get(shopURL).text
    if product in r:
        parse(r)

def parse(r):
    soup = BeautifulSoup(r, "html.parser")
    for a in soup.find_all('a', href=True):
        link = a['href']
        check(link)

def check(l):
    if product in l:
        productURL = mainURL + l
        print(productURL)
        buyProduct(productURL)

def buyProduct(url):
    browser = Browser()
    browser.visit(url)

    #choose a size 
    browser.find_by_text(sizeOption).first.click()
    print('Size Chosen')

    #add to cart
    browser.find_by_name('commit').click()
    print('Added to cart')
    time.sleep(1)

    #try to checkout
    browser.visit(checkoutURL)
    print('Checking out, filling info')

    #fills info form
    browser.fill("order[billing_name]",name)
    browser.fill("order[email]",email)
    browser.fill("order[tel]",tel)
    browser.fill("order[billing_address]",address)
    browser.fill("order[billing_zip]", postcode)
    browser.fill("order[billing_city]",city)
    browser.select("order[billing_country]", country)
    browser.select("order[billing_state]", state)
    #browser.select("credit_card[type]", cctype)
    browser.fill("credit_card[cnb]", ccnumber)
    browser.select("credit_card[month]", ccexpmonth)
    browser.select("credit_card[year]", ccexpyear)
    browser.find_by_css(".terms").click()
    browser.fill("credit_card[vval]", cccvvcc)


main()