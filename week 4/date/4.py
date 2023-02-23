from datetime import datetime

a=datetime.now()
b=datetime.strptime("13 November 2022, 17:22:56","%d %B %Y, %H:%M:%S")
print((a-b).seconds)




