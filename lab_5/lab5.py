def possible_games_sum(filename):
    limits = {'red': 12, 'green': 13, 'blue': 14}
    total = 0
    
    with open(filename) as file:
        for line in file:
            game_id, rounds = line.split(": ")
            game_id = int(game_id.split()[1])

            rounds_list = [pair.split() for round in rounds.split("; ") for pair in round.split(", ")]
            if all(int(num) <= limits[color] for num, color in rounds_list):
                total += game_id
    
    return total

print(possible_games_sum("input.txt"))
#result: 2810