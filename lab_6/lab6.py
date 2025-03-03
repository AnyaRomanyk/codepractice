def calculate_score(filename):
    shape_score = {'X': 1, 'Y': 2, 'Z': 3}
    outcome_score = {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
                     ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
                     ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3}
    
    total_score = 0
    
    with open(filename) as file:
        for line in file:
            opponent, you = line.strip().split()
            total_score += shape_score[you] + outcome_score[(opponent, you)]
    
    return total_score

print(calculate_score("input.txt"))
#result: 8933
