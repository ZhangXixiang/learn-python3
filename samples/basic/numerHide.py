


phone_number = '1386-666-0006';
hiding_number = phone_number.replace(phone_number[:9],'*' * 9)
print(hiding_number)


def b() :
    return 'a';

print(b())




def fahrenheit_converter(C):
    fahrenheit = C * 9/ 5 + 32
    return str(fahrenheit) + '˚ F'

print(fahrenheit_converter(20))



def weight_converter(W):
    kgWeight = str(W*1000) + 'g';
    return kgWeight

print(weight_converter(1.5))





def thirdSideLen(a,b):
    num = a*a + b*b;
    c = num ** 0.5;
    return c;

print(thirdSideLen(b=3,a=4))


def testParm(a,b):
    return a

print(testParm(b=1,a=2))

print('    *','   ***','  *****','    |',sep='\n');