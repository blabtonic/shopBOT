#!/usr/bin/env python
import time
import sys
import requests
from bs4 import BeautifulSoup
from splinter import Browser

#Config#
product = "k1f736npe" #copy and past last part of URL here 
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
country = ""
cctype = ""
ccnumber = ""
ccexpmonth = ""
ccexpyear = ""
cccvv = ""

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
    time.sleep(3)

    #try to checkout
    browser.visit(checkoutURL)
    print('Checking out, filling info')

    #fills info form
    browser.fill("order[billing_name]",name)

main()