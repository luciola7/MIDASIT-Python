from requests import session
from bs4 import BeautifulSoup
    
payload = {
    'strID': 'luciola7',
    'strPWD': '-------'
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

    print('Q: ')
    print(question)
    print('A: ')
    print(answer)
