import openpyxl
import requests
from urllib import request
from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
import time

wb = openpyxl.load_workbook(filename="books.xlsx")
sheet = wb.active
rows = sheet.max_row

list1=[]
#concatenate author and title
for i in range(2,rows+1):
    title = (sheet['A'+str(i)].value,sheet['B'+str(i)].value)
    list1.append(title)    

book_list = []
#convert all rows to the required encoding
for i in list1:
    encoded = request.quote(str(i).encode('cp1251'))
    book_list.append(encoded)

#search for books
driver = webdriver.Chrome()
for i in book_list:
    link = "https://www.alib.ru/find3.php4?tfind=" + i
    driver.get(link)
    books_num = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td")
    books=books_num.text
    if books != "Рассылка: Новые поступления по ключевым словам.":
        print(books)
    time.sleep(1)
driver.quit()