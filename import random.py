import random
import time

# Possible moves
MOVES = ["Rock", "Paper", "Scissors"]

# Function to decide the winner
def get_winner(player, opponent):
    if player == opponent:
        return 0  # Draw
    elif (player == "Rock" and opponent == "Scissors") or \
         (player == "Paper" and opponent == "Rock") or \
         (player == "Scissors" and opponent == "Paper"):
        return 1  # Win
    else:
        return -1  # Loss

# Monte Carlo Tree Search for RPS
def mcts(num_simulations=1000):
    results = {move: {"wins": 0, "plays": 0} for move in MOVES}

    for move in MOVES:
        for _ in range(num_simulations):
            opponent = random.choice(MOVES)
            result = get_winner(move, opponent)
            results[move]["plays"] += 1
            if result == 1:
                results[move]["wins"] += 1

    # Calculate win rate
    best_move = max(MOVES, key=lambda m: results[m]["wins"] / results[m]["plays"])
    return best_move, results

# Game loop
def play_game():
    print("Rock Paper Scissors using Monte Carlo Tree Search")
    while True:
        user = input("Enter your move (Rock/Paper/Scissors or Quit): ").capitalize()
        if user.lower() == "quit":
            print("Game Over!")
            break
        if user not in MOVES:
            print("Invalid move! Try again.")
            continue

        start = time.time()
        ai_move, stats = mcts(num_simulations=500)
        elapsed = time.time() - start

        print(f"AI chose: {ai_move}")
        result = get_winner(user, ai_move)
        if result == 1:
            print("You win!")
        elif result == -1:
            print("AI wins!")
        else:
            print("It's a draw!")
        print(f"(AI decision time: {elapsed:.3f}s)\n")

if __name__ == "__main__":
    play_game()
