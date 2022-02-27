#muveletek
#1 feladat
x=int(input())

t=(x*x)*3.14
k=(2*x)*3.14

print(t)
print(k)

#2 feladat
ker=input()
vez=input()

teljes=vez+ker

print("Hello",teljes)

#felteteles
#1
x=input("Jo napja van?")
if x=="igen":
    print("nekem is")
else:
    print("sajnalom")

#logikai
#1
x=int(input())

if x % 2 == 0:
    print("paros")
else:
    print("paratlan")

#ciklusok
#5
x=int(input())

while x % 2 != 0:
    x+int(input())
else:
    print(x)