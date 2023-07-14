import java.util.Scanner;


class twostones {
    public static void main(String[] args) {
        Scanner reader = new Scanner (System.in);
        //System.out.println("Enter a number: ");
        int number = reader.nextInt();
        if (number % 2 == 0){
            System.out.println("Bob");
        }
        else {
            System.out.println("Alice");
        }
        
    }
}