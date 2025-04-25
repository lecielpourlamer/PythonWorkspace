class BigNumberError(Exception):    # 사용자 정의 예외 처리, Exception 클래스 상속
    pass

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))

    if num1 >=10 or num2 >= 10:     # 입력받은 수가 한 자리인지 확인
        # raise ValueError
        raise BigNumberError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError:      # 사용자 정의 예외 처리
    print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")

# 한 자리 숫자 나누기 전용 계산기입니다.
# 첫 번째 숫자를 입력하세요 : 10
# 두 번째 숫자를 입력하세요 : 5
# 오류가 발생했습니다. 한 자리 숫자만 입력하세요.