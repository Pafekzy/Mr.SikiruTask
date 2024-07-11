print(" WELCOME TO PAFEKZY MOBILE BANK APP!")
 


balance = 0

while True:
    transaction = input("Type in your choice of transaction (deposit or withdraw), or 'quit' to stop: ")
    if transaction.lower() =='quit':
        break

    amount = int(input("Enter amount: "))
    if transaction.lower() == 'deposit':
        balance += amount
        if balance <0 :
            print(" Insufficient Balance. Try Again Later !")
            break

    elif transaction.lower() == 'withdraw':
        balance -= amount
        if balance <0 :
            print(" Insufficient Balance. Try Again Later !")
            break

    print(f"Balance: {balance}")

print(f"Final Balance: {balance}")





















#1. Initialize the balance to 0.
#2. Enter a loop that continues until the user enters 'quit'.
#3. Ask the user to enter a transaction eigher deposit / withdraw.
#4. Ask the user to enter the amount.
#5. If the transaction is a deposit, add the amount to the balance.
#6. If the transaction is a withdrawal, subtract the amount from the balance.
#7. Print the updated balance.
#8. Repeat steps 3-7 until the user enters 'quit'.
#9. Print the final balance.

 