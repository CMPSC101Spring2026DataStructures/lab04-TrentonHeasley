# Basic Rock Paper Scissors Game
# Name: Trenton Heasley
# Date: 20 Feb 2026

import random
from rich.console import Console

"""
main.py
---------
Rock Paper Scissors game for CS101 Spring (Said fall of 25?) 2026 Lab 04.
This script allows a user to play a 3-round game of Rock, Paper, Scissors against the computer.
It uses the 'rich' library for colorful output.
"""

# Create a Console object for rich output
console = Console()

# Constants
CHOICES = ['rock', 'paper', 'scissors']
NUM_TO_CHOICE = {'1': 'rock', '2': 'paper', '3': 'scissors'}

# Function to handle user input also ensures the user enters a valid move.
def get_user_choice():
    """Prompt the user for their choice and return 'rock', 'paper', or 'scissors'."""
    while True:
        user_input = console.input("[bold]Choose rock (1), paper (2), or scissors (3): [/bold]").strip().lower()
        if user_input in NUM_TO_CHOICE:
            return NUM_TO_CHOICE[user_input]
        elif user_input in CHOICES:
            return user_input
        else:
            console.print("[red]Invalid choice. Please try again.[/red]")

# Function to generate the computer's move randomly from the available choices.
def get_computer_choice():
    """Randomly return 'rock', 'paper', or 'scissors'."""
    return random.choice(CHOICES)

# Function to compare choices and decide the winner.
def determine_winner(user_choice, computer_choice):
    """Return 'user', 'computer', or 'tie' based on the choices."""
    if user_choice == computer_choice:
        return 'tie'
    
    # Logic: rock beats scissors, scissors beats paper, paper beats rock
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

# Function to display the outcome of a round using the rich library for colored output.
def print_round_result(user_choice, computer_choice, winner):
    """Print the choices and the winner of the round using rich colors."""
    console.print(f"[magenta]Computer chose: {computer_choice}[/magenta]")
    
    if winner == 'tie':
        console.print("[blue]It's a tie![/blue]")
    elif winner == 'user':
        console.print("[bold green]You win this round![/bold green]")
    else:
        console.print("[bold red]Computer wins this round![/bold red]")

# Main game logic controlling the flow of the application, tracking scores, and determining the overall winner.
def main():
    """Main function to run the game for 3 rounds and print the final result."""
    console.print("[bold cyan]Welcome to Rock, Paper, Scissors![/bold cyan]")
    console.print("[green]You can type 'rock', 'paper', 'scissors' or use 1 for rock, 2 for paper, 3 for scissors.[/green]")

    user_score = 0
    computer_score = 0
    rounds = 3

    for round_num in range(1, rounds + 1):
        console.print(f"\n[bold yellow]Round {round_num} of {rounds}[/bold yellow]")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        print_round_result(user_choice, computer_choice, winner)
        
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

    # Final Score Display
    console.print("\n[bold underline]Game Over![/bold underline]")
    console.print(f"[cyan]Your score: {user_score}[/cyan]")
    console.print(f"[magenta]Computer score: {computer_score}[/magenta]")
	
    # Announce overall winner
    if user_score > computer_score:
        console.print("[bold green]Congratulations, you win the game![/bold green]")
    elif computer_score > user_score:
        console.print("[bold red]Sorry, the computer wins the game.[/bold red]")
    else:
        console.print("[yellow]It's a tie game![/yellow]")

if __name__ == "__main__":
    main()
