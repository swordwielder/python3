import java.util.*;
import java.io.*;
import java.math.*;

class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        String n;
        
            
        n=in.next();
        try{
            double nu=Double.parseDouble(n); 
            if (nu%4==0){
                System.out.println("AAAAAAAAAA!!!");        
            }else{
                System.out.println("Ok");    
            }    
        }catch(NumberFormatException e){
            System.out.println("Ok");    
        }
        

    }
}
