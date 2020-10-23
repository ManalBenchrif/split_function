#Using split() method : 
#This function helps in getting a multiple inputs from user. 
#It breaks the given input by the specified separator. 
#If a separator is not provided then any white space is a separator. 
#Generally, user use a split() method to split a Python string but one can use it in taking multiple input.
#input().split(separator, maxsplit)
x,y=input("enter two number: ").split() #i click space to write second nbr
print("first number",x)
print("second number",y)
print() #jump line

#Using List comprehension 
print("Using List comprehension")
a,b,c=[a for a in input("enter new nbr: ").split(",")]
print("first number",a)
print("second number",b)
print("third number",c)
