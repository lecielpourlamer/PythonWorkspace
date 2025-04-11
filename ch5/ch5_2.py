cabinet = {3: "푸", 100: "피글렛"}
print(cabinet[3])   # 푸, key 3에 해당하는 value
print(cabinet[100]) # 피글렛, key 100에 해당하는 value
print(cabinet.get(3)) # 푸, key 3에 해당하는 value

print(cabinet.get(5))
print("hi")
# print(cabinet[5])   # keyError: 5 발생
print("hi")

print(cabinet.get(5)) # None
print(cabinet.get(5, "사용 가능")) # 사용 가능, key에 해당하는 값이 없으면 기본값을 사용하게 함

# key가 딕셔너리 내부의 존재 여부를 확인
print(3 in cabinet) # True
print(5 in cabinet) # False

# key에 정수형뿐만 아니라 문자열도 넣을 수 있다.
cabinet2 = {"A-3": "푸", "B-100": "피글렛"}
print(cabinet2["A-3"])  # 푸
print(cabinet2["B-100"])    # 피글렛


# in 연산자는 문자열에 해당 글자가 포함됐는지 확인할 때도 사용 가능
print("곰" in "곰돌이")     # True
print("돌이" in "곰돌이")   # True
print("푸" in "곰돌이")     # False






