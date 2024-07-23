#!/usr/bin/env python3
import sys
import numpy as np
import traceback

# dict with test data
test_dict = {
    '3': '12',
    '4': '13',
    '5': '1423',
    '6': '121524',
    '7': '162534',
    '8': '13172635',
    '9': '1218273645',
    '10': '141923283746',
    '11': '11029384756',
    '12': '12131511124210394857',
    '13': '112211310495867',
    '14': '1611325212343114105968',
    '15': '1214114232133124115106978',
    '16': '1317115262143531341251161079',
    '17': '11621531441351261171089',
    '18': '12151811724272163631545414513612711810',
    '19': '118217316415514613712811910',
    '20': '13141911923282183731746416515614713812911'
}

dbg_msg = '''
========================================================================
Key is {k}, sequence is {v}
Keys with p-value > {p}: {key}
========================================================================
'''

# Splits can be x y, x yy because first number is less than second
# lets solve this problem from signal stand point. We have som sequence, that needs to 
# trigger if sum of split equal to devisors of key. We can design filter to calculate 
# rolling sum on input, because, by conditions, we have no idea if input data is in sync 
# (if we are not in t=0). The IRs of filters would be [1,1] and [1, 10, 1], than we can 
# match filters with devisors of key, mark matched region as true an combine sequences with or

def calc_devisors(num: int) -> list:
    '''Calculates all devisors of number'''
    devisors = []
    pg_div, rem = num // 2, num % 2
    if rem == 0: 
        devisors.append(2)
    for i in range(3, pg_div):
        if not (num % i): 
            devisors.append(i)
    if rem == 0 and pg_div != 2: 
        devisors.append(pg_div)
    devisors.append(num)
    return devisors

# dict of devisors:
devisors_dict = {}
for key in range(3, 21):
    devisors_dict[key] = calc_devisors(key)

def crack_key(in_seq: np.ndarray, key_signatures: dict,
              p_threshold: float = 0.9, debug: bool=False) -> list:
    '''Bruteforce keys for provided sequence'''
    possible_keys = {}
    checked_keys = {}
    # Impulse responses
    irs = [[1, 1], [1, 10, 1]]
    c_result = [
        np.convolve(in_seq, ir)[:-(len(ir)-1)] for ir in irs
    ]
    for key, value in key_signatures.items():
        if debug: print(f" Key/divisors {key} / {value}")
        m = []
        for ir, seq in zip(irs, c_result):
            m.append(
                np.convolve(
                    np.isin(seq, value)[::-1],
                    [True]*len(ir)
                )[:-(len(ir)-1)]
            )
        score = np.sum(np.any(np.array(m), axis=0)) / (len(in_seq))
        if debug: print(f" p-value: {score}")
        if score >= p_threshold:
            possible_keys[key] = score
        else:
            checked_keys[key] = score
    return [checked_keys, possible_keys]

try:
    in_seq = np.uint8(list(sys.argv[1]))
    if len(in_seq) < 4:
        raise RuntimeError('Sequence too short')
except:
    print('BAD INPUT!')
    traceback.print_exc()
    print("TEST RUN...")
    p_threshold = 0.9
    for k, v in test_dict.items():
        in_seq = np.uint8(list(v))
        print(dbg_msg.format(
            k=k, v=v, p=p_threshold, 
            key=crack_key(in_seq, devisors_dict)[1]
            )
        )
    exit(1)

# confidance p value for desition
p_threshold = 0.9

print(f'\n\nKeys with p-value > {p_threshold}: {crack_key(in_seq, devisors_dict)[1]}')
