b = [1,2,3,4,5,6,7,8]
m = ["apple","banana","man","gil"]
#newlist = []
#for x in b:
 #   if x % 2 != 0:
  #      newlist.append("odd list")

   # print((newlist))
#else:
 #   newlist.append("even")
#newlist = ["odd" for x in b if x%2 != 0]
#print(newlist)
newlist = ["odd" if x %2 != 0 else "even" for x in b]
print(newlist)
d = [x.lower() for x in m]
d = (1,)
print(type(d))
name = "hello    world"
name = name.split()
print(name)

name=['hello','world','dam']
name = "  ".join(name)#list to string matra use hunxa 
print(name)