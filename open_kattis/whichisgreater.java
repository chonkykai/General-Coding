import java.util.Scanner;
import java.util.*;

public class whichisgreater{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int input1 = scanner.nextInt();
        int input2 = scanner.nextInt();
        if (input1 > input2){
            System.out.println("1");
        } if (input1 == input2) {
            System.out.println("0");
        } if (input1 < input2) {
            System.out.println("0");
        }
    }
}
