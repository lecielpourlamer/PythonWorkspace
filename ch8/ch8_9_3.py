# score.txt 파일을 읽기 모드로 열기
score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline(), end="")    # 한 줄씩 읽어 오고, 커서는 다음 줄로 이동
print(score_file.readline(), end="")    # end 값을 설정해 줄 바꿈 중복 수행 방지
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100