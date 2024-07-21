#!/usr/bin/env python3
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

name = "Dmitry"
age = relativedelta(
    datetime.now(), 
    datetime(1991,12,3,7,0,0,0)
).years
is_student = True
print(f'''Name: {name}
Age: {age}''')
age += 1
print(f'''New Age: {age}
Is Student: {is_student}''')
