import datetime
import calendar

# 取當前的年月日
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day

# 用monthrange取當月有多少天，輸出為tuple型態
# 輸出的第一個元素為這個月第一天的星期碼（0為星期一, 1為星期二）
# 輸出的第二個元素為這個月的天數有多少
day_in_month = calendar.monthrange(year, month)

# 當day超過當月天數時，自動跳下個月
if day > day_in_month[1]:
    month += 1
    if month > 12:
        year += 1
        month = 1
    day = 1

print(f'now time {year}/{month}/{day}')