
while True:
    hrs = input("Enter Hours:")
    try:
        h=int(hrs)
        break
    except ValueError:
        print('Invalid input')
while True:
    rte = input("Enter Rate:")
    try:
        r=float(rte)
        break
    except ValueError:
        print('Invalid input')
if(h>40):
    Opay=((h-40)*r*1.5)
    p=(40*r)
    print(Opay+p)
else:
    print(r*h)