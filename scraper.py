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
        record['span'] = x[1].text
        record['Mat'] =  x[2].text
        record['Inns'] =  x[3].text
        record['Balls'] =  x[4].text
        record['Runs'] =  x[5].text
        record['WktsDescending']=x[6][0].text
        record['BBI']=x[7].text
        record['BBM']=x[8].text
        record['Ave']=x[9].text
        record['Econ']=x[10].text
        record['SR']=x[11].text
        record['Fivefor']=x[12].text
        record['Tenfor']=x[13].text
        print record
        scraperwiki.sqlite.save(unique_keys=['player'], data=record, table_name='bowl_above_35') 

#SETUP
baseurl = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?agemin2=35;ageval2=age;class=1;filter=advanced;orderby=wickets;template=results;type=bowling'
result_xpath = '//*[@id="ciHomeContentlhs"]/div[3]/table[3]/tbody/tr[td/a]'
for i in range(1,6):
    starting_url=baseurl+";page="+str(i)
    print starting_url
    scrape_url(starting_url)
    
    
    


