import sys
try:
    r = int(sys.argv[1])
    div = (r // 17)
    b = 2 *div
    temp = r - ( div * 17)
    j = 2 * b
    left_amount = temp - (j // 2)
    p = left_amount * 26
    result = str(b)+str(j)+str(p)
    print(result)
    
except ValueError:
    print('000')
    
