import java.util.Scanner;
import java.util.*;

public class cold{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int input= scanner.nextInt();
        
        List<Integer> temp = new ArrayList<Integer>();
        for(int i=0; i<input;i++){
            temp.add(scanner.nextInt());
        }
        
        int lowcount = 0;
        for (int j=0; j<temp.size();j++){
            if (temp.get(j) < 0){
               lowcount += 1; 
            }
        } 
        System.out.println(lowcount);
    }
}
