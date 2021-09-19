import sys

population = [int(i) for i in input().split(', ')]
min_wealth = int(input())


def find_richest_index(population_list):
    richest = -sys.maxsize
    for n in range(len(population_list)):
        if population_list[n] >= richest:
            richest = n
    return richest


def is_equal(population_list, min_w):
    equality = True
    for elem in population_list:
        if elem < min_w:
            equality = False
    return equality


for n in range(len(population)):
    if population[n] < min_wealth:
        difference = min_wealth - population[n]
        richest_index = find_richest_index(population)
        population[richest_index] -= difference
        population[n] += difference


if is_equal(population, min_wealth):
    print(population)
else:
    print("No equal distribution possible")