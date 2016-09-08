# 개발 환경 설치
1. 파이썬 3 설치
2. 파이썬 실행경로 환경변수 등록(설치 방법에 따라서 자동들록되기도 함)
3. PYTHONPATH 환경 변수 추가(DBSver의 상위 디렉토리, ....\GitHub\repo\MIDASIT-Python\project2)

# 현재 개발용으로 운영중인 서버 주소
1. MongoDB Server : 192.168.7.75:27017
2. MongoDB Express : 192.168.7.75:8081

# MongoDB Server
1. MongoDB Server 설치
 - https://www.mongodb.com 에서 프로그램 다운로드
 - https://docs.mongodb.com/manual/installation/ 인스톨 참고
2. MongoDB Superuser 추가
 - mongo-express 에서 모든 DB 접근 및 수정 가능하도록 하기 위함
 - $ mongo
 - // mongo.exe 실행
 - > use admin
 - > db.createuser({user:"yourID", pwd:"yourPWD",roles["root"]})
3. MongoDB Server 실행
 - > mongod -dbpath "path" 

# Mongo Express 설치
1. 참고 URL : https://github.com/mongo-express/mongo-express
2. mongo-express 설치
 - > npm install -g mongo-express
 - config.DBSvr.js을 파일을 YOUR_PATH/node_modules/mongo-express/config.js 로 복사
3. mongo-express 실행
 - // yourID 와 yourPWD 는 MongoDB Superuser 추가 에서 생성한 계정
 - > mongo-express -u yourID -p yourPWD -a

# Python MongoDB Driver 설치(pymongo)
1. pymongo 
 - 참고 URL : https://docs.mongodb.com/getting-started/python/
 - 참고 URL : http://ngee.tistory.com/335
 - > pip install pymongo 

# Mongo DB 백업 및 복구(이전)
1. 참고 URL : https://blog.outsider.ne.kr/790

