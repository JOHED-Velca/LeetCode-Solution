import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;

public class TwoSum {
    public static void main(String[] args) {

        int[] nums = {3, 3};
        int target = 6;
        int dif = 0;

        HashMap<Integer, Integer> myNumbers = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            Integer put = myNumbers.put(nums[i], i);
            System.out.println(myNumbers);
            dif = target - nums[i];
            System.out.println(dif);
            if (myNumbers.get(dif) != null && myNumbers.size() > 1) {
                System.out.println("["+i + "," + myNumbers.get(dif)+"]");
                break;
            }else {
                System.out.println("searching...");
            }
        }
//        for (int i = 0; i < myNumbers.size(); i++) {
//            if (target - myNumbers.get(i) = 0)
//        }

        System.out.println(myNumbers);

    }
}
