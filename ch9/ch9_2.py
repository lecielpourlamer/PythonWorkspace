class Unit:
    def __init__(self, name, hp, damage):   # 생성자, self 외 전달값 3개
        self.name = name        # 인스턴스 변수 name에 전달값 name 저장
        self.hp = hp            # 인스턴스 변수 hp에 전달값 hp 저장
        self.damage = damage    # 인스턴스 변수 damage에 전달값 damage 저장
        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

soldier1 = Unit("보병", 40, 5)  # 보병1 생성, 전달값으로 이름/체력/공격력 전달
soldier2 = Unit("보병", 40, 5)  # 보병2 생성, 전달값으로 이름/체력/공격력 전달
tank = Unit("탱크", 150, 35)    # 탱크 생성, 전달값으로 이름/체력/공격력 전달

# 보병 유닛을 생성했습니다.
# 체력 40, 공격력 5
# 보병 유닛을 생성했습니다.
# 체력 40, 공격력 5
# 탱크 유닛을 생성했습니다.
# 체력 150, 공격력 35

# 전투기: 공중 유닛, 은폐 불가
stealth1 = Unit("전투기", 80, 5)    # 객체 생성, 체력 80, 공격력 5

# 인스턴스 변수 접근
print("유닛 이름 : {0}, 공격력 : {1}".format(stealth1.name, stealth1.damage))

# 전투기 유닛을 생성했습니다.
# 체력 80, 공격력 5
# 유닛 이름 : 전투기, 공격력 : 5

# 은폐 가능 
stealth2 = Unit("업그레이드 한 전투기", 80, 5)

# 업그레이드한 전투기만을 위한 특별한 인스턴스 변수 정의, 은폐 상태
stealth2.cloaking = True
if stealth2.cloaking == True:   # 은폐 상태라면
    print("{0}는 현재 은폐 상태입니다.".format(stealth2.name))

if stealth1.cloaking == True:   # 다른 전투기의 은폐 여부
    print("{0}는 현재 은폐 상태입니다.".format(stealth1.name))
# AttributeError: 'Unit' object has no attribute 'cloaking'







