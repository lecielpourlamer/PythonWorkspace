# score.txt 파일을 쓰기 모드로 열기
score_file = open("score.txt", "w", encoding="utf-8")
print("수학 : 0", file=score_file)  # score.txt 파일에 내용 쓰기
print("영어 : 50", file=score_file) # score.txt 파일에 내용 쓰기
score_file.close()  # score.txt 파일 닫기


