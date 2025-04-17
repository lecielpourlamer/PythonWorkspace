# score.txt 파일을 읽기 모드로 열기
score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.read())    # 파일 전체 읽어 오기
score_file.close()

# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100