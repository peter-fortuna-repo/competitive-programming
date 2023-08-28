/* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.*/

// Solution 1: 
/* The simplest approach is to check all possible pairs in a nested loop */

// Computational complexity: O(n^2) 

public int[] twoSum(int[] nums, int target) {
    for(int i=0; i < nums.length-1; i++){
        for(int j=i+1; j< nums.length; j++){
            if(nums[i] + nums[j] == target){
                return new int[]{i, j};
            }
        }
    }
    return null;
}

// Solution 2
/* We can bring the runtime down to O(n). When we check nums[i], we know that
 * the other element must equal target - nums[i]. This lets us speed things up 
 * using a hashtable. After a hashtable linking nums[i] to i is built,  we pass 
 * through nums one time, and at each num we check if the needed element is in 
 * our hashtable.*/

// Computational complexity: O(n)

import java.util.HashMap;

public int[] twoSum(int[] nums, int target) {
    HashMap<Integer, Integer> lookup = new HashMap<Integer, Integer>();
    for(int i=0; i<nums.length; i++){
        lookup.put(nums[i], i);
    }

    for(int i=0; i<nums.length; i++){
        lookup.remove(nums[i], i);
        if(lookup.get(target - nums[i]) != null){
            return new int[] {i, lookup.get(target - nums[i])};
        }
        lookup.put(nums[i], i);
    }

    return null;
}