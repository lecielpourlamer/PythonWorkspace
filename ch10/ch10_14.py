class SoldOutError(Exception):
    pass

chicken = 10    # 남은 치킨 수
waiting = 1     # 대기번호, 1부터 시작

while True:
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨을 몇 마리 주문하시겠습니까? "))
        
        if order > chicken:     # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리를 주문했습니다.".format(waiting, order))
            waiting += 1        # 대기번호 1 증가
            chicken -= order    # 주문 수만큼 남은 치킨 감소
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력했습니다.")
    except SoldOutError:
        print("재료가 소진돼 더 이상 주문을 받지 않습니다.")
        break

# [남은 치킨 : 10]
# 치킨을 몇 마리 주문하시겠습니까? 5 
# [대기번호 1] 5마리를 주문했습니다.
# [남은 치킨 : 5]
# 치킨을 몇 마리 주문하시겠습니까? 3
# [대기번호 2] 3마리를 주문했습니다.
# [남은 치킨 : 2]
# 치킨을 몇 마리 주문하시겠습니까? 0
# 잘못된 값을 입력했습니다.
# [남은 치킨 : 2]
# 치킨을 몇 마리 주문하시겠습니까? -10
# 잘못된 값을 입력했습니다.
# [남은 치킨 : 2]
# 치킨을 몇 마리 주문하시겠습니까? 4
# 재료가 부족합니다.
# [남은 치킨 : 2]
# 치킨을 몇 마리 주문하시겠습니까? 삼
# 잘못된 값을 입력했습니다.
# [남은 치킨 : 2]
# 치킨을 몇 마리 주문하시겠습니까? 2
# [대기번호 3] 2마리를 주문했습니다.
# 재료가 소진돼 더 이상 주문을 받지 않습니다.