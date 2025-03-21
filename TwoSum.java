import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> myNums = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (myNums.containsKey(complement)) {
                return new int[] { myNums.get(complement), i };
            }
            myNums.put(nums[i], i);
        }
        return new int[0];
    }
}

public class TwoSum {
    public static void main(String[] args) {

        int[] nums1 = {2, 7, 11, 15};
        int[] nums2 = {3, 2, 4};
        int[] nums3 = {3, 3};
        int target1 = 9;
        int target2 = 6;
        int target3 = 6;

        Solution sol = new Solution();
        int[] result = sol.twoSum(nums1, target1);
        System.out.println("Indices: [" + result[0] + ", " + result[1] + "]");
    }
}

