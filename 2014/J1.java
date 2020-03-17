import java.util.Scanner;

public class Main {
	
	public static void main(String args[]) {
		Scanner scanner = new Scanner(System.in);
		
    // get input
		int a1 = scanner.nextInt();
		int a2 = scanner.nextInt();
		int a3 = scanner.nextInt();
		
    //check conditions
		if ((a1 + a2 + a3) != 180) System.out.println("Error");
		else if (a1 == a2 && a2 == a3) System.out.println("Equilateral");
		else if (a1 == a2| a2 == a3 | a1 == a3) System.out.println("Isosceles");
		else if (a1 != a2 && a1 != a3 && a2 != a3) System.out.println("Scalene");
		
		scanner.close();
	}
}
