import java.util.ArrayList;
import java.util.Scanner;
import java.util.*;

public class gcvwr{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int G = scanner.nextInt();
        int T = scanner.nextInt();
        int N = scanner.nextInt();
        
        int[] lists = {};
        ArrayList<Integer> values = new ArrayList<>();
        for (int i=0; i < N; i++ ){
            values.add(scanner.nextInt());
        }
        
        int sum = values.stream().mapToInt(Integer::intValue).sum();
        int total_weight = G - T;
        double allowed_weight = total_weight*0.9;
        double weight_trailer = allowed_weight - sum;
        int converted_weight_trailer = (int) weight_trailer;
        System.out.println(converted_weight_trailer);
    }
}