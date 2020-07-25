import java.util.Scanner;
import java.math.BigInteger;

public class Main{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int n, i;
	BigInteger ans;

	while(input.hasNextBigInteger()){
            n = input.nextInt();
            if (n < 1 || n > 1000)
                    break;
            for(i = 2, ans = BigInteger.ZERO; i <= n; ++i){
                    if(i%2 == 1)
                            ans = ans.multiply(BigInteger.valueOf(2)).subtract(BigInteger.ONE);
                    else
                            ans = ans.multiply(BigInteger.valueOf(2)).add(BigInteger.ONE);
            }
            System.out.println(ans);
	}
    }
}