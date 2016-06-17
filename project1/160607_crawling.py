# coding: utf-8
import requests
import bs4
import re
import getpass


def parse_qna_html(session, target_url):
    response = session.get(target_url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    
    title = soup.find('b')
    
    anslist = soup.find_all(class_='boardText')
    
    #assert(len(anslist) == 2)
    
    ret = dict()
    
    ret['title'] = title.text
    if len(anslist) > 0:
        ret['Q'] = anslist[0].text
    if len(anslist) > 1:
        ret['A'] = anslist[1].text
    
    return ret


def get_href(a):
    m = re.compile('(?<=".).+(?<=nCat=)')
    return m.search(a).group(0)


def crwal_qna(most_recent_post):
    """
    가장 최근에 수집한 게시물의 번호를 입력으로 넣으면, 이 번호 이후에 생긴 게시물을 모두 긁어온다.
    """
    ret = list()
    
    account = dict()
    account['strID'] = input('ID: ')
    account['strPWD'] = getpass.getpass('Passward: ')
    
    #faq_url = 'http://kor.midasuser.com/building/support/faq.asp?pg={page_num}&sk=&bid=119&strCate=&strCate2='
    qna_url = 'http://kor.midasuser.com/building/support/qna.asp?pg={page_num}&sk=&so=&sort=&bid=103&nCat='
    
    with requests.session() as s:    
        s.post('https://kor.midasuser.com/building/membership/login_ok.asp', account)
        
        crawl_all = False
        page_index = 1
        
        # 원하는 포스트를 긁어올 때까지 페이지를 이동하면서 크롤링한다.
        while not crawl_all:
            page_url = qna_url.format(page_num=page_index)
            res = s.get(page_url)
            soup = bs4.BeautifulSoup(res.text, 'html.parser')

            # 게시물 번호를 기준으로해서 게시물의 url을 가지고오고, 가져온 url로 들어가서 내용을 긁어온다.
            for post_num_tag in soup.find_all(class_='board_no_green'):
                parent_tag =  post_num_tag.parent
                postnum = parent_tag.find(align='center').text

                if len(postnum) == 0:
                    continue

                if int(postnum) <= most_recent_post:
                    crawl_all = True
                    break

                href = get_href(str(parent_tag.a))

                contents_url = 'http://kor.midasuser.com/building/support' + href
                contents_url = contents_url.replace('&amp;', '&')

                print(contents_url)
                
                ret.append(parse_qna_html(s, contents_url))

            page_index += 1
            
    return ret


crawled_list = crwal_qna(most_recent_post=262100)

for index, crawled in enumerate(crawled_list):
    title = crawled.get('title', '')
    question = crawled.get('Q', '')
    answer = crawled.get('A', '')
    
    print(index+1, title)
    print('Q:\n%s' % question)
    print('A:\n%s' % answer)
    print('=======')