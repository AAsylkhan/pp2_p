import datetime

x = datetime.datetime.now()
print(x.strftime("%Y") + "-" + x.strftime("%m") + "-" + str(int(x.strftime("%d"))-5))
