# reidai451.py
import sys
age=int(sys.argv[1])
sex=sys.argv[2]
country=sys.argv[3]
if age<50 and sex=="M" and country=="KR":
    print("いらっしゃいませ！")
else:
    print("お引き取りください！")
