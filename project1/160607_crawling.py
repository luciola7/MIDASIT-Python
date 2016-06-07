
# coding: utf-8

# In[231]:

def parse_qna_html(session, target_url):
    response = session.get(target_url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    
    title = soup.find('b')
    
    anslist = soup.find_all(class_='boardText')
    assert(len(anslist) == 2)
    
    return {'title': title.text, 'Q': anslist[0].text, 'A': anslist[1].text}


# In[244]:

def get_href(a):
    m = re.compile('(?<=".).+(?<=nCat=)')
    return m.search(a).group(0)


# In[245]:

import requests
import bs4
import re

def crwal_qna(page_index, mrpost):
    #faq_url = 'http://kor.midasuser.com/building/support/faq.asp?pg={page_num}&sk=&bid=119&strCate=&strCate2='
    qna_url = 'http://kor.midasuser.com/building/support/qna.asp?pg={page_num}&sk=&so=&sort=&bid=103&nCat='
    sample_url = qna_url.format(page_num=page_index)

    with requests.session() as s:
        account = {'strID': 'superbsung', 'strPWD': '----'}
        s.post('https://kor.midasuser.com/building/membership/login_ok.asp', account)

        res = s.get(sample_url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for item in soup.find_all(class_='board_no_green'):
            parent = item.parent
            post_num = parent.find(align='center').text

            if len(post_num) == 0: # 전구 그림이 있으면 공지라서 가지고 올 필요 없음
                continue

            post_index = int(post_num) # mrpost 보다 최신인 post 만 긁어오자
            if post_index <= mrpost:
                break

            href = get_href(str(parent.a))
            
            contents_url = 'http://kor.midasuser.com/building/support' + href
            contents_url = contents_url.replace('&amp;', '&')

            #print(contents_url)

            ret = parse_qna_html(s, contents_url)

            print(post_num, ret['title'])
            print('Q:\n%s' % ret['Q'])
            print('A:\n%s' % ret['A'])
            print('=======')


# In[249]:

crwal_qna(page_index=1, mrpost=261892)
#TODO: page_index 상관 없이 mrpost 만으로 동작하게끔


# In[ ]:



