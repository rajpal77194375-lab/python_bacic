#this is calculater
#calculater name
print("----[calculator v1.0]----")
#calculater menu
print("\n[select an opration]")
print('(1)plus (+)')
print('(2)minus (-)')
print('(3)multyply (*)')
print('(4)divide (/)')
#user se input Lena 
opration=int(input('\nenter your opration 1,2,3,or4:'))
#user enter the digits
print('\n----[start calculation]----')
n1=int(input('\nenter your first digit:'))
n2=int(input('enter your second digit:'))
#logic of +,-,*,/
if opration==1:
    print('your ans:',n1+n2)
elif opration==2:
    print('your ans:',n1-n2)
elif opration==3:
    print('your ans:',n1*n2)
elif opration ==4:
    print('your ans',n1/n2)
else:
    print('pleas enter number')    
    

