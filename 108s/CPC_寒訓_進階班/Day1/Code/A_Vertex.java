import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n, v, e, test;
        int i, j, k;
        int d[][];
        
        while(input.hasNextLine()){
            //construct graph
            n = input.nextInt();
            ////preparing for shortest path
            d = new int[n][n];
            for(i = 0; i < n; ++i)
                for(j = 0; j < n; ++j)
                        d[i][j] = 100;
            ////
            if(n == 0)
                break;
            while(input.hasNextLine()){
                v = input.nextInt();
                if(v == 0)
                    break;
                for(e = input.nextInt(); e != 0; e = input.nextInt())
                    d[v-1][e-1] = 1;
            }
            
            //shortest path
            for(k = 0; k < n; ++k)
                for(i = 0; i < n; ++i)
                    for(j = 0; j < n; ++j)
                        if(d[i][k] + d[k][j] < d[i][j])
                            d[i][j] = d[i][k] + d[k][j];
            
            //print answers
            test = input.nextInt();
            for(i = 0; i < test; ++i){
                v = input.nextInt() - 1;
                e = 0;
                ArrayList<Integer> ans = new ArrayList<>();
                for(j = 0; j < n; ++j)
                    if(d[v][j] == 100){
                        ++e;
                        ans.add(j + 1);
                    }
                System.out.print(e);
                for(j = 0; j < e; ++j)
                        System.out.print(" " + ans.get(j));
                System.out.println();
            }
        }
    }
}