absent = [2, 5] # 결석한 학생 출석번호
no_book = [7]   # 책을 가져오지 않은 학생 출석번호

for student in range(1, 11):    # 출석번호 1~10번
    if student in absent:       # 결석한 학생이면
        continue        # 다음 학생으로 넘어가기
    elif student in no_book:    # 책을 가져오지 않으면 바로 수업 종료
        print("오늘 수업은 여기까지. {0}번 학생은 교무실로 따라와요.".format(student))
        break   # 반복문 탈출
    print("{0}번 학생, 책을 읽어 보세요".format(student))

# 1번 학생, 책을 읽어 보세요
# 3번 학생, 책을 읽어 보세요
# 4번 학생, 책을 읽어 보세요
# 6번 학생, 책을 읽어 보세요
# 오늘 수업은 여기까지. 7번 학생은 교무실로 따라와요.
