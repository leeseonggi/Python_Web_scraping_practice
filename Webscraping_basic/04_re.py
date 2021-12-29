# 정규식 기본 1
import re
# 뺑소니 운전자를 신고 경찰에 수소 협조하러감 자동차 번호판은 4자리 문자
# abcd book desk
# ca?e 세번째를 모르는데 cae는 확실히 봄
# care cafe case cave
# 이런 차량들에 대해서 검색을 할때 어째 해야 할 수 있을까?
# caae cabe cace cade ....... 너무 많음 -> 정규식 이용하면 좀 편해짐

p = re.compile("ca.e") 
# . (ca.e): 하나의 문자를 의미 > care cafe case O | caffe X
# ^ (^de) : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$) : 문자열의 끝 > case, base (O) | face(X)

m = p.match("case")
print(m.group()) # 정규식과 매칭이 된다면 출력이 됨

n = p.match("caffe")
# print(n.group()) # 매치가 되지 않으면 에러

if n:
    print(n.group())
else:
    print("매칭되지 않음")
# 조건문 작성시 매칭되지 않아도 에러가 나지 않아 걔속 프로그램을 가동 할 수 있음

def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")

m = p.match("careless")
print_match(m)


