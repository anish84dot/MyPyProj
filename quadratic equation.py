print("Let's find the roots of a quadratic equation")
# get the coefficients from the user 
a = float(input("Enter coefficient a:"))
b = float(input("Enter coefficient b:"))
c = float(input("Enter coefficient c:"))
disc = (b**2-4*a*c)**0.5
if disc < 0 :
    print("the equation has no real roots")
elif disc == 0 :
    root = -b/(2*a)
    print("root one is", root)
else :
    root2 = (-b + disc)/2*a
    root3 = (-b - disc)/2*a
    print(" root two and root three",root2,root3)
