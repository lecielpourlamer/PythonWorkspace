def open_account(): # 계좌 개설 함수
    print("새로운 계좌를 개설합니다.")

open_account()  # open_account() 함수 호출

def deposit(balance, money):    # 입금 처리 함수
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money  # 입금 후 잔액 정보 반환

def withdraw_night(balance, money): # 업무 시간 외 출금
    commission = 100    # 출금 수수료 100원
    print("업무 시간 외에 {}원을 출금했습니다.".format(money))
    return commission, balance - money - commission
    
balance = 0 # balance 변수에 초깃값으로 0 저장
balance = deposit(balance, 1000)    # 1,000원 입금, balance 변수에 deposit() 함수의 반환값을 다시 저장

# 업무 시간 외 출금 시도
# 튜플 형태로 반환한 값 2개를 각각 변수에 저장
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

# 새로운 계좌를 개설합니다.
# 1000원을 입금했습니다. 잔액은 1000원입니다.
# 업무 시간 외에 500원을 출금했습니다.
# 수수료 100원이며, 잔액은 400원입니다.