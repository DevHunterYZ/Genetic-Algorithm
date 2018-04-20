import sys
import random

# Gen sınıfı
class gen:
    sample=None
    fitness=None
    def __init__(self,sample_value,fitness_value):
        self.sample=sample_value
        self.fitness=fitness_value

# Fonksiyonu tanımla
def calculate_fitness(value):
    function=15*value-value*value
    return function

def generate_random_generation(length,quantity):
    max_value = 15
    min_value = 0
    generation_list=[]
    for i in range(0,quantity):
        value = int(random.uniform(min_value,max_value+1))
        binary=bin(value)[2:]
        binary=binary.zfill(length)
        generation_list.append(binary)
    test=['1100','0100','0001','1110','0111','1001']
    return test
    #döndür generation_list

def fitness_calculation(generation_list):
    fitness_list=[]
    generation_sum=0
    for i in range(0,len(generation_list)):
        generation_sum=generation_sum+calculate_fitness(int(generation_list[i],2))
    for i in range(0,len(generation_list)):
        fitness=calculate_fitness(int(generation_list[i],2))
        fitness_list.append(round((fitness/(generation_sum*1.0))*100.0,2))
    return fitness_list

def min_index(generation_fitness,invalid):
    min=-1
    min_value=sys.minint
    for i in range(0,len(generation_fitness)):
        if min_value>generation_fitness[i] and i!=invalid:
            min_value=generation_fitness[i]
            min=i
    return min

def sort_gene_list(gene_list):
    return sorted(gene_list,key=lambda x: x.fitness, reverse=True)

def crossover(generation_list,generation_fitness,length):
    probability_value_in_number=int(len(generation_list)*.7)
    gene_list=[]
    for i in range(0,len(generation_list)):
        gene_list.append(gene(generation_list[i],generation_fitness[i]))
    gene_list=sort_gene_list(gene_list)
    breaking_point=random.randrange(1,length)
    # kırılma noktası = 2
    first_portion=[]
    second_portion=[]
    for i in range(0,probability_value_in_number):
        first_portion.append(gene_list[i].sample[0:breaking_point])
        second_portion.append(gene_list[i].sample[breaking_point:length])
    semi_new_generation=[]
    start=1
    # -----------------------------------------------------
    for i in range(0,len(generation_list)):
        if i<=probability_value_in_number-1 and (i+1)<len(second_portion):
            semi_new_generation.append(first_portion[0]+second_portion[i+1])
        else:
            semi_new_generation.append(second_portion[0] + first_portion[start])
            start=start+1
    return semi_new_generation

def mutation(new_generation):
    random_selection = random.randrange(0, len(new_generation))
    if new_generation[random_selection][0:1] == '1':
        new_generation[random_selection] = new_generation[random_selection][0:1].replace('1', '0') + new_generation[
                                                                                                         random_selection][
                                                                                                     1:]
    else:
        new_generation[random_selection] = new_generation[random_selection][0:1].replace('0', '1') + new_generation[
                                                                                                         random_selection][
                                                                                                     1:]
    return new_generation

def genetic_algorithm(length,quantity,iteration):
    new_generation=generate_random_generation(length, quantity)
    for i in range (0,iteration):
        generation_fitness=fitness_calculation(new_generation)
        print ('----------------------------------')
        print ('----------------------------------')
        print (i,'.nesil ve onların fitness değeri:')
        for j in range(0,len(new_generation)):
            print ('Gen',new_generation[j],'Fitness',generation_fitness[j])
        semi_new_generation=crossover(new_generation,generation_fitness,length)
        new_generation=mutation(semi_new_generation)

genetic_algorithm(4,6,100)
