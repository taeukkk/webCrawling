import re

text = """
jkilee@gmail.com
kttredef@naver.com
akdef!aa.com
adekik@best.kr
abkereff@aacde
adefgree@korea.co.kr
"""

for each in re.finditer("[a-zA-z0-9]+@[a-z]+(\.[a-z]{2,3}){1,2}",text):
    print(each.group())