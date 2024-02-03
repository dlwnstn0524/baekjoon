import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 농작물 {
    static int T, N;
    static int answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        for(int t = 1 ; t <= T; t++){
            N = Integer.parseInt(br.readLine());
            System.out.println("#" + t +" " + answer);
        }
    } 
}
