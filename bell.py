print("running")
'''
@desc Parse Google Drive spreadsheet data via python
@author Misha M.-Kupriyanov https://plus.google.com/104512463398531242371/
@link https://gist.github.com/3969255
'''
# Spreadsheet https://docs.google.com/spreadsheet/pub?key=0Akgh73WhU1qHdFg4UmRhaThfUFNBaFR3N3BMVW9uZmc&output=html


import logging
import urllib.request as urllib2
import json
import datetime


def get_times_to_ring():
    # JSON Representation
    url = 'https://spreadsheets.google.com/feeds/list/0Akgh73WhU1qHdFg4UmRhaThfUFNBaFR3N3BMVW9uZmc/od6/public/basic?prettyprint=true&alt=json'
    #      https://spreadsheets.google.com/feeds/list/<spreadsheet_key>/<worksheet_id>/public/basic
    #      
    url = 'https://spreadsheets.google.com/feeds/list/1Baj0j80ewjzpnL8GOfGpdqbnxAsueIl-DHCLTQ7PO70/od6/public/basic?prettyprint=true&alt=json'


    #https://spreadsheets.google.com/feeds/worksheets/1Baj0j80ewjzpnL8GOfGpdqbnxAsueIl-DHCLTQ7PO70/private/full

    #https://docs.google.com/spreadsheets/d//edit?usp=sharing
    response = urllib2.urlopen(url)
    html = response.read()
    html = json.loads(html)

    format = ['column1', 'column2', 'column3']     
    day = datetime.datetime.today().weekday()
    #monday is 0, saturday is 6
    row = html['feed']['entry'][day]['content']['$t'].encode('utf-8').strip()   

    times = list(map(lambda x:x.split(":")[1],str(row).split(",")))[1:]
    return times



if __name__ == "__main__":
    print(get_times_to_ring())
    #print ('column1:%s column2:%s column3:%s' % (column1, column2, column3)    )
    

