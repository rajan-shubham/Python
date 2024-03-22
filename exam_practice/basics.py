a = 24
a + 2
print(a)
a += 2
print(a)

x = a
print((x>10) or (x % 2 == 0))
print((x>10) and (x % 2 == 0))

print(2 in [1,2,3,4,5])
name = "shubham"
print(len(name)) # 7
print(name[2])

e = [2,3,5,7]
print(e.append(11),e)
f = e + [9,8,4]
print(f)
f.sort()
print(f)

primes = {2,3,5,7,11} ; odds = {3,5,7,9}
print(primes | odds) # union
print(primes & odds) # intersection
print(primes - odds) # {2, 11} -> difference

print(f"My name is {name}.")

def fibonacci(n):
    l = []
    a,b = 0,1
    while len(l) < n:
        a, b = b, (a+b)
        l.append(a)
    return l

print(fibonacci(10))

add = lambda x,y : x + y
print(add(5,6))

#runtime Errors
#print(Q)
#print(1 + 'abc')

try:
    print(2/0) #Zero div. error
    print("This execut first")
except:
    print("This gets executed when its Error in try portion")

# raise  ("oops error")
# raise Rumtime Error ("oops error")

l = [2,4,6,8,10] ; r = [3,6,9,12,15]
for lval, rval in zip(l, r):
    print(lval, rval)