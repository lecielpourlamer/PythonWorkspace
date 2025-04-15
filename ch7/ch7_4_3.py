def buy(item1, item2="음료수"): # 올바른 함수 정의: 일반 전달값을 먼저 작성
    print(item1, item2)

buy("빵")
# 빵 음료수

# def buy2(item1="음료수", item2): # 잘못된 함수 정의: 기본값이 있는 전달값을 먼저 작성
#     print(item1, item2)

# buy("빵")
# SyntaxError: non-default argument follows default argument