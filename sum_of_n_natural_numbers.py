#let's find the sum of n natural numbers
limit=int(input("Enter n= "))
sum=0
for n in range(1,limit+1):
    sum += n
print("sum:",sum)
