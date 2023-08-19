package lectures3;

public class Variables {
    public static void main(String[] args) {
        int x; //declaring a variable
        x = 4; // initializing a variable

        double y = 3.5; // declaring and initialize

        // int result = x + y; 이렇게하면 자료형이 서로 안 맞아서 오류 
        // int = result = x + (int)y; 아래와 같은 결과
        double result = x + y; 
        
        System.out.println("Result " + result);
        //    

    }

}