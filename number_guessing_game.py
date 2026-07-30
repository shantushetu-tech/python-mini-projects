import random

print("=" * 45)
print("        NUMBER GUESSING GAME")
print("=" * 45)

while True:
    # Generate a random number
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have chosen a number between 1 and 100.")
    print("Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("📉 Too Low! Try again.")

        elif guess > secret_number:
            print("📈 Too High! Try again.")

        else:
            print("\n🎉 Congratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            break

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n👋 Thank you for playing!")
        break