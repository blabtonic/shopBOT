#!/usr/bin/env python
import time
import sys
import requests
from bs4 import BeautifulSoup
from splinter import Browser

#Config#
product = "k1f736npe" #copy and past last part of URL here / prompt user to enter in 
shopURL = "http://www.supremenewyork.com/shop/all"
mainURL = "http://www.supremenewyork.com" 
checkoutURL = "https://www.supremenewyork.com/checkout"
sizeOption = "Medium"

name = ""
email = ""
tel = ""
address = ""
city = ""
postcode = "" 
state = "" #ex TWO CAPITAL LETTERS
country = "" #ex ALL CAPS
cctype = "" #ex Visa Mastercard American Express
ccnumber = ""
ccexpmonth = "" #ex 04
ccexpyear = "" #ex 2019
cccvvcc = "" #ex 194

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
    browser.fill("tl",tel)
    browser.select("order[billing_country]", country)
    browser.select("order[billing_state]", state)
    browser.fill("order[billing_address]",address)
    browser.fill("order[billing_city]",city)
    browser.fill("order[billing_zip]", postcode)
    #browser.select("credit_card[type]", cctype)
    browser.fill("credit_card[cnb]", ccnumber)
    browser.select("credit_card[month]", ccexpmonth)
    browser.select("credit_card[year]", ccexpyear)
    browser.find_by_css(".terms").click()

main()