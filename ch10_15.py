def save_battery(level):
    try:
        print(f"배터리 잔량 : {level}%")    # 배터리 잔량 표시

        if level > 30:
            print("일반 모드로 사용합니다.")
        elif level > 5:
            print("절전 모드로 사용합니다.")
        else:
            raise Exception("배터리가 부족해 스마트폰을 종료합니다.")   # 오류 발생
    except Exception as e:
        print(e)
    print()

# 테스트 코드
save_battery(75)
save_battery(25)
save_battery(3)

# 배터리 잔량 : 75%
# 일반 모드로 사용합니다.

# 배터리 잔량 : 25%
# 절전 모드로 사용합니다.

# 배터리 잔량 : 3%
# 배터리가 부족해 스마트폰을 종료합니다.