import sys
spam = ['apples', 'bananas', 'tofu', 'cats']
x = spam

def commaCode(x):
    
    if type(x) is not list:
        sys.exit()

    if len(x)< 1:
        print ("No value in list")
        sys.exit()
    result = ''
    for i in x:
        if i == x[-1]:
            result += 'and '+i
            break     
        result += i + ' ' 
    return result

y = []

print (commaCode(y))
