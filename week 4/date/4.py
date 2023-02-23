from datetime import datetime

a = datetime.now()
b = datetime.strptime("13 November 2022, 17:26:11", "%d %B %Y, %H:%M:%S")
print((a-b).seconds)



