from datetime import date, datetime
import pytz
import time as t

local_timezone = t.tzname[0]

today = date.today()
now = datetime.now()

print("The current date is:", today)
print("The current date and time is:", now)
print("Detected timezone is:", local_timezone)