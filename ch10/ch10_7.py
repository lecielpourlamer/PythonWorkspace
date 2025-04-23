try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))

    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")
    
# 첫 번째 숫자를 입력하세요: 6
# 두 번째 숫자를 입력하세요: 2
# 6 / 2 = 3

# 나누기 전용 계산기입니다.
# 첫 번째 숫자를 입력하세요: 10
# 두 번째 숫자를 입력하세요: 5
# 값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.