from time import time
import re

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} seconds to run this program')
        return result
    return wrapper

'''
Password:
> at least 8 characters long;
> may contain any sort of letters, numbers, and $%&@
'''

password = input("Enter string to test: ")
if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}\d+$', password):
    print('zjbs')
else:
    print('xuijne')