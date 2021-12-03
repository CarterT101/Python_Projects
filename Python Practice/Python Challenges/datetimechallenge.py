


from datetime import datetime
import pytz


tz_NewYork = pytz.timezone("EST")
dt_NewYork = datetime.now(tz_NewYork)

tz_Portland = pytz.timezone("PST8PDT")
dt_Portland = datetime.now(tz_Portland)

tz_London = pytz.timezone("GMT")
dt_London = datetime.now(tz_London)

dt_Open = datetime(2021,12,2,9,0,0)

dt_Closed = datetime(2021,12,2,17,0,0)



opennow = dt_Open.strftime("%H:%M:%S")
closednow = dt_Closed.strftime("%H:%M:%S")


portland = dt_Portland.strftime("%H:%M:%S")
newyork = dt_NewYork.strftime("%H:%M:%S")
london = dt_London.strftime("%H:%M:%S")



if london > closednow:
    print("London location is closed")
else:
    print("London location is open")

if portland > closednow:
    print("Portland location is closed")
else:
    print("Portland location is open")

if newyork > closednow:
    print("New York location is closed")
else:
    print("New York location is open")



