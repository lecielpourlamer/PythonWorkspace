# 보병: 공격 유닛, 군인, 총을 쏠 수 있음
name = "보병"   # 이름
hp = 40        # 체력
damage = 5      # 공격력


print("{} 유닛을 생성했습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크: 공격 유닛, 포를 쏠 수 있음, 두 가지 모드(일반/시지 모드)
tank_name = "탱크"  
tank_hp = 150
tank_damage = 35

print("{} 유닛을 생성했습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# 새로운 탱크2 추가
tank2_name = "탱크"  
tank2_hp = 150
tank2_damage = 35

print("{} 유닛을 생성했습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))


# 공격 함수
def attack(name, location, damage):
    print("{0} : {1} 방향 적군을 공격합니다.[공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage) # 보병 공격 명령
attack(tank_name, "1시", tank_damage)   # 탱크 공격 명령
attack(tank2_name, "1시", tank2_damage)   # 탱크 공격 명령

# 보병 유닛을 생성했습니다.
# 체력 40, 공격력 5

# 탱크 유닛을 생성했습니다.
# 체력 150, 공격력 35

# 탱크 유닛을 생성했습니다.
# 체력 150, 공격력 35

# 보병 : 1시 방향 적군을 공격합니다.[공격력 5]
# 탱크 : 1시 방향 적군을 공격합니다.[공격력 35]
# 탱크 : 1시 방향 적군을 공격합니다.[공격력 35]