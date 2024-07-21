#!/usr/bin/env python3
from datetime import date
name = "Dmitry"
# its okay but not perfect, lazy solution 
age = (date.today() - date(1991, 12, 3)).days // 365
is_student = True
print(f'''Name: {name}
Age: {age}''')
age += 1
print(f'''New Age: {age}
Is Student: {is_student}''')
