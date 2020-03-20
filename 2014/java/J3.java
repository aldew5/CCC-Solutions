/*
 Alec Dewulf
 "Double Dice" J3 2014
 March 20, 2020
 */

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		// setting variables
		int ant = 100;
		int david = 100;
		
		// initial input
		int num_rounds = scanner.nextInt();
		scanner.nextLine();
		
		int i = 0;
		while (i < num_rounds) {
			// getting input based on the number of rounds
			String scores = scanner.nextLine();
			String [] split_scores = scores.split(" ");
			
			// Antonia had the higher roll
			if (Integer.parseInt(split_scores[0]) > Integer.parseInt(split_scores[1])) {
				david -= Integer.parseInt(split_scores[0]);
			}
			// David had the higher roll
			else if (Integer.parseInt(split_scores[0]) < Integer.parseInt(split_scores[1])) {
				ant -= Integer.parseInt(split_scores[1]);
			}
			i ++;
			
		}
		// Output results
		System.out.println(ant);
		System.out.println(david);
		
		scanner.close();
		
	}
}
