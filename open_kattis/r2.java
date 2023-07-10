import java.util.Scanner;


class r2 {
    public static void main(String[] args) {
        
        Scanner reader = new Scanner (System.in);
        //input 1st number
        int R1 = reader.nextInt();
        //input 2nd number
        int S = reader.nextInt();
        //calculation for R2
        int R2 = (2*S)-R1;
        System.out.println(R2);
    }
}