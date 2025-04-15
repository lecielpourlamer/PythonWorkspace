def profile(name, age=20, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("찰리")
profile("케빈", 22)
profile("루시", 24, "자바")

# 이름 : 찰리     나이 : 20       주 사용 언어 : 파이썬
# 이름 : 케빈     나이 : 22       주 사용 언어 : 파이썬
# 이름 : 루시     나이 : 24       주 사용 언어 : 자바

