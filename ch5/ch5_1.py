subway = [10, 20, 30]
print(subway)   # [10, 20, 30]

subway1 = ["푸", "피글렛", "티거"]
print(subway1)  # ['푸', '피글렛', '티거']

# 피글렛이 몇 번째 칸에 탔는가?
print(subway1.index("피글렛")) # 1

subway1.append("이요르")
print(subway1)  # ['푸', '피글렛', '티거', '이요르']

# 루를 푸와 피글렛 사이(인덱스 1 위치)에 삽입
subway1.insert(1, "루")
print(subway1)  # ['푸', '루', '피글렛', '티거', '이요르']

# 지하철 역마다 한 명씩 내림
print(subway1.pop()) # 이요르
print(subway1)  # ['푸', '루', '피글렛', '티거']

print(subway1.pop()) # 티커
print(subway1)  # ['푸', '루', '피글렛']

print(subway1.pop()) # 피글렛
print(subway1)  # ['푸', '루']

subway1.clear()
print(subway1)  # []

subway2 = ["푸", "피글렛", "티거"]
subway2.append("푸")
print(subway2)  # ['푸', '피글렛', '티거', '푸']
print(subway2.count("푸")) # 2

num_list = [5, 4, 3, 2, 1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]

num_list.sort(reverse=True) # 내림차순 정렬
print(num_list) # [5, 4, 3, 2, 1]

num_list.reverse()  # 순서 뒤집기
print(num_list) # [1, 2, 3, 4, 5]

my_list = [1, 3, 2]
my_list.sort()  # 리스트 정렬
print(my_list)  # [1, 2, 3] my_list 리스트 데이터 변경

your_list = [5, 7, 6]
new_list = sorted(your_list)    # 정렬할 리스트를 소괄호 안에 넣음
print(sorted(your_list))    # [5, 6, 7]
print(your_list)    # [5, 7, 6] your_list 리스트 데이터는 변경되지 않음
print(new_list) # [5, 6, 7] 정렬된 새로운 리스트

mix_list = ["푸", 20, True, [5, 2, 4, 3, 1]]
print(mix_list) # ['푸', 20, True, [5, 2, 4, 3, 1]]

mix_list2 = ["푸", 20, True]
num_list2 = [5, 2, 4, 3, 1]
num_list2.extend(mix_list2) # 리스트 합치기
print(mix_list2)    # ['푸', 20, True]
print(num_list2)    # [5, 2, 4, 3, 1, '푸', 20, True]


