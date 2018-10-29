import numpy as np

"""
refer my genetic.py file to understand the code 
"""
def calfitness(population, value, weight,max_weight):
    tot_value=np.sum(population*value,axis=1)
    tot_weight=np.sum(population*weight,axis=1)
    fitness=np.where(tot_weight>max_weight,0,tot_value)
    print("maximum output {}".format(max(fitness)))
    print("values are {}".format(population[np.argmax(fitness)]))
    return fitness
def matingpool(max_parents,population,fitness):
    high_fitness_index=[]
    parent=[]
    for i in range(max_parents):
        high_fitness_index.append(np.argmax(fitness))
        parent.append(population[np.argmax(fitness)])
        fitness[np.argmax(fitness)]=-999999999
    return parent
def crossover(num_parents_mating,num_var,parent):
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
    for idx in range(offspring.shape[0]):
        random_value = np.random.randint(2, size=1)
        if((offspring[idx, 1] + random_value)>=0) and ((offspring[idx, 1] + random_value)<=1):
            offspring[idx, 1] = offspring[idx, 1] + random_value
    return offspring



value=[int(x) for x in raw_input("enter value of each element").split()]
weight=[int(x) for x in raw_input("enter weight of each element").split()]
max_parents=5
num_var=len(value)
max_weight=input("enter max weight of knapsack")
iteration=100
population_size=(10,num_var)
population=np.random.randint(2,size=population_size)
for i in range(iteration):
    print("generation {}".format(i+1))
    fitness=calfitness(population=population,value=value,weight=weight,max_weight=max_weight)
    parent=matingpool(max_parents=max_parents,population=population,fitness=fitness)
    offspring=crossover(num_parents_mating=max_parents,num_var=num_var,parent=parent)
    mutated_offspring=mutation(offspring=offspring)
    population[0:max_parents]=parent
    population[max_parents:]=offspring