from datetime import timedelta,datetime

print('yesterday',datetime.now() + timedelta(days=-1))
print('today',datetime.now())
print('tomorrow',datetime.now() + timedelta(days = 1))




