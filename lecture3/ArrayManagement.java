package lecture3;

import java.util.Arrays;

public class ArrayManagement { // Arrays라고 하면 위에 import한 Arrays랑 충돌됨, 따라서 이름 다르게 해야함
    public static void main(String[] args) {
        /* 
         * Syntax to create an array:
         * <type> [] <arrayname> = new <type>[size];
        
        
        
        shift +command + p 
         */
        String[] names = new String[3];
        names[0] = "John Smith"; // ''하면 오류, " " 사용하기
        names[1] = "Alen";
        names[2] = "Lucy";

        System.out.println(Arrays.toString(names));
        // [null,null,null]출력됨: 이유는 디폴트값

        names[0] = "John"; // ''하면 오류, " " 사용하기
        names[1] = "Alana";
        names[2] = "Lucy";

        System.out.println(Arrays.toString(names));
        
        // clear하면 커멘드라인 다 삭제
        System.out.println(names[0]);
        System.out.println(names[names.length-1]); // 길이 인덱스 0부터 시작하기 때문에 -1
        // System.out.println(names[names.length]); 이거 오류

        int x[] = new int[] {4, 6, 2}; // new int[3] {4, 6, 2} 괄호 3 넣으면 오류
        System.out.println(Arrays.toString(x));

        x[0] += 2;
        System.out.println(Arrays.toString(x));

        x[0]++;
        System.out.println(Arrays.toString(x));

        ++x[0];
        System.out.println(Arrays.toString(x));



    }
    
}

