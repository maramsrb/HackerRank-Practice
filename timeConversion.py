#Given a time in -hour AM/PM format, convert it to military (24-hour) time.
#Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
#- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.


def timeConversion(s):
  #corta la cadena dependiendo si es AM o PM
  x=s[-2:]
  
  if x=='PM' and s[:2] != '12':
    calc = int(s[:2]) + 12
    res = str(calc) + s[-8:-2]
  #  print('res1: ' + s[:2])
  elif s[:2] == '12' and x == 'AM':
    res= '00' + s[2:8]
  else:
    res = s[:-2]  


  print(res)     




timeConversion("04:59:59AM")