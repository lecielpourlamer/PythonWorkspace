python = "Python is Amazing"

print(python.lower())   # 전체 소문자로 변환
print(python.upper())   # 전체 대문자로 변환
print(python[0].isupper())  # 인덱스 0에 있는 값이 대문자인지 확인
print(python[1:3].islower())    # 인덱스 1부터 2에 있는 값이 소문자인지 확인
print(python.replace("Python", "Java")) # Python을 Java로 바꾸기