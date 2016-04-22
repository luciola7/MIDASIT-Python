
# coding: utf-8

# In[78]:

from urllib import request
from bs4 import BeautifulSoup

web_url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'


# In[79]:

# HTML을 그대로 파일에 저장
with request.urlopen(web_url) as f:
    with open('article_html.txt', 'wb') as fout:
        fout.write(f.read())


# In[80]:

# article_html.txt 에서 HTML을 읽어서 파싱한 후 output.txt에 내용물만 저장
with open('article_html.txt', 'rb') as fin:
    soup = BeautifulSoup(fin.read(), 'html.parser')
    
    text = ''
    for dek in soup.find_all(class_='dek'):
        text += dek.getText()

    for content in soup.find_all(class_='content-section'):
        text += content.getText()
        
    with open('output.txt', encoding='utf-8', mode='w') as fout:
        fout.write(text)


# In[ ]:



