"""Travelling salesman using Genetic Algorithm"""

import random
import operator
import numpy as np 
import matplotlib
matplotlib.use('TkAgg') # Or 'Qt5Agg' or 'QtAgg'
import matplotlib.pyplot as plt 
from geopy.geocoders import Nominatim
import time 

class City:
    def __init__(self , x, y, name):
        # A constructor to initialize a City object with its coordinates (x, y) and name.
        self.x = x
        self.y = y
        self.name = name
    
    def __repr__(self):
        return self.name + " (" + str(self.x)+ " , " + str(self.y) + " )"
    
    # This is a method to calculate the straight-line distance between two cities.
    # using Pythagorean theorem.
    def get_distance(self ,city):
        return (np.sqrt((city.x - self.x)**2 +(city.y - self.y)**2))


# helper function to calculate the total distance of a route.
# It sums up the distances between consecutive cities and connects the last city back to the first.
def get_total_distance(route):
    dist = 0.0
     
    for i in range(len(route)-1):
        dist += route[i].get_distance(route[i+1])
    dist += route[-1].get_distance(route[0]) # This closes the loop to form a complete circuit.
    return dist

# function to read city names from a text file and get their coordinates using geopy.
def read_cities(PNames):
    P=[]
    geolocator = Nominatim(user_agent = "VARUN_APP")
    with open("india_cities_GA.txt", "r") as file:
        for line in file:
            city_name = line.strip()
            if not city_name:
                continue
            
            city_query = city_name + ", India"
            
            try:
                pt = geolocator.geocode(city_query, timeout=10)
                if pt:
                    y = round(pt.latitude, 2)
                    x = round(pt.longitude, 2)
                    P.append(City(x, y, city_name))
                    PNames.append(city_name)
                    print(f"City: {city_name}, Coordinates: ({x}, {y})")
                else:
                    print(f"Could not find coordinates for: {city_name}")
            except Exception as e:
                print(f"Error geocoding {city_name}: {e}")
                time.sleep(2) # added a 2-second delay to avoid getting blocked for too many requests.
    return P

# function plots the route on a graph.
def plot_route(route, tot_dist, PNames):
    #creating an array of coordinates to plot the path.
    Pt = [[city.x, city.y] for city in route]
    Pt.append([route[0].x, route[0].y]) 
    Pt = np.array(Pt) 
    
    plt.figure()
    plt.title(f'Total Distance: {tot_dist:.2f}')
    plt.plot(Pt[:, 0], Pt[:, 1], '-o') # '-o' makes it a line with dots.
    
    # This loop adds the city names as labels on the plot.
    for i, city in enumerate(route):
        plt.annotate(city.name, (city.x, city.y), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.show()

# A class to calculate the "fitness" of each route.
# The shorter the route, the higher its fitness.
class Fitness:
    def __init__(self , route):
        self.route = route
        self.distance = 0.0
        self.fitness = 0.0

    # This method calculates the distance of the route.
    def route_distance(self):
        if self.distance == 0:
            self.distance = get_total_distance(self.route)
        return self.distance

    # This method calculates the fitness. It's the reciprocal of the distance
    def get_fitness(self):
        if self.fitness == 0:
            self.fitness = 1.0 / self.route_distance()
        return self.fitness
    
# Function to create a single random route. This is one "individual" in our population
def create_route(P):
    return random.sample(P , len(P))
    
# Function to create the very first population of random routes
def initial_population(pop_size , P):
    population = []
    for _ in range( 0 , pop_size):
        population.append(create_route(P))
    return population

# This ranks the population from most fit to least fit
def rank_routes(population):
    fitness_result = {}
    for i in range (0 , len(population)):
        fitness_result[i] = Fitness(population[i]).get_fitness()
    # It returns a sorted list of tuples, where each tuple is index, fitness_score
    return sorted(fitness_result.items() , key=operator.itemgetter(1) , reverse=True)

# This selects the best individuals "elite" to pass on their genes to the next generation
# I'm using a simple selection method here.
def selection(ranked_population, elite_size):
    selection_result = []
    
    for _ in range(len(ranked_population)):
        # I'm picking a few random individuals and choosing the best one to survive
        individual = random.sample(ranked_population, elite_size) 
        best_individual = max(individual, key=lambda x: x[1])
        selection_result.append(best_individual[0])             

    return selection_result

# This creates the "mating pool" of individuals that will be used for crossover.
def mating_pool(population , selection_result):
    mating_pool = []
    for i in range (len(selection_result)):
        mating_pool.append(population[selection_result[i]])
    return mating_pool

# This is the "crossover" or "mating" function. It combines two parent routes to create a new child route.
def crossover(parent1 ,parent2):
    child_p1 = []
    
    gene_a = int(random.random() * len(parent1))
    gene_b = int(random.random() * len(parent1))

    start_gene = min(gene_a , gene_b)
    end_gene =  max(gene_a , gene_b)
    # I'm taking a slice of genes (cities) from parent1.
    for i in range(start_gene , end_gene):
        child_p1.append(parent1[i])
    
    # Then I'm filling the rest of the child with the remaining cities from parent2 in their original order.
    child_p2 = [item for item in parent2 if item not in child_p1]

    return child_p1 + child_p2

# This function creates a whole new generation of children.
def create_children(mating_pool , elite_size):
    children = []
    n = len(mating_pool) - elite_size
    pool = random.sample(mating_pool, len(mating_pool))
    # First I'm just copying the best individuals from the previous generation (the elite) directly.
    for i in range(elite_size):
        children.append(mating_pool[i])
    # Then I'm creating the rest of the children through crossover.
    for i in range(n):
        child  =crossover(pool[i] , pool[len(mating_pool) - i - 1])
        children.append(child)
    
    return children

# This function introduces random changes (mutations) into a route.
# It randomly swaps two cities to prevent the algorithm from getting stuck in a local minimum.
def mutation(individual , mutation_probability):
    for i in range(len(individual)):
        if random.random()  < mutation_probability:
            j = int(random.random()  * len(individual))

            city1 = individual[i]
            city2 = individual[j]

            individual[i] = city2
            individual[j] = city1

    return individual

# This applies mutation to the entire population.
def mutate_population(population , mutation_probability):
    mutated_population =[]
    for individual in population:
        mutated_individual = mutation(individual ,mutation_probability)
        mutated_population.append(mutated_individual)
    return mutated_population

# This is the heart of the algorithm. It generates the next generation.
def next_generation(current_generation , elite_size , mutation_probability):
    # 1 Rank the current population by fitness.
    ranked_population = rank_routes(current_generation)
    # 2 Select the individuals that will reproduce.
    selection_result = selection(ranked_population , elite_size)
    # 3 Create the mating pool.
    mating_pool_population = mating_pool(current_generation , selection_result)
    # 4 Create a new generation of children through crossover.
    new_children = create_children(mating_pool_population , elite_size)
    # 5 Apply mutations to the new generation.
    next_generation = mutate_population(new_children , mutation_probability)

    return next_generation

# This is the main function that runs the entire genetic algorithm.
def genetic_algorithm(pop_size , elite_size , mutation_probability , generations):
    PNames = []
    # I'm getting the list of cities from the file.
    P = read_cities(PNames)
    
    if not P:
        print("No cities found. Exiting.")
        return

    # I'm creating the initial, random population.
    population = initial_population(pop_size , P)
    progress =[]
    old_distance = get_total_distance(population[0])
    print(f"Initial distance :: {old_distance}")
    progress.append(1/rank_routes(population)[0][1])

    # The main loop that runs for a set number of generations.
    for gen in range(1 , generations+1):
        population = next_generation(population , elite_size , mutation_probability)
        best_route_ind = rank_routes(population)
        best_route = population[best_route_ind [0][0]]

        progress.append(1 / best_route_ind[0][1])

        if gen%25 ==0:
            new_distance = get_total_distance(best_route)
            print(f"Generation {gen} :: Distance = {new_distance}")

    best_route_ind = rank_routes(population)[0][0]
    best_route = population[best_route_ind]
    print(f"\nFinal distance = {get_total_distance(best_route)}\n")
    
    # I'm plotting the final best route.
    plot_route(best_route, get_total_distance(best_route), PNames)

    # I'm also plotting the progress of the algorithm over time.
    plt.figure()
    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.title('Distance over Generations')
    plt.show()

if __name__ == "__main__":
    # These are the main parameters I can tweak to see how the algorithm behaves.
    pop_size = 100
    elite_size = 20
    mutation_probability = 0.01
    generations = 200
    # Let's start the genetic journey!
    genetic_algorithm(pop_size , elite_size , mutation_probability , generations)