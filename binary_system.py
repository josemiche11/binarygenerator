num1= int(input("Enter the frst: "))
num2= int(input("Enter the sec: "))
num= int(input("Enter the nth term: "))

for k in range(num):
 bi= list(bin(k)[2:])
 ch=""
 for i in range(len(bi)):
    if bi[i]=="0":
        bi[i]= str(num1)
    else:
        bi[i]= str(num2)
 for j in range(len(bi)):
    ch= ch+ bi[j]
 print(int(ch))
