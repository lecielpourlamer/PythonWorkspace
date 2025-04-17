import pickle

with open("study.txt", "w", encoding="utf8") as study_file:    # 새로운 파일 생성
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

# 파이썬을 열심히 공부하고 있어요.
