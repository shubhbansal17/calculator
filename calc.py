#this is a calculator made in python
while True:
    num1=int(input('enter number 1'))
    num2=int(input('enter nmber2'))
    oper=input('enter operation you want to perform')
    if oper=='add':
        print(num1+num2)
    elif oper=='subtract':
        print(num1-num2)
   
    elif oper=='multiply':
        print(num1*num2)
    elif oper=='divide':
        print(num1/num2)
    
    ans=input('do you want to do more operations')
    if ans in 'nN':
        break
   
