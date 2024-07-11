

import java.util.Scanner;

public class TransactionBalance {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double balance = 0;

        while (true) {
            System.out.print("Enter transaction (deposit/withdraw), or 'quit' to stop: ");
            String transaction = scanner.next();
            if (transaction.equalsIgnoreCase("quit")) {
                break;
            }
            System.out.print("Enter amount: ");
            double amount = scanner.nextDouble();
            if (transaction.equalsIgnoreCase("deposit")) {
                balance += amount;
            } else if (transaction.equalsIgnoreCase("withdraw")) {
                balance -= amount;
            }
            System.out.println("Balance: " + balance);
        }
        System.out.println("Final Balance: " + balance);
    }
}

 
