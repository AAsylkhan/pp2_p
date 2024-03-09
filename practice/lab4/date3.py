import datetime

x = datetime.datetime.now()

output_datetime = x.replace(microsecond=0)
print(output_datetime)