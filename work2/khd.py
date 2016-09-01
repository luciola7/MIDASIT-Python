# coding: utf-8
from requests import Session
import bs4
import threading

def generate_session(userID, userPWD, loginURL):
    payload = {
        'strID': userID,
        'strPWD': userPWD
    }
    c = Session()
    r = c.post(loginURL, data=payload)
    return c

def check_session(session, userID):
    retVal = False
    if userID in session.cookies.values():
        retVal = True
    return retVal

def query_page(session, queryURL):
    res = session.get(queryURL)
    return res.text

def grep_result(queryResult, className, prevResult):
    soup = bs4.BeautifulSoup(queryResult, 'html.parser')
    for htmlElem in soup.find_all(class_=className):
        if htmlElem.text:
            if htmlElem.text not in prevResult:
                print(htmlElem.text + ' is new Question!')
                prevResult[htmlElem.text] = 'added'  
                      
    return prevResult

def run_checker(loginSession, queryURL, findClass, existReult):
    threading.Timer(20.0, run_checker, [loginSession, queryURL, findClass, existReult]).start()
    print('Query Start')
    textResult = query_page(loginSession, queryURL)
    print(grep_result(textResult, findClass, existReult))
    print('Query End')
    

def main():
    """main function"""
    userID = 'hdkim'
    pserPWD = ''
    loginURL = 'https://kor.midasuser.com/building/membership/login_ok.asp'
    queryURL = 'http://kor.midasuser.com/building/support/qna.asp'
    findClass = 'board_no_green'
    existReult = {'263138': 'inital', '262329': 'inital', '262961': 'inital', '262985': 'inital', '263017': 'inital',
     '262913': 'inital', '262975': 'inital', '263014': 'inital', '262834': 'inital', '262909': 'inital',
     '263063': 'inital', '262872': 'inital', '263044': 'inital', '263158': 'inital', '262884': 'inital',
     '262378': 'inital', '262374': 'inital'}

    loginSession = generate_session(userID, pserPWD, loginURL)

    if check_session(loginSession, userID):
        run_checker(loginSession, queryURL, findClass, existReult)
    else :
        print('login fail.')
    
if __name__ == '__main__':
    main()