import datetime

today = datetime.date.today()           # 오늘 날짜 저장
td = datetime.timedelta(days=100)       # 100일째 날짜 저장
print("오늘은", today)                         
print("우리가 만난 지 100일은", today + td) # 오늘부터 100일 후 날짜

# 오늘은 2025-04-29
# 우리가 만난 지 100일은 2025-08-07