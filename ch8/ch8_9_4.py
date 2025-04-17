# score.txt 파일을 읽기 모드로 열기
score_file = open("score.txt", "r", encoding="utf-8")

while True:
    line = score_file.readline()
    if not line:    # 더 이상 읽어 올 내용이 없을 때
        break;
    print(line, end="") # 읽어 온 내용 출력

# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100