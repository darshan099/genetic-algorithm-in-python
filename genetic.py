import numpy as np

def calfitness(eq_inputs,population):
    # Calculating the fitness value of each solution in the current population.
    fitness=np.sum(eq_inputs*population,axis=1)
    print("maximum output {}".format(max(fitness)))
    print("values are {}".format(population[np.argmax(fitness)]))
    return fitness
def matingpool(num_parents_mating,population,fitness):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    high_fitness_index=[]
    parent=[]
    for i in range(num_parents_mating):
        high_fitness_index.append(np.argmax(fitness))
        parent.append(population[np.argmax(fitness)])
        fitness[np.argmax(fitness)]=-9999999999
    return parent
def crossover(num_parents_mating,num_var,parent):
    # The point at which crossover takes place between two parents. Usually it is at the center.
    mid_index=int(num_var/2)
    parent_crossover=[]
    final_parent_crossover=np.empty((num_parents_mating,num_var))
    for i in range(num_parents_mating-1):
        parent_crossover[0:mid_index]=parent[i][0:mid_index]
        parent_crossover[mid_index:]=parent[i+1][mid_index:]
        final_parent_crossover[i]=parent_crossover
    parent_crossover[0:mid_index]=parent[num_parents_mating-1][0:mid_index]
    parent_crossover[mid_index:]=parent[0][mid_index:]
    final_parent_crossover[num_parents_mating-1]=parent_crossover
    return final_parent_crossover
def mutation(offspring):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring.shape[0]):
        random_value = np.random.uniform(-10, 10, 1)
        if((offspring[idx, 1] + random_value)>0):
            offspring[idx, 1] = offspring[idx, 1] + random_value
    return offspring

"""
The y=target is to maximize this equation ASAP:
    y = w1x1+w2x2+w3x3+w4x4+w5x5+6wx6
    where (x1,x2,x3,x4,x5,x6)=(4,-2,3.5,5,-11,-4.7)
    What are the best values for the 6 weights w1 to w6?
    We are going to use the genetic algorithm for the best possible values after a number of generations.
"""
# Inputs of the equation.
print("enter the size of polynomial")
raw_input()
print("enter the values of constants")
eq_inputs=[int(x) for x in raw_input().split()]

# Number of the weights we are looking to optimize.
num_var=len(eq_inputs)
num_parents_mating=5

#defining generations
iteration=100

# Defining the population size.
population_size=(10,num_var)

#initial population
population=np.random.uniform(low=0,high=100,size=population_size)
print("population {}".format(population))
for i in range(iteration):
    print("generation {}".format(i+1))
    # Measing the fitness of each chromosome in the population.
    fitness=calfitness(eq_inputs,population)

    # Selecting the best parents in the population for mating.
    parent=matingpool(num_parents_mating=num_parents_mating,population=population,fitness=fitness)
    
    # Generating next generation using crossover.  
    offspring=crossover(num_parents_mating=num_parents_mating,num_var=num_var,parent=parent)

    # Adding some variations to the offsrping using mutation.
    mutated_offspring=mutation(offspring=offspring)

    # Creating the new population based on the parents and offspring.
    population[0:num_parents_mating]=parent
    population[num_parents_mating:]=offspring