def minimum_cubes(game):
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    
    for subset in game:
        subset_cubes = subset.split(', ')
        for cube_info in subset_cubes:
            count, color = cube_info.split()
            min_cubes[color] = max(min_cubes[color], int(count))

    return min_cubes

def power_of_set(cubes):
    return cubes['red'] * cubes['green'] * cubes['blue']

def total_power_of_sets(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    total_power = 0
    for line in lines:
        subsets = line.split(':')[1].strip().split(';')
        min_cubes = minimum_cubes(subsets)
        print(min_cubes)
        total_power += power_of_set(min_cubes)

    return total_power

# Beispielaufruf mit den gegebenen Würfelzahlen
result = total_power_of_sets('day02/input')
print(result)
