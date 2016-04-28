import requests
from bs4 import BeautifulSoup

def print_to_text(base_url):
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "html.parser")   
    data1 = soup.find_all('div', {"class:","dek"})
    text = ''
    for item in data1:
        print(item.text)
        text += item.getText()
    #data2 = soup.find_all('section',{"class:","content-section"})
    #for item2 in data2:
    #    print(item2.text)
    #    text += item2.getText()    
    with open("D:/Study_Python/Python/.vscode/homework.txt", encoding='utf-8', mode='w') as fout:
        fout.write(text)
    
if __name__ == "__main__":
    #Chose my own article
    base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
    print_to_text(base_url)

     