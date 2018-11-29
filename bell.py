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
import time
import winsound



def get_times_to_ring():     
    url = 'https://spreadsheets.google.com/feeds/list/1Baj0j80ewjzpnL8GOfGpdqbnxAsueIl-DHCLTQ7PO70/od6/public/basic?prettyprint=true&alt=json'
    response = urllib2.urlopen(url)
    html = response.read()
    html = json.loads(html)

    format = ['column1', 'column2', 'column3']     
    day = datetime.datetime.today().weekday()
    #monday is 0, saturday is 6
    row = html['feed']['entry'][day]['content']['$t'].encode('utf-8').strip()   

    times = list(map(lambda x:x.split(":")[1].strip().replace("'",""),str(row).split(",")))[1:]
    return times

def ring_the_bell():
    print("DING!!!!")
    notes = [1521,1809,2280,3043,2280,3043]
    for note in notes[:-1]:
        winsound.Beep(note,250)
    
    winsound.Beep(notes[-1], 1000)


if __name__ == "__main__":
    day_sheet_checked = 0
    times = get_times_to_ring()
    rung = [False for i in range(len(times))]
    while 1:    
        now = datetime.datetime.now()
        timestr = "%H%M"
        sj_time = now.strftime(timestr)
        index = -1
        if(now.hour == 8 and day_sheet_checked != now.day):
            times = get_times_to_ring()
            rung = [False for i in range(len(times))]
            day_sheet_checked = now.day        
        try:
            index = times.index(sj_time)
            if(not rung[index]):
                ring_the_bell()
                rung[index] = True
        except:
            index = -1


        time.sleep(5)#it doesn't make a difference if the bell is 5 seconds late



