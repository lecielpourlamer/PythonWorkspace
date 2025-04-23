try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except  ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")
except ZeroDivisionError as err:
    print(err)

# 나누기 전용 계산기입니다.
# 첫 번째 숫자를 입력하세요 : 6
# 두 번째 숫자를 입력하세요 : 0
# division by zero