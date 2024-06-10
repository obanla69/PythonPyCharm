

#tuple = 1,
##help(tuple)

##tuple1 = (0,"ojo",2.5)
##print(tuple1[0])

#tuple1 = (0, "ojo",2.5,[])
#tuple1[3].extend([1,3,"Kent"])
#tuple1 = tuple1 + (1,6)  ##agumented assignment
#tuple1 += (1,6)
#print(tuple1)

#tuple1 = (0,0,"ojo",2.5,[])
#names = ["afeez","yinka","eniola"]
#names += tuple1
#names = tuple(names)
#print(names)



    #set

#x = {1,1,2,3,2,2,4,5,1}
#y = set()
##print(x)

x = {1,1,2,3,2,2,4,5,1,"mercy"}
y = {1,3,7,9,10,2}
x.add(10)
print(x.difference(y))
