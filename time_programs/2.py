from datetime import *
import pytz

tz_INDIA = pytz.timezone('Asia/Kolkata')

print(datetime.now(tz=tz_INDIA).date())
print(datetime.now(tz=tz_INDIA).time())

print(datetime.utcnow())
