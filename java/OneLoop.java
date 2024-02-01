import java.util.Arrays;

public class OneLoop {

    public static void main(String[] args) {
        int[] a = { 1, 2, 3, 4, 5, 6, 7 };
        boolean hasDuplicates = hasDuplicate(a);
        System.out.println("int array: " + Arrays.toString(a) + " Has duplicates: " + hasDuplicates);

        int[] b = { 1, 2, 2, 3, 4, 5 };
        hasDuplicates = hasDuplicate(b);
        System.out.println("int array: " + Arrays.toString(b) + " Has duplicates: " + hasDuplicates);
    }

    public static boolean hasDuplicate(int[] a) {
        for (int i = 0; i < a.length; i++) {
            for (int j = i + 1; j < a.length; j++) {
                if (a[i] == a[j]) {
                    return true; // duplicate found
                }
            }
        }
        return false;// no duplicate
    }
}
