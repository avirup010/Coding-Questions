#Calendar Module in Python
# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime
import calendar

m, d, y = map(int, input().split())
input_date = datetime.date(y, m, d)
print(calendar.day_name[input_date.weekday()].upper())
