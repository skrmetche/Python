import random as rd

print("=" * 40)
print("🎮 Welcome to Rock-Paper-Scissors 🎮")
print("=" * 40)

# Get player name
player_name = input("Enter your name: ").strip().capitalize()
if player_name == "":
    player_name = "Player"

game_options = ["Rock", "Paper", "Scissor"]

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

you_win = """
__   __          _            _   _          
\ \ / /__  _   _( )_ __ ___  | |_| |__   ___ 
 \ V / _ \| | | |/| '__/ _ \ | __| '_ \ / _ \\
  | | (_) | |_| | | | |  __/ | |_| | | |  __/
  |_|\___/_\__,_| |_|  \___|  \__|_| |_|\___|
__      _(_)_ __  _ __   ___ _ __| |         
\ \ /\ / / | '_ \| '_ \ / _ \ '__| |         
 \ V  V /| | | | | | | |  __/ |  |_|         
  \_/\_/ |_|_| |_|_| |_|\___|_|  (_)         
  """

you_lose = """
__     ______  _    _   _      ____   _____ ______ 
\ \   / / __ \| |  | | | |    / __ \ / ____|  ____|
 \ \_/ / |  | | |  | | | |   | |  | | (___ | |__   
  \   /| |  | | |  | | | |   | |  | |\___ \|  __|  
   | | | |__| | |__| | | |___| |__| |____) | |____ 
   |_|  \____/ \____/  |______\____/|_____/|______|
                      YOU LOSE!
"""

ascii_art =[rock,paper,scissor]


player_score = 0
computer_score = 0
draws = 0

while True:
    try:
        player_input = int(input("""
                                Press 0 for Rock 
                                Press 1 for Paper
                                Press 2 for Scissor
                                """))
        # 0 = rock
        # 1 = paper
        # 2 = scissor
        if player_input not in [0,1,2]:
            print("Invalid input. Please enter 0,1 or 2.")
        else:
            computer_input = rd.randint(0,2)

            print(f"\nYou chose: {game_options[player_input]} {ascii_art[player_input]}")
            print(f"Computer chose: {game_options[computer_input]} {ascii_art[computer_input]}")
            if player_input == computer_input:
                print("It's a draw. Play again!")
                draws += 1
            elif (player_input == 1 and computer_input == 0) or \
                (player_input == 2 and computer_input == 1) or \
                (player_input == 0 and computer_input == 2):
                print(you_win)
                player_score += 1
            else :
                print(you_lose)
                computer_score += 1

            # Show current scores
            print(f"""
--------------------------
   SCOREBOARD
--------------------------
🧍 {player_name}:    {player_score}
💻 Computer:  {computer_score}
🤝 Draws:     {draws}
--------------------------
""")

        # Ask user if they want to play again
        while True:
            play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
            if play_again in ['y', 'yes']:
                break  # Continue the outer game loop
            elif play_again in ['n', 'no']:
                print("Thanks for playing! Goodbye 👋")
                exit()  # Ends the program completely
            else:
                print("❌ Invalid input. Please enter 'y' or 'n'.")

    except ValueError:
        print("Invalid input. Please enter a number.")