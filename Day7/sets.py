itCompanies = {'Facebook', 'Google', 'Microsoft',
               'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

############# Exercises : Level 1 ##################

# 1
print(len(itCompanies))

#  2
itCompanies.add("Twitter")
print(itCompanies)

# 3
itCompanies.update(["Coding Minutes", "Virtusa", "Wipro"])
print(itCompanies)

# 4
itCompanies.remove("Virtusa")
print(itCompanies)

# 5
'''
remove(): 
1.remove an item from a set
2.If the item is not found remove() method will raise errors

discard():
1.doesn't raise any errors.
'''

################## Exercise : Level 2 ####################
# 1
print("Joined = {}" .format(A.union(B)))

# 2
print("Intersection= {}".format(A.intersection(B)))

# 3
print("Is A subset of B : {}".format(A.issubset(B)))

# 4
print("Are A and B are disjoint sets: {}".format(A.isdisjoint(B)))

# 5
print("Join A with B and B with A:{}{}".format(A.union(B), B.union(A)))

# 6
print("Symmetric Difference : {}".format(A.symmetric_difference(B)))

# 7
del A
del B
del itCompanies

####################### Exercise : Level 3 ##################
print(len(age))
ages=set(age)
print(len(ages))
string="I am a teacher and I love to inspire and teach people"
print(len(set(string.split())))