import requests
from lxml import html
from bs4 import BeautifulSoup
import time
import sys
start_time = time.time()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    
}
login_data = {
    'Input.Email' : 'davor.begovic@scan.hr',
    'Input.Password' : 'a123456A',
    '__RequestVerificationToken': ''
}
with requests.session() as s: # Koristimo session kako nebi svako malo slali zahtjeve web stranici (otvarali i zatvarali session)
    url = "https://radninalog.scan.hr/Identity/Account/Login" # Stranica na koju idemo
    response = s.get(url, headers=headers, stream=True) # Uzimamo podatke sa stranice url
    soup = BeautifulSoup(response.content, 'html.parser') 
    login_data['__RequestVerificationToken'] = soup.find('input', attrs={'name':'__RequestVerificationToken'})['value']



    r = s.post(url, data=login_data, headers=headers)
    a = s.get("https://radninalog.scan.hr/RadniSati?month=9&amp;year=2021", headers=headers).text # 0.55 SEKUNDI ZA USPOSTAVU KONEKCIJE
    s = BeautifulSoup(a, "lxml")
    Tags = []



    def GetTagsFromDay(day, month):
        day_div = s.find("div", attrs={'data-day':day, 'data-month':month})
        day_a = day_div.findAll('a', attrs={'ondragstart':'drag(event)'})
        for i in range(len(day_a)):
            hour = day_a[i].find('span', attrs={'class':'badge badge-pill badge-dark'}).text
            text = day_a[i]['title']
            text_parts = text.splitlines() # splitamo title na svim newlineovima
            radni_nalog = text_parts[0]
            opis_posla = text_parts[1]
            tag = {
                'day':day,
                'month':month,
                'hours':hour,
                'radni_nalog':radni_nalog,
                'opis_posla':opis_posla
            }
            Tags.append(tag)

    GetTagsFromDay(10, 9)
    for t in range(len(Tags)):
        print(Tags[t])
    print("--- %s seconds ---" % (time.time() - start_time))


    
    
