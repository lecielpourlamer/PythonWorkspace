import pickle   # pickle 모듈 가져다 쓰기

profile_file = open("profile.pickle", "wb") # 바이너리 형태로 저장

profile = {"이름" : "스누피", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
print(profile)

pickle.dump(profile, profile_file)  # profile 데이터를 profile.pickle 파일에 저장
profile_file.close()    # 파일 닫기

# 바이너리 파일을 읽기 모드 r에 b를 붙여서 rb로 작성
# load() 함수에 파일명을 전달하면 파일에서 데이터를 불러와 profile 변수에 그대로 저장
profile_file = open("profile.pickle", "rb") # 읽어 올 때도 바이너리 형태 명시
profile = pickle.load(profile_file)         # 파일에 있는 정보를 불러와서 profile에 저장

print(profile)
profile_file.close()

# {'이름': '스누피', '나이': 30, '취미': ['축구', '골프', '코딩']}
# {'이름': '스누피', '나이': 30, '취미': ['축구', '골프', '코딩']}