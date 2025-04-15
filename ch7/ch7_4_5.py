def profile(name, age, main_lang):  # 키워드 인자 : name, age, main_lang
    print(name, age, main_lang)

profile("찰리", age=20, main_lang="파이썬")    # 올바른 함수 호출: 일반 전달값을 먼저 작성
profile(name="루시", 25, "파이썬")  # 잘못된 함수 호출: 키워드 인자를 먼저 작성

# SyntaxError: positional argument follows keyword argument