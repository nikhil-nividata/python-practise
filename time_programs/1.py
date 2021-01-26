from datetime import *
import pytz
print(datetime.now().time())

tz_INDIA = pytz.timezone('Asia/Kolkata')

print(datetime.now(tz=tz_INDIA).time())
