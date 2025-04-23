"""Write a class called Rock_paper_scissors that implements the logic of the game Rock paper-
scissors. For this game the user plays against the computer for a certain number of rounds.

Your class should have fields for the how many rounds there will be, the current round number,
and the number of wins each player has. There should be methods for getting the computer’s
choice, finding the winner of a round, and checking to see if someone has one the (entire)
game. You may want more methods."""

import random


class RPS:

    def __init__(self, rounds):
        self.total_rounds = rounds
        self.current_round = 1
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ["rock", "paper", "scissors"]

    def computer(self):
        return random.choice(self.choices)

    def win(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
             
            self.user_wins += 1
            return "user"
        else:
            self.computer_wins += 1
            return "computer"

    def check_winner(self):
        if self.user_wins > self.total_rounds // 2:
            return "User wins the game! 🎉"
        elif self.computer_wins > self.total_rounds // 2:
            return "Computer wins the game! 🤖"
        return None

    def play(self):

        while self.current_round <= self.total_rounds:
            print(f"\nRound {self.current_round}:")
            user_choice = input("Choose rock, paper, or scissors: ").lower()
            while user_choice not in self.choices:
                print("Invalid choice! Please choose rock, paper, or scissors.")
                user_choice = input(
                    "Choose rock, paper, or scissors: ").lower()

            computer_choice = self.computer()
            print(f"Computer chose: {computer_choice}")

            result = self.win(user_choice, computer_choice)
            if result == "user":
                print("You win this round!")
            elif result == "computer":
                print("Computer wins this round! 🤖")
            else:
                print("It's a tie!")

            game_winner = self.check_winner()
            if game_winner:
                print("\n" + game_winner)
                break

            self.current_round += 1

        if not self.check_winner():
            print("\nGame over! It's a tie. 🤝")
        print(
            f"Final Score - You: {self.user_wins}, Computer: {self.computer_wins}")


rounds = int(input("Enter the number of rounds: "))
game = RPS(rounds)
game.play()
