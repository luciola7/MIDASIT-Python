# coding: utf-8
from requests import Session
import bs4
import threading
import operator

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

def process_word_to_key(word):
    word = word.replace('[답변완료]', '')
    word = word.replace('.', '')
    return word

def save_key(postNumber, word, wordMap):
    elemArr = wordMap.get(word)
    if elemArr:
        elemArr.append(postNumber)
    else:
        elemArr = []
        elemArr.append(postNumber)
        wordMap[word] = elemArr

def convert_sentence_to_keys(sentence):
    words = sentence.split()
    for idx, word in enumerate(words):
        words[idx] = process_word_to_key(word)
    return words

def save_sentence(postNumber, sentence, prevResult, wordMap):
    prevResult[postNumber] = sentence
    words = convert_sentence_to_keys(sentence)
    for word in words:
        save_key(postNumber, word, wordMap)

def grep_result(queryResult, className, prevResult, wordMap):
    soup = bs4.BeautifulSoup(queryResult, 'html.parser')
    for htmlElem in soup.find_all(class_=className):
        if htmlElem.text:
            if htmlElem.text not in prevResult:
                postNumber = int(htmlElem.text)
                sentence = htmlElem.parent.a.text;
                save_sentence(postNumber, sentence, prevResult, wordMap)

def run_checker(loginSession, queryURL, findClass, existReult, wordMap):
    #threading.Timer(2.0, run_checker, [loginSession, queryURL, findClass, existReult]).start()
    print('Query :', queryURL)
    textResult = query_page(loginSession, queryURL)
    grep_result(textResult, findClass, existReult, wordMap)   

def main():
    """main function"""
    userID = '--------'
    pserPWD = '------'
    loginURL = 'https://kor.midasuser.com/building/membership/login_ok.asp'
    queryURL = 'http://kor.midasuser.com/building/support/qna.asp'
    qnaUrlPage = 'http://kor.midasuser.com/building/support/qna.asp?pg={page_num}&sk=&so=&sort=&bid=103&nCat='
                  
    findClass = 'board_no_green'
    existReult = {}

    wordMap = {}

    queryEnd = 5;
    queryFrom = 1;

    # 데이터를 만든다.
    loginSession = generate_session(userID, pserPWD, loginURL)

    if check_session(loginSession, userID):
        while queryFrom < queryEnd:
            queryURL = qnaUrlPage.format(page_num=queryFrom)
            run_checker(loginSession, queryURL, findClass, existReult, wordMap)
            queryFrom = queryFrom + 1
    else :
        print('login fail.')

    #데이터 중에서 관련 있는 글을 찾는다.

    resultDic = {}
    
    target = 262291
    targetTitle = existReult.get(target)
    if targetTitle:
        print('Check relative item No.', target, ' : ', targetTitle)  
        keys = convert_sentence_to_keys(targetTitle)
        for key in keys:
            items = wordMap.get(key)
            if items:
                for item in items:
                    prevCount = resultDic.get(item)
                    if prevCount:
                        resultDic[item] = prevCount + 1
                    else:
                        resultDic[item] = 1
        resultsSort = sorted(resultDic.items(), key = operator.itemgetter(1), reverse = True)

        print('Relative items')
        for result in resultsSort:
            print('No.', result[0], ' : ', existReult.get(result[0]))
        print(resultsSort)
    else:
        print("Cannot get results.")

if __name__ == '__main__':
    main()