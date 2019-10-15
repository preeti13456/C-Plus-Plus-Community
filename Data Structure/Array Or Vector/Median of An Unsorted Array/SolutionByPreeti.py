t = int(input())
2
def findMedian(a, n): 
  
    # First we sort the array 
    sorted(a) 
  
    # check for even case 
    if n % 2 != 0: 
        return float(a[n/2]) 
      
    return float((a[int((n-1)/2)] +
                  a[int(n/2)])/2.0) 
  
# Driver program 
a = [ 1, 3, 4, 2, 7, 5, 8, 6 ] 
n = len(a) 
print("Median =", findMedian(a, n)) 
