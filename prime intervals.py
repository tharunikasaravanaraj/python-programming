a=int(input())
b=int(input())
for num in range(a,b+1):
  if(num>1):
    for n in range(2,num):
      if(num%n)==0:
      break
  else:
    print(a,b=" ")
  
  
