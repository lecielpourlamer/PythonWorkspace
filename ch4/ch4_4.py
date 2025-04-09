python = "Python is Amazing"

find = python.find("n")     # 처음 발견한 n의 인덱스
print(find)                 # 'Python'에서 n(인덱스 5)

find = python.find("n", find + 1)   # 인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스
print(find)                         # ' is Amazing'에서 n(인덱스 15)

find = python.find("Java")          # Java가 없으면 -1을 반환(출력 후) 프로그램 계속 수행
print(find)

index = python.index("n")           # 처음 발견한 n의 인덱스
print(index)                        # 'Python'에서 n=5

index = python.index("n", index + 1)    # 인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스
print(index)                            # ' is Amazing'에서 n=15

index = python.index("n", 2, 6)         # 인덱스 2부터 6 직전까지 찾아 처음 발견한 n의 인덱스
print(index)                            # 'thon'에서 n(인덱스 5)

# index = python.index("java")            # Java가 없으면 오류가 발생하여 프로그램 종료
# print(index)                            # ValueError: substring not found

print()
print(python.count("n"))    # count() 함수 - 지정한 문자 또는 문자열이 총 몇 번 나오는지 횟수를 확인 2
print(python.count("v"))    # 0
print(len(python))          # len(문자열 또는 변수) 함수 - 문자열의 길이 정보 출력
