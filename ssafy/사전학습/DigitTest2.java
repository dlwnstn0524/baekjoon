package startCamp1;

public class DigitTest2 {

	public static void main(String[] args) {
		int count = 1;
		for(int i = 0 ; i < 5 ; i++) {
			if(i == 0 || i == 4) {
				for(int j = 0 ; j < 5; j++) {
					System.out.print(count + " ");
					count++;
				}
			}else if(i == 1 || i == 3) {
				System.out.print(" ");
				for(int j = 0 ; j < 3 ; j++) {
					System.out.print(count + " ");
					count++;
				}
				System.out.print(" ");
			}else {
				System.out.print("   " + count + "   ");
				count++;
			}
			System.out.println();
		}
	}

}
