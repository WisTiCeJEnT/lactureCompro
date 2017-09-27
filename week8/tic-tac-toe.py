def v(y):
    for i in range(n):
        print(' '*y + '|' + ' '*y + '|')
def h(x):
    print('-'*x + '+' + '-'*x + '+' + '-'*x)
n = int(input())
v(n)
h(n)
v(n)
h(n)
v(n)
