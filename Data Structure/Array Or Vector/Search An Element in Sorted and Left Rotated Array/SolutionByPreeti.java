import java.util.*;
import java.lang.*;
import java.io.*;

       public class SortedRotatedArray {
 
    public static int findElementIteratve(int[] input, int start, int end, int key) {
 
        while (start <= end) {
            int mid = start + (end - start) / 2;
 
            if (input[mid] == key) return mid;
 
            else if (input[start] <= input[mid]) {
                /*Left sub array is sorted, check if
                key is with A[start] and A[mid] */
                if (input[start] <= key && input[mid] > key) {
                    /*
                      Key lies with left sorted part of array
                     */
                    end = mid - 1;
                } else {
                    /*
                    Key lies in right subarray
                     */
                    start  = mid + 1;
                }
            } else {
                /*
                 In this case, right subarray is already sorted and
                 check if key falls in range A[mid+1] and A[end]
                 */
                if (input[mid + 1] <= key && input[end] > key) {
                    /*
                      Key lies with right sorted part of array
                     */
                    start = mid + 1;
                } else {
                    /*
                    Key lies in left subarray
                     */
                    end  = mid - 1;
                }
            }
        }
        return -1;
    }
 
    public static void main(String[] args) {
        int[] input = {10,11,15,17,3,5,6,7,8,9};
 
        int index = findElementIteratve(input,0, input.length-1, 6);
        System.out.print(index == -1 ? "Element not found" : "Element found at : " + index);
 
    }
}

