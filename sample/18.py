n=int(input("Enter the number:"))
if n>1:
  for i in range (2,int(n/2)+1):
    if (n%i)==0:
      print(n,"is not a prime number")
      break
  else:
     print(n,"is  a prime number")
else:
   print(n,"is not a prime number")











