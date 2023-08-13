# def 함수이름(매개변수1, 매개변수2, ...):
#     # 함수 내용
#     return 반환값

# 결과 = 함수이름(인자1, 인자2, ...)

# if 조건:
#     # 들여쓰기로 블록 시작
#     코드 블록 내용
#     # 블록 끝


# for 요소 in 시퀀스:
#     # 들여쓰기로 블록 시작
#     코드 블록 내용
#     # 블록 끝

# 함수 정의
def 함수이름(매개변수):
    print("함수가 호출되었습니다.")
    return 매개변수 + 10


# 함수 호출
결과 = 함수이름(5)
print("결과:", 결과)


def add(a, b):
    result = a + b
    return result


sum_result = add(3, 5)
print(sum_result)  # 출력: 8


# 기본 매개변수 예제
def 함수이름(매개변수1, 매개변수2=10):  # 기본 값이 지정되지 않은 매개변수는 "필수" 매개변수이다.
    return 매개변수1 + 매개변수2


결과1 = 함수이름(5)  # 매개변수2에 값이 전달되지 않아 기본 값 10이 사용됩니다.
결과2 = 함수이름(5, 3)  # 매개변수2에 값 3이 전달되어 기본 값 대신 사용됩니다.
print(결과1, 결과2)  # 출력 결과: 15 8


# "기본 매개변수는 필수 매개변수 뒤에 와야 한다" 예제
def 올바른함수(필수매개변수, 기본매개변수=10):
    return 필수매개변수 + 기본매개변수


print(올바른함수(5))  # 출력 결과: 15


# def 잘못된함수(기본매개변수=10, 필수매개변수):  # 문법 오류
#     return 기본매개변수 + 필수매개변수


# print(잘못된함수(5))  # 이 코드는 실행되지 않습니다.


# 인수를 지정해서 함수를 호출하기
# 함수 정의
def 예제함수(이름, 나이, 성별):
    print(f"이름: {이름}, 나이: {나이}, 성별: {성별}")


# 키워드 인수를 사용하여 함수 호출
예제함수(이름="홍길동", 나이=30, 성별="남")
예제함수(나이=25, 성별="여", 이름="이순신")


# 출력 결과:
# 이름: 홍길동, 나이: 30, 성별: 남
# 이름: 이순신, 나이: 25, 성별: 여


# 인수를 지정해서 함수를 호출 할 때 주의 사항
def 예제함수(이름, 나이, 성별):
    print(f"이름: {이름}, 나이: {나이}, 성별: {성별}")


# 잘못된 인수명
# 예제함수(name="홍길동", 나이=30, 성별="남")  # TypeError

# 위치 인수와 키워드 인수의 순서 오류
# 예제함수("홍길동", 성별="남", 30)  # SyntaxError

# 중복 인수 전달
# 예제함수("홍길동", 나이=30, 성별="남", 나이=25)  # TypeError


# 가변길이 위치인수 - *args
def 합계(*숫자들):
    결과 = 0
    for 숫자 in 숫자들:
        결과 += 숫자
    return 결과


print(합계(1, 2, 3, 4, 5))  # 출력 결과: 15


# 가변길이 키워드인수 - **kwargs
def 프로필(**정보):
    for 키, 값 in 정보.items():
        print(f"{키}: {값}")


프로필(이름="홍길동", 나이=30, 성별="남")


# 출력 결과:
# 이름: 홍길동
# 나이: 30
# 성별: 남


# 가변길이 위치인수와 키워드인수는 함께 쓸 수 있다
def 예제함수(*args, **kwargs):
    print("위치 인수:", args)
    print("키워드 인수:", kwargs)


예제함수(1, 2, 3, 이름="홍길동", 나이=30)


# 출력 결과:
# 위치 인수: (1, 2, 3)
# 키워드 인수: {'이름': '홍길동', '나이': 30}


# 가변길이 인수 주의사항
# 잘못된 매개변수 순서
# def 잘못된함수1(**kwargs, *args):  # SyntaxError
#     pass
#
# # 중복 사용
# def 잘못된함수2(*args, *more_args):  # SyntaxError
#     pass
#
# def 잘못된함수3(**kwargs, **more_kwargs):  # SyntaxError
#     pass

# 중복 인수 전달
def 예제함수(*args, **kwargs):
    pass


# 예제함수(1, a=2, 3)  # TypeError, 위치 인수와 키워드 인수가 중복됨


def 가변함수1(*args, a):
    print("가변 위치 인수:", args)
    print("키워드 전용 인수:", a)


가변함수1(1, 2, 3, a=4)
# 출력 결과:
# 가변 위치 인수: (1, 2, 3)
# 키워드 전용 인수: 4

# return 예제 - case 1
def 더하기(a, b):
    return a + b

결과 = 더하기(3, 5)
print(결과)  # 출력 결과: 8


# return 예제 - case 2
def 계산(a, b):
    return a + b, a - b

덧셈결과, 뺄셈결과 = 계산(10, 5)
print(덧셈결과, 뺄셈결과)  # 출력 결과: 15 5


# reurn 예제 - case 3
def 양수판별(number):
    if number < 0:
        return "음수입니다."
    return "양수입니다."

print(양수판별(-5))  # 출력 결과: 음수입니다.

# reurn 예제 - case 4
def 메시지출력():
    print("안녕하세요!")

결과 = 메시지출력()
print(결과)  # 출력 결과: None
