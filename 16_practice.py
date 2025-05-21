# 日期计算

date = input("请输入日期（格式：YYYY-MM-DD）：")
year, month, day = map(int, date.split("-"))
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# 判断闰年
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days[2] = 29

leap_year(year)

result = 0

for i in range(month):
    result += days[i]
result += day
print("该日期是该年的第", result, "天")