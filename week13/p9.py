while True:
    try:
        num = int(input('Input the numerator: ')) 
        den = int(input('Input the denomerator: ')) 
        print('%d//%d = %d'%(num, den, num//den))
    except ZeroDivisionError:
        print(' Devision or modulo by zero occurs!!') 
        print(' Try next input..')
    except Exception as e:
        print('Exception occurs: ' + str(e)) 
        print('Try next input..')
    else:
        print('Very good, next input..')
