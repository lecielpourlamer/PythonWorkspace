# 일반 유닛
class Unit:   # 공격 유닛
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # Unit 클래스 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)   # 부모 클래스의 생성자 호출
        self.damage = damage

    def attack(self, location):  # 전달받은 방향으로 공격
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]" \
              .format(self.name, location, self.damage))
    
    def damaged(self, damage):  # damage 만큼 유닛 피해
        # 피해 정보 출력
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage   # 유닛의 체력에서 전달받은 damage 만큼 감소
        # 남은 체력 출력
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:    # 남은 체력이 0 이하이면
            print("{0} : 파괴됐습니다.".format(self.name))  # 유닛 파괴 처리

# 비행 기능
class Flyable:
    def __init__(self, flying_speed):   # 비행 속도
        self.flying_speed = flying_speed

    def fly(self, name, location):  # 유닛 이름, 비행 방향
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
              .format(name, location, self.flying_speed))


# 공중 공격 유닛'
class FlyableAttackUnit(AttackUnit, Flyable):
    # 유닛 이름, 체력, 공격력, 비행 속도
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage) # 유닛 이름, 체력, 공격력
        Flyable.__init__(self, flying_speed)    # 비행 속도

# 요격기: 공중 공격 유닛, 미사일 여러 발을 한 번에 발사
# 유닛 이름, 체력, 공격력, 비행 속도
interceptor = FlyableAttackUnit("요격기", 200, 6, 5)
interceptor.fly(interceptor.name, "3시")    # 3시 방향으로 이동



