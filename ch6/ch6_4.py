students = [1, 2, 3, 4, 5]
print(students)
# [1, 2, 3, 4, 5]

# 한 줄 for문으로 각 항목에 100 더하기
students = [i + 100 for i in students]
print(students)
# [101, 102, 103, 104, 105]

students2 = ["Iron man", "Thor", "Spider Man"]
print(students2)
# ['Iron man', 'Thor', 'Spider Man']

# 한 줄 for문으로 각 이름을 이름의 길이 정보로 변환
students2 = [len(i) for i in students2]
print(students2)
# [8, 4, 10]

students3 = ["Iron man", "Thor", "Spider Man"]
print(students3)
# ['Iron man', 'Thor', 'Spider Man']

# 한 줄 for문으로 각 이름을 이름의 길이 정보로 변환
students3 = [i.upper() for i in students3]
print(students3)
# ['IRON MAN', 'THOR', 'SPIDER MAN']
