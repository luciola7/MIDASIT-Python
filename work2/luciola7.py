"""luciola7 work2"""

import sys
import requests
from bs4 import BeautifulSoup

def main():
    """main function"""
    base_url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    result = requests.get(base_url)
    print(sys.stdout.encoding)

    if result.status_code == 200:
        soup = BeautifulSoup(result.content, 'html.parser')
        data = soup.find_all('section', {"class", "content-section"})
        for content in data:
            print(content.text.encode('utf-8', 'ignore'))
    else:
        print("Request fail")

if __name__ == '__main__':
    main()
