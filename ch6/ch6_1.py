weather = "비"

if weather == "비":     # 대입 연산자(=)가 아닌 비교 연산자(==) 사용
    print("우산을 챙기세요.")


weather2 = "맑음"

if weather2 == "비":
    print("우산을 챙기세요.")


weather3 = "미세먼지"

if weather3 == "비":
    print("우산을 챙기세요.")  # 1번
elif weather3== "미세먼지":
    print("마스크를 챙기세요.") # 2번

print()

weather4 = "맑음"

if weather4 == "비":
    print("우산을 챙기세요.")
elif weather4 == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")

print()
# input()으로 값 입력받아 비교하기
# weather5 = input("오늘 날씨 어때요? ")
# print(weather5)

print()
weather6 = input("오늘 날씨 어때요? ")
if weather6 == "비":
    print("우산을 챙기세요.")
elif weather6 == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")














