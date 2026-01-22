
# functions.py
# def 함수명([파라미터=매개변수=아규먼트]):
#  함수내코드

# 내장함수사용
print()
print('Hello python')
print(str(10))

# 함수정의(매개변수가 없는 것)
def sayHello1():
   # pass  #코드 오류를 방지(무시)하는 기능
    print('Hello Everyone~')
    # return None 이 숨어있는 형태

# 매개변수 사용
def sayHello2(name):
    print('Hello~ Im + name')
    print("Hello~ I'm "+ name)

#매개변수 사용 + 반환
def add(x, y):
    result = x + y
    return result

# 매개변수 없이 반환하는 함수
def process():
    result = 'Done'
    return result

# 커스텀함수 사용(호출)
sayHello1()

# 함수호출(매개변수사용)
sayHello2('명건')
sayHello2('애슐리')

sum = add(10,5)
# sum = 15
print(sum)

print(process())    #   print('Done') 와 동일 

def get_user_info(id):
    # DB에서 개인정보를 가져옴
    info = None
    return info