from datetime import datetime, timedelta


y= (datetime.now () + timedelta (days = -7))
y1= (datetime.now () + timedelta (days = 7))

with open ('111.txt', 'w') as a:
    a.write(y,y1)