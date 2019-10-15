t = int(input())
2
def gcd(a,b): 
    # Everything divides 0  
    if (b == 0): 
         return a 
    return gcd(b, a%b) 
  
  
  # Driver program to test above function 
a = 4 
b = 12
if(gcd(a,b)):
    print('gcd of', a, 'and', b, 'is', gcd(a, b)) 
else:    
     print('not found')       
