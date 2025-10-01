from lab7.dice import roll_D6, roll_D12

#Number of wins needed to win the game
winning_score = 3
#Array for storing the names of the players
player_names = []
#Array for storing the number of wins for each player
player_wins = []
rounds = 0
number_of_players = int(input("How many players?"))


for i in range(number_of_players):
    name = input(f"What is the name of Player {i+1}?")
    player_names.append(name)

for i in range(number_of_players):
    player_wins.append(0)


player_rolls_history = []

for i in range(number_of_players):
    player_rolls_history.append([])
    
gameover = False
while not gameover:
    print(f"\nRound {rounds + 1}:")
    current_totals = []
    
    #we need to roll the dice for each player
    for i in range(number_of_players):
        d6 = roll_D6()
        d12 = roll_D12()
        total = d6 + d12
        current_totals.append(total)
        player_rolls_history[i].append(total)
        print(f"Player names {player_names[i]} rolled: ({d6}, {d12}) Total is {total}")
    
    input("\nPress Enter to continue...")
    #obtain the highest roll this round:
    max_roll = max(current_totals)

    winners = []

    for j in range(len(current_totals)):
        if current_totals[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j] += 1
    print(f"Winners of this round are: {winners}")

    for z in range(number_of_players):
        if player_wins[z] >= winning_score:
            print(f"\n {player_names[z]} is the newest battle of dices champion!")
            gameover = True
    
    if gameover is False:
            print("Battle is still going on. Who will win?")

    rounds +=1

filename = input("\nEnter the filename to save results ")
with open(filename, "w") as file:
    for round_number in range(rounds):
        file.write(f"Round {round_number + 1}: ")
        rolls_str = ""
        for i in range(number_of_players):
            rolls_str += f"{player_names[i]} rolled {player_rolls_history[i][round_number]}"
            if i < number_of_players - 1:
                rolls_str += ", "
        print(f"Saving {rolls_str}")
        file.write(rolls_str + "\n")


# It is me again, Lukas! HELLOOOOOO WORLD!
