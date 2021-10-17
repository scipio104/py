# divide.py
def divide(divident,divisor):
  quotient=divident/divisor
  rest=divident%divisor
  return quotient,rest
#
dive=int(input("被除数>"))
divo=int(input("除数>"))
quotient,rest=divide(dive,divo)
print("商: %d,余り: %d"% (quotient,rest))
