while True:
    try:
        num = int(input('Input the numerator: ')) 
        den = int(input('Input the denomerator: ')) 
        print('%d//%d = %d'%(num, den, num//den))
    except Exception as e:
        print('Exception occurs: ' + e) 
        print('Try next input..')
    else:
        print('Very good, next input..')
"""
Input the numerator: s
Traceback (most recent call last):
  File "my.py", line 3, in <module>
    num = int(input('Input the numerator: ')) 
ValueError: invalid literal for int() with base 10: 's'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "my.py", line 7, in <module>
    print('Exception occurs: ' + e) 
TypeError: must be str, not ValueError
"""
