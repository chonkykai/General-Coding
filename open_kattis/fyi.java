import java.util.Scanner;

public class fyi{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int  values= scanner.nextInt();
        int digit = values/10000%1000;
        if (digit == 555){
            System.out.println("1");
        }   else{
            System.out.println("0");
        }
    }
}