#!/usr/bin/env python3
import pandas as pd
import numpy as np
from tabulate import tabulate
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
df = pd.DataFrame(data=grades).T
df.columns = list(students)

print(" "*20 + "STUDENT GRADES\n",
    tabulate(df, headers='keys', tablefmt='outline'),
    '\n',
    sep='')

print(df.describe())

print(f'''
MEAN dict: {dict(df.mean())}
''')
