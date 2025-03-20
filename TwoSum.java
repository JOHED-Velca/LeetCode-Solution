import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;

public class TwoSum {
    public static void main(String[] args) {

        int[] nums = {3, 2, 4};
        int target = 6;

        HashMap<Integer, Integer> myNumbers = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            int dif = target - nums[i];
            if (myNumbers.containsKey(dif)) {
                System.out.println("[" + myNumbers.get(dif) + "," + i + "]");
            }
            myNumbers.put(nums[i], i);

        }
    }
}
//class Solution {
//    public int[] twoSum(int[] nums, int target) {
//        Map<Integer, Integer> myNums = new HashMap<>();
//
//        for (int i = 0; i < nums.length; i++) {
//            int complement = target - nums[i];
//            if (myNums.containsKey(complement)) {
//                return new int[] { myNums.get(complement), i };
//            }
//            myNums.put(nums[i], i);
//        }
//        return new int[0];
//    }
//}
