from theater_module import price, price_morning     # 모듈에서 일부 함수만 가져와 사용함

price(5)            # 5명
price_morning(6)    # 6명
price_soldier(7)    # import하지 않아서 사용 불가

# 5명, 영화표 가격은 50000원입니다.
# 6명, 조조 할인 영화표 가격은 36000원입니다.
# Traceback (most recent call last):
#   File "c:\Users\shlim\Desktop\PythonWorkspace\ch11\ch11_4.py", line 5, in <module>
#     price_soldier(7)    # import하지 않아서 사용 불가
# NameError: name 'price_soldier' is not defined