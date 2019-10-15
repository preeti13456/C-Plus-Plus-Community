t = int(input())
2
# Function to check if an array is 
# sorted and rotated clockwise 
def checkIfSortRotated(arr, n): 
    for i in range (arr.length):
        if (array[i+1] < array[i]):
            return i + 1;
            break;                                                     
left = int(input())
right = int(input(arr.length - 1))
while (array[left] > array[right]):                                       
    mid = int(input(left + (left + right) / 2))
    if(array[mid] > array[right]):
        left = mid + 1;
    else:
        right = mid;
return left;
