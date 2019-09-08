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
        record['player']=x[0][0].text
        record['country']=x[0][0].tail
        record['span'] = x[1].text
        record['Mat'] =  x[2].text
        record['Inns'] =  x[3].text
        record['No'] =  x[4].text
        record['RunsDescending']=x[5][0].text
        record['Highest']=x[6].text
        record['Average']=x[7].text
        record['100']=x[8].text
        record['50']=x[9].text
        record['0']=x[10].text
        print record
        scraperwiki.sqlite.save(unique_keys=['player'], data=record, table_name='allbatsmen') 

#SETUP
baseurl = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;filter=advanced;orderby=runs;template=results;type=batting'
result_xpath = '//*[@id="ciHomeContentlhs"]/div[3]/table[3]/tbody/tr[td/a]'
for i in range(1,61):
    starting_url=baseurl+";page="+str(i)
    print starting_url
    scrape_url(starting_url)
    
    
    


