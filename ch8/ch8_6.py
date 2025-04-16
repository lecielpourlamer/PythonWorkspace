scores = {"수학": 0, "영어": 50, "코딩": 100}

for subject, score in scores.items():   # (key, value)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 수학      :   0
# 영어      :  50
# 코딩      : 100