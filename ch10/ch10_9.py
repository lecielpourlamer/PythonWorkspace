class BigNumberError(Exception):    # 사용자 정의 예외 처리, Exception 클래스 상속
    def __init__(self, msg):        # 오류 메시지 msg를 전달받아 인스턴스 변수로 설정
        self.msg = msg

    def __str__(self):              # 인스턴스 변수 msg르 반환
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))

    if num1 >=10 or num2 >= 10:     # 입력받은 수가 한 자리인지 확인
        # 자세한 오류 메시지
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:      # 사용자 정의 예외 처리
    print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err)      # 오류 메시지 출력

# 한 자리 숫자 나누기 전용 계산기입니다.
# 첫 번째 숫자를 입력하세요 : 10
# 두 번째 숫자를 입력하세요 : 5
# 오류가 발생했습니다. 한 자리 숫자만 입력하세요.
# 입력값 : 10, 5