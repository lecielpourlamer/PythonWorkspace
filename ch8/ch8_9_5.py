# score.txt 파일을 읽기 모드로 열기
score_file = open("score.txt", "r", encoding="utf-8")

lines = score_file.readlines()  # 파일에서 모든 줄을 읽어 와 리스트 형태로 저장
for line in lines:  # lines에 내용이 있을 때까지
    print(line, end="")

score_file.close()

# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100