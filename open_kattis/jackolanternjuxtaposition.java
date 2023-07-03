import java.util.Scanner;


class jackolanternjuxtaposition {
    public static void main(String[] args) {
        
        Scanner reader = new Scanner (System.in);
        //input 1st number
        int num1 = reader.nextInt();
        //input 2nd number
        int num2 = reader.nextInt();
        //input 3rd number
        int num3 = reader.nextInt();
        
        //calculation for R2
        int product = num1 * num2 * num3;
        System.out.println(product);
    }
}