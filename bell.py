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

    html =json.loads(html.decode('utf-8'))
    # = json.loads()

    format = ['column1', 'column2', 'column3']     
    day = datetime.datetime.today().weekday()
    #monday is 0, saturday is 6
    row = html['feed']['entry'][day]['content']['$t'].encode('utf-8').strip()   

    times = list(map(lambda x:x.split(":")[1].strip().replace("'",""),str(row).split(",")))[1:]
    return times

def playnote(frequency,duration):
    winsound.Beep(frequency,duration)
    time.sleep(.10)
    

def ring_the_bell():
    print("DING!!!!")
    notes = {"C":1635,"F":2183,"A":2750,"HiC":3270}
    '''
    1/4	1/8	1/8 1/16	 	Tempo	1/4	1/8	1/8 1/16
90	667	333	222	167	 	    150	    400	200	133	100
    '''    
    

    playnote(notes["C"],333)
    playnote(notes["C"],84)

    playnote(notes["F"], 167)
    playnote(notes["C"],167)
    playnote(notes["F"], 167)
    playnote(notes["A"], 167)
    playnote(notes["F"], 333)

    playnote(notes["F"], 333)
    playnote(notes["F"], 84)
    playnote(notes["A"], 167)
    playnote(notes["F"], 167)
    playnote(notes["A"], 167)
    playnote(notes["HiC"], 167)
    playnote(notes["A"], 333)

    playnote(notes["F"], 167)
    playnote(notes["A"], 167)
    playnote(notes["HiC"], 333)
    playnote(notes["A"], 167)
    playnote(notes["F"], 167)

    playnote(notes["C"], 333)
    playnote(notes["C"], 167)
    playnote(notes["C"], 167)
    playnote(notes["F"], 333)
 
    playnote(notes["F"], 167)
    playnote(notes["F"], 84)

    playnote(notes["F"], 666)


    
    #winsound.Beep(notes["HiC"], 167)

if __name__ == "__main__":
    ring_the_bell()
    hour_sheet_checked = 0
    times = get_times_to_ring()
    rung = [False for i in range(len(times))]
    while 1:    
        now = datetime.datetime.now()
        timestr = "%H%M"
        sj_time = str(int(now.strftime(timestr)))

        index = -1
        if(now.minute == 0 and hour_sheet_checked != now.hour):
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



