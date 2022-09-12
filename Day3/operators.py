print("###################Question: 4 ##############################")
b=int(input("Enter Base:"))
h=int(input("enter Height:"))
area=0.5*b*h
print(area)

print("###################Question: 5 ##############################")
a=int(input("Enter side a:"))
b = int(input("Enter side b:"))
c=int(input("Enter side c:"))
perimeter=a+b+c
print("The perimeter of the triangle is:"+str(perimeter))


print("###################Question: 6 ##############################")
l=int(input("Enter length:"))
b=int(input("Enter bredth:"))
areaOfRectangle = l*b
perimeterOfRectangle=2*(l+b)
print("Area="+str(areaOfRectangle)+"\n"+"Perimeter="+str(perimeterOfRectangle))


print("###################Question: 7 ##############################")
#refer Day2>variables.py



print("###################Question: 9 ##############################")
x1,y1=2,2
x2, y2 = 6, 10
m2 = y2-y1/x2-x1
print(m2)


print("###################Question: 12 ##############################")
stm1="python"
stm2 = "dragon"
print(stm1<stm2)


print("###################Question: 13 ##############################")
if "on" in stm1 and stm2:
    print("True")
else:
    print("False")

print("###################Question: 14 ##############################")
sentence = "I hope this course is not full of jargon."
print('jargon' in sentence)


print("###################Question: 16 ##############################")
lenOfStm1=len(stm1)
print(float(lenOfStm1))
print(str(float(lenOfStm1)))

print("###################Question: 17 ##############################")
number=int(input())
if number%2==0:
    print("even")
else:
    print("odd")


print("###################Question: 18 ##############################")
floorDicision=7//3
intConverted=int(2.7)
print(floorDicision==intConverted)

print("###################Question: 19 ##############################")
tens="10"
ten=10
print(type(tens)==type(ten))

# print("###################Question: 20 ##############################")
# Nine='9.8'
# intNine=int(Nine)
# print(intNine==ten)

print("###################Question: 21 ##############################")
hrs = int(input("Enter hours:"))
hr = int(input("Enter rate per hour:"))
print("Your weekly earning is :"+str(hrs*hr))

print("###################Question: 22 ##############################")
days = int(input("Enter number of years you have lived:"))
lived=days*365*24*60*60
print("You have lived for "+str(lived)+" seconds.")
print("###################Question: 23 ##############################")
print("1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")
