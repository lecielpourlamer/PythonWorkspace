for waiting_no in [1, 2, 3, 4, 5]:
    print("대기번호 : {0}".format(waiting_no))  # {0} 위치에 waiting_no의 값이 들어감
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4
# 대기번호 : 5
print()

for waiting_no2 in range(5):    # 0부터 5직전까지 (0~4)
    print("대기번호 : {0}".format(waiting_no2))
# 대기번호 : 0
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4
print()

for waiting_no3 in range(1, 6): # 1부터 6직전까지 (1~5)
    print("대기번호 : {0}".format(waiting_no3))
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4
# 대기번호 : 5
print()

for waiting_no4 in range(1, 6, 2):  # 1부터 6직전(1~5)까지 2씩 간격 추가
    print("대기번호 : {0}".format(waiting_no4))
# 대기번호 : 1
# 대기번호 : 3
# 대기번호 : 5

print()
orders = ["아이언맨", "토르", "스파이더맨"] # 손님 닉네임 리스트
for customer in orders:
    print("{0} 님, 커피가 준비됐습니다. 픽업대로 와 주세요.".format(customer))
# 아이언맨 님, 커피가 준비됐습니다. 픽업대로 와 주세요.
# 토르 님, 커피가 준비됐습니다. 픽업대로 와 주세요.
# 스파이더맨 님, 커피가 준비됐습니다. 픽업대로 와 주세요.
