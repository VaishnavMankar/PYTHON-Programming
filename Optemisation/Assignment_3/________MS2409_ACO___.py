from geopy.geocoders import Nominatim
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math, random

class Ant:
    def __init__(self, id, ph, currentCity):
        self.id = id
        self.ph = ph
        self.allowedCities = []
        self.distanceTravelled = 0.0
        self.currentCity = currentCity
        self.route = []

    def chooseCity(self, pheromoneMatrix, distanceMatrix):
        if len(self.allowedCities) == 0:
            return None
        selection, highestP, factor = None, 0, 0
        for city in self.allowedCities:
            if distanceMatrix.at[self.currentCity.name, city] != 0.0:
                factor += (pheromoneMatrix.at[self.currentCity.name, city] /
                           distanceMatrix.at[self.currentCity.name, city])
        if factor == 0:
            return None
        for city in self.allowedCities:
            if distanceMatrix.at[self.currentCity.name, city] != 0.0:
                p = (pheromoneMatrix.at[self.currentCity.name, city] /
                     distanceMatrix.at[self.currentCity.name, city]) / factor
                if p > highestP:
                    highestP = p
                    selection = city
        return selection

    def reset(self, initialPh):
        self.ph = initialPh
        self.allowedCities = []
        self.distanceTravelled = 0.0
        self.route = []

class City:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

def distance(C1, C2):
    return math.sqrt((C1.x - C2.x) ** 2 + (C1.y - C2.y) ** 2)

def getTotalDistance(route):
    dist = 0.0
    for i in range(len(route) - 1):
        dist += distance(route[i], route[i + 1])
    dist += distance(route[-1], route[0])
    return dist

def Plot(route, dist, Pnames):
    Pt = np.array([[r.x, r.y] for r in route] + [[route[0].x, route[0].y]])
    plt.title(f"(ACO) Total distance = {dist:.2f}")
    plt.plot(Pt[:, 0], Pt[:, 1], '-o')
    for i, city in enumerate(route):
        plt.annotate(city.name, (Pt[i][0], Pt[i][1]))
    plt.show(block=False)
    plt.pause(0.05)
    plt.cla()

def getCityObj(name, citylist):
    for city in citylist:
        if city.name == name:
            return city
    return None

def readcities(Pnames):
    citylist = []
    j = 0
    geolocator = Nominatim(user_agent="VARUN_App")
    with open("Indian_cities.txt") as file:
        for line in file:
            city = line.strip()
            if city == "":
                continue
            Pnames.insert(j, city)
            pt = geolocator.geocode(city + ", India", timeout=10000)
            citylist.append(City(pt.latitude, pt.longitude, city))
            j += 1
    return citylist

def distance_matrix(citylist, cityNames):
    l = len(citylist)
    df = pd.DataFrame(np.zeros((l, l)), index=cityNames, columns=cityNames)
    for r in df.index:
        for c in df.columns:
            if r != c:
                c1 = getCityObj(r, citylist)
                c2 = getCityObj(c, citylist)
                df.at[r, c] = distance(c1, c2)
                df.at[c, r] = df.at[r, c]
    return df

def pheromoneMatrix(citylist, cityNames):
    df = pd.DataFrame(np.full((len(citylist), len(citylist)), 0.1),
                      index=cityNames, columns=cityNames)
    return df

def createAntSample(m, cities):
    pheromones = np.random.normal(loc=10, scale=1, size=m)
    ants = [Ant(i+1, pheromones[i], getCityObj('Pune', cities)) for i in range(m)]
    return ants

def antColonyOptimization(cities, pnames, m, maxIterations, rho):
    dM = distance_matrix(cities, pnames)
    pM = pheromoneMatrix(cities, pnames)
    ants = createAntSample(m, cities)
    bestTour, bestDistance = None, float('inf')

    for iters in range(maxIterations):
        for ant in ants:
            if iters > 0:
                ant.reset(10.0)
                ant.currentCity = getCityObj('Pune', cities)
            ant.allowedCities = pnames.copy()
            ant.allowedCities.remove('Pune')
            ant.route = [ant.currentCity]

            for _ in range(len(cities) - 1):
                nextCityName = ant.chooseCity(pM, dM)
                nextCity = getCityObj(nextCityName, cities)
                if not nextCity:
                    break
                ant.distanceTravelled += distance(ant.currentCity, nextCity)
                ant.route.append(nextCity)
                ant.allowedCities.remove(nextCity.name)
                ant.currentCity = nextCity

            ant.distanceTravelled += distance(ant.route[-1], ant.route[0])

            if ant.distanceTravelled < bestDistance:
                bestDistance = ant.distanceTravelled
                bestTour = ant.route.copy()

        # Evaporation
        pM *= rho

        # Deposit pheromones
        for ant in ants:
            for i in range(len(ant.route) - 1):
                c1, c2 = ant.route[i], ant.route[i + 1]
                delta = 1 / ant.distanceTravelled
                pM.at[c1.name, c2.name] += delta
                pM.at[c2.name, c1.name] += delta

        if bestTour is not None:
            Plot(bestTour, bestDistance, pnames)

        if iters % 10 == 0 or iters == maxIterations - 1:
            print(f"Iteration {iters}: Best Distance = {bestDistance:.2f}")

    plt.close()

if __name__ == '__main__':
    m = 20
    iters = 100
    rho = 0.7
    pnames = []
    cities = readcities(pnames)
    antColonyOptimization(cities, pnames, m, iters, rho)
