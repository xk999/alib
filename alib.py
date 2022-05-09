# -*- coding: utf-8 -*-
import openpyxl
import requests
from urllib import request
from bs4 import BeautifulSoup
import time
from langdetect import detect

wb = openpyxl.load_workbook(filename="books.xlsx")
sheet = wb.active
rows = sheet.max_row

num = int(input("Which row shall we start with? "))
list1=[]
#concatenate author and title
for i in range(num,rows+1):
    title = (sheet['A'+str(i)].value,sheet['B'+str(i)].value)
    list1.append(title)    

book_list = []
#convert rows to the required encoding
for i in list1:
    lang = detect(str(i))
    if lang == 'ru' or 'bg': 
        encoded = request.quote(str(i).encode('cp1251'))
        book_list.append(encoded)

#search for books
for book in book_list:
    link = "https://www.alib.ru/find3.php4?tfind=" + book
    page= requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    books = soup.findAll("table", {"bgcolor" : "#FFFFFF"})
    for element in books:
        print(element.text)
    time.sleep(1)
