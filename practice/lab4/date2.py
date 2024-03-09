import datetime

x = datetime.datetime.now()
print("Today: " + x.strftime("%Y") + "-" + x.strftime("%m") + "-" + str(int(x.strftime("%d"))))
print("Yesterday: " + x.strftime("%Y") + "-" + x.strftime("%m") + "-" + str(int(x.strftime("%d"))-1))
print("Tomorrow: " + x.strftime("%Y") + "-" + x.strftime("%m") + "-" + str(int(x.strftime("%d"))+1))
