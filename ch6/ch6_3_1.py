customer = "아이언맨"   # 손님 닉네임
index = 1

while True:
    print("{0} 님, 커피가 준비됐습니다. 호출 {1}회".format(customer, index))
    index += 1

# ...
# 아이언맨 님, 커피가 준비됐습니다. 호출 38797회
# 아이언맨 님, 커피가 준비됐습니다. 호출 38798회
# 아이언맨 님, 커피가 준비됐습니다. 호출 38799회
# Traceback (most recent call last):
#   File "c:\Users\shlim\Desktop\PythonWorkspace\ch6\ch6_3_1.py", line 5, in <module>
#     print("{0} 님, 커피가 준비됐습니다. 호출 {1}회".format(customer, index))
# KeyboardInterrupt