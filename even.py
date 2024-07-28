#let find the even numbers between two user defined numbers
number1 = int(input("Enter number 1 :"))
number2 = int(input("Enter number 2 :"))
#number1 = number1+(number1%2)
number1 += number1%2

'''for counter in range (number1,number2+1,2):
    print(counter)'''

for counter in range (number1,number2+1):
    if(counter%2 == 0):
        print(counter)    