import java.util.Scanner;
import java.util.*;

public class digitswap{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int input= scanner.nextInt();
        double digit1 = (input/10)%10;
        double digit2 = input%10;
        
        int digit1st = (int) digit1;
        int digit2nd = (int) digit2;
        
        System.out.print(digit2nd + "" + digit1st);
        
    }
}
