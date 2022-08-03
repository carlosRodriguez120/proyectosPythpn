

i=int(input("numero"))
cont=0
while(i!=1):
    if i%2!=0:
        i=(i*3)+1
        print(i)
    else:
        i=i/2
        print(i)
    cont+=1

print(f"el contador fue: {cont}")