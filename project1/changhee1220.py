# -*- coding: utf-8 -*-
from requests import session
from bs4 import BeautifulSoup
    
payload = {
    'strID': 'pch0202',
    'strPWD': 'changhee30165'
}

with session() as c:
    r = c.post('https://kor.midasuser.com/building/membership/login_ok.asp', data=payload)
    print(r.headers)
    
    # print(r.headers)
    # print(r.text)
    response = c.get('http://kor.midasuser.com/building/support/faq_view.asp?idx=89423&nPage=1&strNo=194&sk=&bid=119&strCate=&strCate2=')
    print(response.text)

    html_text = response.text

    soup = BeautifulSoup(html_text, 'html.parser')

    question = soup.font.text

    answer = soup.p.text
    
f=open("project1.txt", mode='w', encoding='utf-8')

f.write('Question: ')
f.write(question)
f.write('\n')
f.write('Answer: ')
f.write(answer)

f.close()
