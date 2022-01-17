import datetime
import pytz


now = datetime.datetime.now()
time_zone = pytz.timezone("Europe/Kiev")
time_in_kyiv = time_zone.localize(datetime.datetime.now())

print("Hour: ", now.hour)
print("Date and month: ", now.day, "\t", now.month)
print("Time zone: ", time_zone)
print("Time in Kiev: ", time_in_kyiv)
# print(type(time_in_kyiv))
# print(time_in_kyiv.month)