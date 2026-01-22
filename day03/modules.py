# modules.py - 모듈 내장함수확인
# import 모듈명

import math # 수학관련된 함수와 데이터 담고있는 모듈

pi = 3.141592

radius = 10

result = radius * radius * pi
print('간단 원의 넓이는 ' + str(result))

result = radius * radius * math.pi
print(math.pi)
print('복잡 원의 넓이는 ' + str(result))

#수학 모듈 계속
print(math.sqrt(16))
print(math.floor(4.9)) # 바닥, 숫자내림
print(math.ceil(4.3))   #숫자올림

import datetime # 날짜시간 모듈

print(datetime.datetime.now())

## 내장함수
# 배열, 문자열 길이 리턴 함수 
print(len('Hello')) # len 문자열의 길이, 문자에만 사용가능, 숫자는 불가
print(len([1,2,3,4,5,6]))   #문자배열에도 len사용가능

print(type(1))  #int는 정수 
print(type(pi)) #float은 실수
print(type([1,2,3,4]))  #배열에도 사용가능, list
print(type('Hello'))    #str은 문자열이라는 뜻

print(int(80))  #int는 숫자만, 문자는 사용불가
print(int('80'))    # 정수형으로 된 문자열만 변환이 가능
print(float('4.6')) # 정수형, 실수형 둘다 모두 변환이 가능, 그러나 문자는 불가능
print(str(3.141592))    # str은 모두 다 된다