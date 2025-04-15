def open_account(): # 계좌 개설 함수
    print("새로운 계좌를 개설합니다.")

open_account()  # open_account() 함수 호출

def deposit(balance, money):    # 입금 처리 함수
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money  # 입금 후 잔액 정보 반환

def withdraw(balance, money):   # 출금 처리 함수
    if balance >= money:    # 잔액이 출금액보다 많으면
        print("{0}원을 출금했습니다. 잔액은 {1}원입니다.".format(money, balance - money))
        return balance - money  # 출금 후 잔액 반환
    else:
        print("잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))
        return balance  # 기존 잔액 반환
    
balance = 0 # balance 변수에 초깃값으로 0 저장
balance = deposit(balance, 1000)    # 1,000원 입금, balance 변수에 deposit() 함수의 반환값을 다시 저장

# 출금
balance = withdraw(balance, 2000)   # 2,000원 출금 시도
balance = withdraw(balance, 500)    # 500원 출금 시도

# 새로운 계좌를 개설합니다.
# 1000원을 입금했습니다. 잔액은 1000원입니다.
# 잔액이 부족합니다. 잔액은 1000원입니다.
# 500원을 출금했습니다. 잔액은 500원입니다.