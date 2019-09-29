#!/usr/bin/env python


import scraperwiki
import lxml.html
import urlparse


def scrape_url(url):
    record = {}
    html = scraperwiki.scrape(url)
    root = lxml.html.fromstring(html)
    results = root.xpath (result_xpath)
    print results
    for x in results:	
        record['rank']=x[0].text
        record['mark'] = x[1].text
        record['wind'] =  x[2].text
        record['competitor'] =  x[3].text
        record['dob'] =  x[4].text
        record['nat']=x[5][0].text
        record['pos']=x[6].text
        record['venue']=x[7].text
        record['date']=x[8].text
        print record
        scraperwiki.sqlite.save(unique_keys=['date', 'competitor'], data=record, table_name='100races') 

#SETUP
baseurl = 'https://www.iaaf.org/records/toplists/sprints/100-metres/outdoor/men/senior/2017?regionType=world&timing=electronic&windReading=regular&bestResultsOnly=false'
result_xpath = '//*[@id="toplists"]/div[3]/table/tbody/tr[td]'
for i in range(1,181):
    starting_url=baseurl+"&page="+str(i)
    print starting_url
    scrape_url(starting_url)
    
    
    


