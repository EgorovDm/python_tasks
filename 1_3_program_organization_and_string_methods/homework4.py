#!/usr/bin/env python3

my_string = input("Input text, and press enter:")

print(f'''
{"="*20}
text length: {len(my_string)}
UPPERCASE: {my_string.upper()}
lowercase: {my_string.lower()}
first char: {my_string[0]}
last char: {my_string[-1]}
{"="*20}
''')
