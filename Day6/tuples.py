#1

emptyTuple=tuple()

# 2
sisters=("Bunny","Roops","Anu")
print(sisters)
brothers=("Sanketh","Jittu","Sunil")
print(brothers)
# 3
sibilings=sisters+brothers
print(sibilings)
# 4
print(len(sibilings))
# 5
sibilings=list(sibilings)
sibilings.append("Srinivas")
sibilings.append("Ramadevi")
sibilings=tuple(sibilings)
familyMembers= sibilings
print(familyMembers)



################ EXERSICE :LVL2 ######################
# 1
unpakSibilings=familyMembers[:6]
print(unpakSibilings)

# 2
fruits=("Apple","banana","Orange","grapes")
vegetables=("potato","tomato","spinach")
animalFood=("pedegree","wiskwer","milk")
foodStuffTuple=fruits+vegetables+animalFood
print(foodStuffTuple)

# 3
foodStuffTuple=list(foodStuffTuple)
print(foodStuffTuple)
# 4
length=len(foodStuffTuple)
print(length)
middle=float(length/2)
if middle%2!=0:
    print(foodStuffTuple[int(middle-.5)])
else:
    print(foodStuffTuple[int(middle)],foodStuffTuple[int(middle-1)])
del foodStuffTuple
nordicCountries=('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordicCountries)
print('Iceland' in nordicCountries)