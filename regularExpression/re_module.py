import re

text = "I like orange! I love orange!"
#match: 문자열 처음부터 매치여부 조사. 객체 리턴
result = re.match("orange",text)
#search: 문자열 전체를 조사. 처음 검색된 최초 문자열 객체 리턴
result = re.search("orange",text)
print(result.group())#매치된 문자열 리턴
print(result.start())#매치된 문자열의 시작 위치 리턴
print(result.end())#매치된 문자열의 끝 위치 리턴
print(result.span())#매치된 문자열의 (시작,끝) 리턴

# findall: 매치되는 모든 문자열 리스트로 리턴
result = re.findall("orange",text)
print(result)
#finditer: 매치되는 모든 문자열의 반복가능한 객체로 리턴
result = re.finditer("orange",text)
for each in result:
    print(each)
    print(each.group())
    print(each.start())
    print(each.end())
    print(each.span())
#sub: 매치되는 문자열을 변경
text = """[앵커] 
1
2
3
4
5

[기자] 

6
7
8
9
0"""
# text = re.sub("\[.+\]","",text)
text = re.sub("\[.+\]","=====",text)
print(text)