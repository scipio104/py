# reidai453.py
import sys
age=int(sys.argv[1])
sex=sys.argv[2]
country=sys.argv[3]
if (age>=20 and age<60) and sex=="M" and \
    (country=="JP" or country=="CN"):
    print("いらっしゃいませ！")
else:
    print("お引き取りください！")
