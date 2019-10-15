t = int(input())  #test case input
2
def oppositeSigns(a,b): 
    return ((a ^ b) < 0);  #will check for each real no. inclusive
  
a = 100  #driver code
b = -1
  
if (oppositeSigns(a, b) == True): 
    print("Yes")
else: 
    print("No")
