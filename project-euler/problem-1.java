/* Problem:
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 
 * 3, 5, 6, and 9. The sum of these multiples is 23.
 * 
 * Find the sum of all the multiples of 3 or 5 below 1000. */


 
// Solution 1:
/* Loop through all multiples of 3 and 5 and add them together, then subtract all 
 * multiples of 15 because they get double counted.*/

// Computational complexity: O(n) (where n is the upper limit, ie 1000)

static class Solution_1{
    public static int addMultiples(){
        int sum = 0;

        // Add multiples of 3
        for(int i=0; i < 1000; i+=3){
            sum += i;
        }

        // Add multiples of 5
        for(int i=0; i < 1000; i+=5){
            sum += i;
        }

        // Remove duplicate multiples of 15
        for(int i=0; i < 1000; i+=15){
            sum -= i;
        }

        return sum;
    }
}


// Solution 2
/* We can speed this up using a math trick.
 * Note that:
 * 3(0) + 3(1) + 3(2) + ... + 3(332) + 3(333)
 * 
 * Simplifies to:
 * 3(1 + ... + 332 + 333)
 * 
 * Due to the fact that the sum from one to n is n(n+1)/2, we get:
 * 3 (333 * 334 / 2)
 * 
 * This allows us to solve the problem in constant time. */

 // Computational complexity: O(1)

class Solution_2{
    public static int addMultiples(){
        int n = 1000;
        int a = 3;
        int b = 5;
        int c = a*b;
        return (a * (n/a) * (n/a + 1))/2 +
                (b * (n/b) * (n/b + 1))/2 -
                (c*(n/c) * (n/c + 1))/2;
    }
}