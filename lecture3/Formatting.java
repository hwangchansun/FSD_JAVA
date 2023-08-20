package lecture3;

import java.util.Scanner;

public class Formatting {
    static Scanner in = new Scanner(System.in);
    public static void main(String[] args) {
        //read pattern
        System.out.print("x = "); //s: 자동생성
        double x = in.nextDouble();

        System.out.println("x = "+x); // x = 13.3456
        System.out.printf("x = %.2f \n", x); // x = 13.35
        String result = String.format("x = %.3f", x); 
        System.out.println(result); //x = 3.457
    }
}
