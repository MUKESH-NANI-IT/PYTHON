


print("############### Question: 1 ######################")
th,d,o,p="Thirty ","Days ","Of ","Python"
print(th+d+o+p)


print("############### Question: 2 ######################")
c,f,a="Coding ","For ","All"
print(c+f+a)


print("############### Question: 3 ######################")
company="Coding For All"


print("############### Question: 4 ######################")
print(company)


print("############### Question: 5 ######################")


print(len(company))


print("############### Question: 6 ######################")
print("To Upper" + company.upper())


print("############### Question: 7 ######################")
print("To Lower"+ company.lower())


print("############### Question: 8 ######################")
print("Captalise:"+company.capitalize())
print("Title:"+company.title())
print("SwapCase:"+company.swapcase())


print("############### Question: 9 ######################")
splitted=company.split()
fw=splitted[0]
print(fw)


print("############### Question: 10 ######################")
print(company.find("Coding"))
print(company.index("Coding"))


print("############### Question: 11 ######################")
replacedCompany = company.replace("Coding", "Python")
print(replacedCompany)


print("############### Question: 12 ######################")
print(replacedCompany.replace("All","Everybody"))


print("############### Question: 13 ######################")
print(company.split(" "))


print("############### Question: 14 ######################")
companies="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))


print("############### Question: 15 ######################")
print(company.index("Coding"))


print("############### Question: 16 ######################")
print(len(company))


print("############### Question: 17 ######################")
print(company[11])


print("############### Question: 18 ######################")
line = company
acronym=''.join(w[0] for w in line.split() if w[0].isupper())
print(acronym)


print("############### Question: 19 ######################")
line=replacedCompany
acronym = ''.join(w[0] for w in line.split() if w[0].isupper())
print(acronym)


print("############### Question: 20 ######################")
indexOfC=company.index("C")
print(indexOfC)


print("############### Question: 21 ######################")
indexOfF = company.index("F")
print(indexOfF)


print("############### Question: 22 ######################")
company="Coding For All People."
print(company.rfind("l",0,len(company)))


print("############### Question: 23 ######################")
because="You cannot end a sentence with because because because is a conjunction"
print(because.find("because"))


print("############### Question: 24 ######################")
print(because.rfind("because",0,len(because)))


print("############### Question: 25 ######################")
print(because.replace("because because because",""))


print("############### Question: 26 ######################")
print(because.find("because"))


print("############### Question: 27 ######################")
print("refer 25")


print("############### Question: 28 ######################")
print(company.startswith("Coding"))


print("############### Question: 29 ######################")
print(company.endswith("coding"))


print("############### Question: 30 ######################")
print(company.rstrip().lstrip)


print("############### Question: 31 ######################")
print("A:")
print("30DaysOfPython".isidentifier())
print("B:")
print("thirty_days_of_python".isidentifier())


print("############### Question: 32 ######################")
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(libs))

print("############### Question: 33 ######################")
print("I am enjoying this challenge.\nI just wonder what is next.")

print("############### Question: 34 ######################")
print("Name\tAge\tCountry\tCity\nMukesh\t21\tIndia\tHyderabad")


print("############### Question: 35 ######################")
r=10
area=3.14*r**2
print("The are of the circle with radius {} is {} meter square. ".format(r,area))

print("############### Question: 36 ######################")
eight=int(8)
six=int(6)
print("{}+{}={}".format(eight,six,eight+six))
print("{}-{}={}".format(eight,six,eight-six))
print("{}*{}={}".format(eight,six,eight*six))
print("{}/{}={}".format(eight,six,eight/six))
print("{}%{}={}".format(eight,six,eight%six))
print("{}**{}={}".format(eight,six,eight**six))
print("{}//{}={}".format(eight,six,eight//six))