from requests_html import HTMLSession
import sqlite3, csv, xlsxwriter

#Get url
url = input('url: ')
session = HTMLSession()
req = session.get(url)
# req.html.render()

#Scrap data
while True:
    source = input('What to scrape?\n >>> ')
    slot = input('Where to slot? \n >>>')
    try:
        scrap = req.html.find(source)
        with open(slot[0:10], 'w') as f:
            for i in scrap:
                f.write(i.text)
            f.close() 
    
    except:
        scrap = req.html.xpath(source)
        with open(slot[0:10], 'w') as f:
            for i in scrap:
                f.write(i.text)
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

    workbook = xlsxwriter.Workbook('Output.xlsx')
    worksheet = workbook.add_worksheet()

elif out == "2":
    pass
elif out == "3":
    with open('Output.txt', 'w') as f:
        for i in data:
            f.write(i.text)
        f.close()        
elif out == "4":
    pass


