import java.util.Arrays;
import java.util.Scanner;

public class BuildingTest {

	public static void main(String[] args) throws Exception{
		// 코드를 작성해주세요.
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1 ; test_case <= T ; test_case++){
			int answer = 0;
			int[] di = {0, 0, 1, -1, 1, 1, -1, -1};
			int[] dj = {1, -1, 0, 0, -1, 1, -1, 1};
			int max = Integer.MIN_VALUE;

			int n = sc.nextInt();
			int[][] map = new int[n][n];

			for(int i = 0 ; i < n ; i++){
				for(int j = 0 ; j < n ; j++){
					String a = sc.next();
					if(a.equals("G")){
						map[i][j] = 0;
					} else {
						map[i][j] = 1;
					}
				}
			}

			for(int i = 0 ; i <  n; i++){
				for(int j = 0 ; j < n ; j++){
					if(map[i][j] == 1){
						boolean flag = true;
						for(int k = 0 ; k < 8 ; k++){
							int ni = i + di[k];
							int nj = j + dj[k];
							if(ni >= 0 && ni < n && nj >= 0 && nj < n && map[ni][nj] == 0){
								flag = false;
							}
						}
						if(flag){
							int cnt = -1;
							for(int k = 0; k < n ; k++){
								if(map[i][k] == 1){
									cnt += 1;
								}
								if(map[k][j] == 1){
									cnt += 1;
								}
							}
							max = Math.max(max, cnt);
						}
					}
				}
			}
			System.out.println("#" + test_case + " " + max);
		}
	}
}