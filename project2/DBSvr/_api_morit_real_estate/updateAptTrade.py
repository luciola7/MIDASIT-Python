# coding: utf-8
from pymongo import MongoClient
import urllib
import urllib.request
import xml.etree.ElementTree

apiQueryURL = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?'
apiQyeryMonth = '201601'
apiQueryKey = 'aI474NdT71RfYAP8R1alaVKdyR8ZYuNMyjdysTlEAfCWRpbxHQHnR97yOdbKKfA4Fd6BSdLfGLw9jZj9OTP7lA%3D%3D'

password = urllib.parse.quote('mid@sit')
user = 'hjang'
client = MongoClient('mongodb://' + user + ':' + password + '@192.168.7.75:27017/')

db = client['_api_morit_real_estate']
collection = db['LAWD_CD']

colAptTrade = db['APT_TRADE'] 

# year 년
# month 월
# date 일
# dong 법정동
# subadr 지번
# apt 아파트
# stor 층
# ownarea 전용면적
# price 거래금액

cursor = collection.find()
counter = 0;
for document in cursor:
    if (counter > 2): 
        break
    else:
        counter = counter + 1
        print(document["_id"])
        apiQueryCode = document["code"]
        reqQuery = urllib.request.urlopen(apiQueryURL + 'LAWD_CD=' + str(apiQueryCode) + '&DEAL_YMD=' + str(apiQyeryMonth) + '&serviceKey=' + apiQueryKey)
        result = reqQuery.read().decode('utf-8')
        root = xml.etree.ElementTree.fromstring(result)
        for child in root:
            if (child.tag == 'body'):
                for items in child:
                    for item in items:
                        print(item)
                        year = ""
                        month = ""
                        date = ""
                        dong = ""
                        subadr = ""
                        apt = ""
                        stor = ""
                        ownarea = ""
                        price = ""
                        for entity in item:
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

                        # print(entity.tag, entity.text)
                        colAptTrade.insert_one({
                                'year': year,
                                'month': month,
                                'date': date,
                                'dong': dong,
                                'subadr': subadr,
                                'apt': apt,
                                'stor': stor,
                                'ownarea': ownarea,
                                'price': price
                            })
                for item in child:
                    if(item.tag == item):
                        print('-------------item Only-----------')
                        print(item.tag, item.attrib)
