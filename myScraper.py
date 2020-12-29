#! env/bin/python3
from openpyxl import Workbook
from requests_html import HTMLSession
import sqlite3, csv, xlsxwriter

#Get url
url = input('url: ')
session = HTMLSession()
req = session.get(url)
#For dynamic pages
#req.html.render()

#Scrap data
while True:
    source = input('What to scrape?\n >>> ')
    slot = input('Where to slot? \n >>> ')
    try:
        scrap = req.html.find(source)
        data = []
        for i in scrap:
            data.append(i.text)
        with open('slots/'+slot[0:10], 'w') as f:
            slot_writer = csv.writer(f) 
            slot_writer.writerow(data)
            f.close() 
    
    except:
        scrap = req.html.xpath(source)
        data = []
        for i in scrap:
            data.append(i.text)
        with open('slots/'+slot[0:10], 'w') as f:
            slot_writer = csv.writer(f)
            slot_writer.write(data)
            f.close()    
    ask = input('More source?\n >>> ')
    if ask == 'y':
        pass
    else:
        break
#Output data
out = input('formats: \n(1)xlsx \n(2)csv\n(3)txt \n(4)sql \n>>>')

if out == "1":

    col = 0
    row = 0
    #wb = Workbook()
    #ws = wb.active
    workbook = xlsxwriter.Workbook('Output.xlsx')
    worksheet = workbook.add_worksheet()

elif out == "2":
    output = open('Output.csv', 'w')
    writer = csv.writer(out)

elif out == "3":
    with open('Output.txt', 'w') as f:
        for j in scrap:
            f.write(j.text)
        f.close()        
elif out == "4":
    pass


