import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;

public class TwoSum {
    public static void main(String[] args) {
        HashMap<String, String> capitalCities = new HashMap<String, String>();

        capitalCities.put("England", "London");
        capitalCities.put("Peru", "Lima");
        capitalCities.put("Canada", "Ottawa");
        capitalCities.put("USA", "Washington");
        capitalCities.put("Chile", "Santiago");

        for (String i : capitalCities.keySet()) {
            System.out.println(i);
        }

        System.out.println("--------------------------------");

        for (String i : capitalCities.values()) {
            System.out.println(i);
        }
        System.out.println("--------------------------------");
        System.out.println(capitalCities);
        System.out.println(capitalCities.size());
        capitalCities.remove("Chile");
        System.out.println(capitalCities);
        System.out.println(capitalCities.get("Peru"));
        System.out.println(capitalCities.size());
    }
}
