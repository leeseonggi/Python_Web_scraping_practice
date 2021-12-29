# pip install requests 로 리퀘스트 설치
import requests
res = requests.get("http://google.com") # 우리가 원하는 url 정보를 넘겨줌
print("응답코드 네이버: ",res.status_code) # 확인코드 200이면은 정상

res_nado = requests.get("http://www.nadocoding.tistory.com") 
print("응답코드 나도코딩: ",res_nado.status_code) 

if res.status_code == requests.codes.ok:
    print("정상입니다")
else:
    print("문제가 생겼습니다. [에러코드 ",res.status_code,"]")

if res_nado.status_code == requests.codes.ok:
    print("정상입니다")
else:
    print("문제가 생겼습니다. [에러코드 ",res.status_code,"]")
    
res.raise_for_status() # 제대로 HTML 문서를 가져오지 못한 경우에는 에러를 내고 프로그램을 끝냄
print("웹 스크래핑을 진행합니다")
# res_nado.raise_for_status() 
# print("웹 스크래핑을 진행합니다")

# res_nado = requests.get("http://www.nadocoding.tistory.com") 
# res_nado.raise_for_status() 
# 줄여서 이 두문장만으로 처리 가능 -> 문제가 있음 ->종료
#                               -> 문제가 없다 -> 스크래핑
# 거의 항상 같이 씀

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f: # 구글에 있는 내용을 HTML파일로 만들어줌
    f.write(res.text) 