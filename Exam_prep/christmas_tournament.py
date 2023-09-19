tournament_days = int(input())

total_money_won = 0
games_won = 0
games_lost = 0

for current_day in range(tournament_days):
    sport_type = input()
    daily_wins = 0
    daily_games_won = 0
    daily_games_lost = 0

    while sport_type != "Finish":
        result = input()
        if result == "win":
            daily_wins += 20
            games_won += 1
            daily_games_won += 1
        elif result == "lose":
            games_lost += 1
            daily_games_lost += 1

        sport_type = input()

    if daily_games_won > daily_games_lost:
        daily_wins *= 1.1
    total_money_won += daily_wins

if games_won > games_lost:
    total_money_won *= 1.2
    print(f"You won the tournament! Total raised money: {total_money_won:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money_won:.2f}")