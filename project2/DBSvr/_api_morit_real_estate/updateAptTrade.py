# coding: utf-8
from pymongo import MongoClient 
import urllib
import urllib.request
import xml.etree.ElementTree

from DBSvr.configPython import gConf

apiQueryURL = gConf['DBSvr']['apiQueryURL']
apiQyeryMonth = gConf['DBSvr']['apiQyeryMonth']
apiQueryKey = gConf['DBSvr']['apiQueryKey']

password = urllib.parse.quote(gConf['mongodb']['password'])
user = gConf['mongodb']['username']
client = MongoClient(gConf['mongodb']['protocol'] + user + ':' + password + '@' + gConf['mongodb']['address']+ '/')
# http://192.168.7.75:8081

db = client['_api_morit_real_estate']
collection = db['LAWD_CD']
colAptTrade = db['APT_TRADE'] 

# subadr, dong, apt address, ltan(좌표)

class QueryResult:
    def __init__(self, message):
        self.success = True
        self.message = message
    def __init__(self, flag, message):
        self.success = flag
        self.message = message

def get_mongoclient(username, password, address):
    """MongoDB 파이선 클라이언트를 리턴한다.
    참조 : https://docs.mongodb.com/getting-started/python/client/ """
    return MongoClient("mongodb://" + username + ':' + password + '@' + address + '/')

# year 년 
# month 월
# date 일
# dong 법정동
# subadr 지번
# apt 아파트
# stor 층
# ownarea 전용면적
# price 거래금액
def element_to_dic(element):
    year = ""; month = ""; date = ""
    dong = ""; subadr = ""; apt = ""
    stor = ""; ownarea = ""; price = ""
    for entity in element:
        if(entity.tag == '년'):
            year = entity.text
        elif(entity.tag == '월'):
            month = entity.text
        elif(entity.tag == '일'):
            date = entity.text
        elif(entity.tag == '법정동'):
            dong = entity.text
        elif(entity.tag == '지번'):
            subadr = entity.text
        elif(entity.tag == '아파트'):
            apt = entity.text
        elif(entity.tag == '층'):
            stor = entity.text
        elif(entity.tag == '전용면적'):
            ownarea = entity.text
        elif(entity.tag == '거래금액'):
            price = entity.text
    return { 'year': year, 'month': month, 'date': date,
            'dong': dong, 'subadr': subadr, 'apt': apt,
            'stor': stor, 'ownarea': ownarea, 'price': price }

def query_and_result(query):
    try:
        reqQuery = urllib.request.urlopen(query)
    except Exception as e:
        return QueryResult(False, str(e))
    else:
        result = reqQuery.read().decode('utf-8')
        return QueryResult(True, result)

def query_and_update(query):
    queryResult =query_and_result(query); 
    if( queryResult.success ):
        root = xml.etree.ElementTree.fromstring(queryResult.message)
        for child in root:
            if (child.tag == 'body'):
                for items in child:
                    for item in items:
                        dic = element_to_dic(item)
                        colAptTrade.insert_one(dic)
                for item in child:
                    if(item.tag == item):
                        print('-------------item Only-----------')
                        print(item.tag, item.attrib)
    else:
        print( queryResult.message )

def gen_api_morit_real_estate():
    cursor = collection.find()
    counter = 0;
    for document in cursor:
        if (counter > 5): 
            break
        else:
            counter = counter + 1
            print(document["_id"])
            apiQueryCode = document["code"]
            queryString = apiQueryURL + 'LAWD_CD=' + str(apiQueryCode) + '&DEAL_YMD=' + str(apiQyeryMonth) + '&serviceKey=' + apiQueryKey;
            query_and_update(queryString)



def main():
    gen_api_morit_real_estate();

if __name__ == '__main__':
    main()