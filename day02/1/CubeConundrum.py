def is_game_possible(game, red, green, blue):
    cube_counts = {'red': red, 'green': green, 'blue': blue}
    
    for subset in game:
        subset_cubes = subset.split(', ')
        for cube_info in subset_cubes:
            count, color = cube_info.split()
            if int(count) > cube_counts[color]:
                return False
            else:
                cube_counts[color] -= int(count)
        cube_counts = {'red': red, 'green': green, 'blue': blue}

    return True

def possible_games_sum(filename, red, green, blue):
    with open(filename, 'r') as file:
        lines = file.readlines()

    possible_sum = 0
    for line in lines:
        game_id, subsets = line.split(':')
        game_id = int(game_id.split()[-1])
        subsets = subsets.strip().split(';')

        if is_game_possible(subsets, red, green, blue):
            possible_sum += game_id

    return possible_sum

# Beispielaufruf mit den gegebenen Würfelzahlen
result = possible_games_sum('day02/input', 12, 13, 14)
print(result)