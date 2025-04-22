class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()  # 부모 클래스의 생성자를 호출

# 수송선
troopship = FlyableUnit()

# Flyable 생성자