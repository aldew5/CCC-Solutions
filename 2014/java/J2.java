/*
 Alec Dewulf
 "Vote Count" J2 2014
 March 19, 2020
 
 This solution demonstrates the need to read a blank line after integer input.  
 This is because nextInt doesn't read the newline character of the input
 */

import java.util.Scanner;

public class Main {
	// define a method to calculate the number of A votes
	public static int returna(String votes, int num_votes) {
		int num_a = 0;
		
		for(int i = 0; i < num_votes; i ++) {
			if (votes.charAt(i) == 'A') {
				num_a ++;
			}
		}
		return num_a;
	}
	// method to calculate the number of B votes
	public static int returnb(String votes, int num_votes) {
		int num_b = 0;
		
		for(int i = 0; i < num_votes; i ++) {
			if (votes.charAt(i) == 'B') num_b ++;
		}
		return num_b;
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int num_votes = scanner.nextInt();
		// use this after integer input
		scanner.nextLine();
		String votes = scanner.nextLine();
		
		// calculate values for a and b votes
		int num_a = returna(votes, num_votes);
		int num_b = returnb(votes, num_votes);
		
		// check conditions
		if (num_a > num_b) System.out.println('A');
		else if (num_a < num_b) System.out.println('B');
		else if (num_a == num_b) System.out.println("Tie");
		scanner.close();
	}

}
