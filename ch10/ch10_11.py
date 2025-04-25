class SpecialClass():
    def __init__(self):
        print("특별한 생성자")

    def __str__(self):
        return "특별한 메서드"

s = SpecialClass()  # 특별한 생성자 출력
print(s)    # 특별한 메서드 출력

# 특별한 생성자
# 특별한 메서드