
import pandas as pd
import numpy as np
import requests
import json
import urllib
import re
import time
from IPython.display import display, HTML

def get_hypertext_reference(r):
    text = r.text.replace("\n","")
    text = re.search('<h2>List of results</h2>.+?</table>',text).group()
    text = re.search("<table.*",text).group()
    references = re.findall('a href=".+?"',text)
    
    return references

def get_detail(references):
#     print(references)
    details = []
    for ref in references:
        hp_txt = ref[8:-1]
        while True:
            try:
                r = requests.get(""+hp_txt,headers=headers)
                break
            except:
                time.sleep(0.2)
        print("REQUEST",r.text)
        details.append(r.text)
    return details

headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'cs-CZ,cs;q=0.8',
'Connection':'keep-alive',
'Cookie':'ASP.NET_SessionId=m1cqowvgbfhvre23furdzlge; .AspNet.ApplicationCookie=0EZWchXJK-GPA6g5Z04hqt-Q95LTOxgkX-mDigQCJuYUf5jSC61afEfBQWFVjs-1YGHb396AoNuNE3fD-H7ic4elyXpFiFq_8d-8zWOQ9kyPwwwtn3ywf02Tpi4xPAHtrdqQeG2D6Xff9CpQyFu2NHJv8-ky7etvjwszBMM4WIFDLD8COz-cnu2dDeDhMIdKPpDvhcYyeCmS5LrNYSDlwAiYAmS8b3CDwIy01llnhnWDMH-U-e2-sHAJkLTTgEHVp6wnptuN1QGd9HYGjKqNYl821kyhjgCS0NQH1TKX-oLG1STOZxylAd4XRzsLJL0ulaEOOlIsekZxc2nnn6CzqA',
'Host':'',
'Referer':'',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/41.0.2272.76 Chrome/41.0.2272.76 Safari/537.36'
}

list_of_results = []

# Python 3.x:
import html.parser
html_parser = html.parser.HTMLParser()
import codecs


data_vybrane = pd.read_excel("",skiprows=[0])

data_vybrane = data_vybrane.loc[:,['Hodnocení "A"','Název','Panel','ID výsledku v RIV']]
panels = data_vybrane['Panel'].unique()
panels

hodnoceni_panely = {}
for panel in panels:
    hodnoceni_panely[panel] = {}
    
cnt_panelE4 = 0
for web_copy in ['']:
    with codecs.open(""+web_copy,'r',encoding="ascii") as f:
        data = json.loads(f.read())    
        idx = 0 
        
        for page in data:
            for res in page:
                text = res.replace("\n","")
                title = html_parser.unescape(re.search("<title>.+?</title>",text).group()[7+16:-34])
                try:
                    riv = re.search("RIV/.+?</dd>",text).group()[:-5]
                except:
                    riv = ""
        #             display(HTML(text))

                s = re.search('.+?!',riv)
                if(s):
                    riv = s.group()[:-1]

                panel = re.search("Panel\r            </dt>\r            <dd>...",text).group()[-3:]
                panel = panel.replace(" ","")
                if(panel=='E2'):
                    cnt_panelE4 += 1
                authors = re.search("Authors.+?</dd>",text).group()[29:-5]
                authors = html_parser.unescape(authors)
                content = html_parser.unescape(re.search("Výpis udělených hodnocení:.+?Log</div>", text).group())
                A = re.findall('A\r',content)
                B = re.findall('B\r',content)
                A = list(map(lambda x: x.replace("\r",""),A))
                B = list(map(lambda x: x.replace("\r",""),B))
                others = re.findall('<strong>\r                            [^AB].+?\r',content)
                others = list(map(lambda x: x.replace('<strong>\r                            ',"")[:-1],others))
                reasons = re.findall('</td>\r\r                    <td>[^\r].+?</td>',content)
                reasons = list(map(lambda x: x.replace('</td>\r\r                    <td>','').replace('</td>\r                    <td>eng</td>','').replace('\r','').replace('</td>',''),reasons))
                reasons = list(filter(lambda x: x!='', reasons))
                hodnoceni_panely[panel][idx] = {}
                hodnoceni_panely[panel][idx]['Panel'] = panel
                try:
                    hodnoceni_panely[panel][idx]['Hodn "A"'] = data_vybrane[data_vybrane["ID výsledku v RIV"]==riv]['Hodnocení "A"'].values[0]
                except:
                    print(title)
                    hodnoceni_panely[panel][idx]['Hodn "A"'] = data_vybrane[data_vybrane["Název"]==title]['Hodnocení "A"'].values[0]
        
                hodnoceni_panely[panel][idx]['Název'] = title
                hodnoceni_panely[panel][idx]['Autoři'] = authors
                hodnoceni_panely[panel][idx]['Celkem'] = len(A)+len(B)
                hodnoceni_panely[panel][idx]['A'] = len(A)
                hodnoceni_panely[panel][idx]['B'] = len(B)
                hodnoceni_panely[panel][idx]['Celkem nehodnotilo'] = len(others)
                
                hodnoceni_panely[panel][idx]['mimo aj.'] = ""
                hodnoceni_panely[panel][idx]['střet'] = ""
                hodnoceni_panely[panel][idx]['nedost'] = ""
                
                
                for i, reason in enumerate(reasons):
                    hodnoceni_panely[panel][idx]['Zdůvodnění '+str(i)] = reason

                idx += 1 

cnt_panelE4

writer = pd.ExcelWriter('', engine='xlsxwriter')
for panel in hodnoceni_panely.keys():
    if(hodnoceni_panely[panel]!={}):
        df = pd.DataFrame(hodnoceni_panely[panel])
        df = df.transpose()
        clms = df.columns
        columns = ['Hodn "A"','Panel', 'Název','Autoři', 'Celkem', 'A',  'B',  'Celkem nehodnotilo','mimo aj.','střet' ,'nedost']
        columns.extend(list(filter(lambda x: x[:3]=='Zdů',clms)))
        df.to_excel(writer, sheet_name=panel,columns=columns,index=False)
writer.save()


