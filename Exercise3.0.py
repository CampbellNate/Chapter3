score = input("Enter Score: ")
g=float(score)
if(1>=g>=.9):
    print('A')
elif(.9>=g>=.8):
    print('B')
elif(.8>=g>=.7):
    print('C')
elif(.7>=g>=.6):
    print('D')
elif(0<=g<=.6):
    print('e')
else:
    print('Invalid Response')