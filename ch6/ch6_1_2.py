temp = int(input("오늘 기온은 어때요? "))   # 입력값을 정수형으로 형변환

if 30 <= temp:  # 30도 이상이면
    print("너무 더워요. 외출을 자제하세요.")
elif 10 <= temp and temp < 30:  # 10도 이상 30도 미만이면
    print("활동하기 좋은 날씨예요.")
elif 0 <= temp and temp < 10:   # 0도 이상 10도 미만이면
    print("외투를 챙기세요.")
else: # 그 외의 모든 경우(0도 미만이면)
    print("너무 추워요. 나가지 마세요.")