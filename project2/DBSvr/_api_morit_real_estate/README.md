1. LAWD_CD
 - http://data.go.kr 에서 제공하는 아래 서비스에서 사용하는 지역 코드
 아파트 매매 신고 조회 서비스	RTMSDataSvcAptTrade
 아파트 전월세 신고 조회 서비스	RTMSDataSvcAptRent
 연립다세대 매매 신고 조회 서비스	RTMSDataSvcRHTrade
 연립다세대 전월세 신고 조회 서비스	RTMSDataSvcRHRent
 단독다가구 매매 신고 조회 서비스	RTMSDataSvcSHTrade
 단독다가구 전월세 신고 조회 서비스	RTMSDataSvcSHRent
 - 출처
  - API 기술 문서(실거래+데이터+OpenAPI+활용가이드_v3.0.docx) 내의 데이터
  - Excel 저장 > CSV 내보내기 > CSV 파일을 메모장에서 열어 인코딩 UTF-8 로 변경
  - > "mongoimport -d _api_morit_real_estate -c LAWD_CD --type csv --file LAWD_CD.csv --headerline"

 