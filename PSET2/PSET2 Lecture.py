'''
#Find divisors of 100, by getting modulo == 0,
#and store them inside tuples.
x = 100
divisors = ()
for i in range (1, x):
    if (x % i == 0):
        divisors = divisors+(i,)
print ("All Tuples:", divisors)
print ("Slice of Tuples:", divisors[1:3])
'''

'''
#Combine list and access each list with loops
Techs = ['MIT', 'Cal Tech']
Ivys = ['Harvard', 'Yale', 'Brown']
Univs = []
Univs.append(Techs)
print ('Univs =', Univs)
Univs.append(Ivys)
print ('Univs =', Univs)
for e in Univs:
    print ("e = ", e)

flat = Techs + Ivys
print ("Flat: ", flat)
#Removing
artSchools = ['RISD', 'Harvard']
for u2 in artSchools:
    if u2 in flat:
        flat.remove(u2)
print ('Removed Harvard:', flat)
#Sorting
flat.sort()
print ('Sorted  ', flat)
#Change each element what you want
flat[1] = "Hi"
print ("Changing Element: ", flat);

#Copy list from source to destination
def copyList(LSource, LDest):
    for e in LSource:
        LDest.append(e)
        print ("LDest = ", LDest)
L1 = []
L2 = [1, 2, 3]
copyList(L2, L1)
print ("L1 =", L1)
print ("L2 =", L2)
#L1, L1 Points at same list so it will run forever
copyList(L1, L1)
print ("L1 =", L1)
'''

D = {1, 'one', 'deux', 'two', 'pi', 3.14159}




