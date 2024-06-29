#This will become a tabu search for a one dimension binary knapsack problem.

#import necessary packages

import numpy as np
from Knapsack_constructor import knapsack_construct
from Obj_value_calculate import calc_obj
from Find_neighbours import find_neighbours

#Adjust problem values
obj_func_coeffs = np.array([3, 5, 4, 11, 8, 2, 3, 10, 8])
weights = np.array([2, 3, 3, 10, 3, 5, 1, 3, 7])
capacity = 20
iters = 10
tabu_length = 2
tabu_list = np.empty(tabu_length, dtype=int)

#Get initial solution
initial_soln = knapsack_construct(obj_func_coeffs, weights, capacity)

#Set current best solution to the initial solution and best obj. value to initial solutions obj. value
best_soln = np.array(initial_soln)
best_obj = calc_obj(obj_func_coeffs, initial_soln, weights, capacity)

#Set the current solution as the initial solution
current_soln = np.array(initial_soln)

#The loop for tabu search
for i in range(iters):
    neighbours = find_neighbours(current_soln) #Find all neighbours of current solution
    neigh_objs = np.zeros(len(neighbours)) #Initialize the objective function values of the neighbours as 0
    for j in range(len(neighbours)):
        if j in tabu_list:
            neigh_objs[j] = -np.inf #If the neighbour is attained through a tabu move, set its objective function value as negative infinity
        else:
            neigh_objs[j] = calc_obj(obj_func_coeffs, neighbours[j], weights, capacity) #Otherwise calculate the objective function value
    max_index = neigh_objs.argmax() #Find the neighbour with the best objective function value
    max_val = neigh_objs[max_index]
    if max_val > best_obj: #If the best neighbour has a better objective function value than the current best, update the best solution and its value.
        best_obj = max_val
        best_soln = np.array(neighbours[max_index])
    current_soln = np.array(neighbours[max_index]) #Update the current solution.
    tabu_list =np.array(tabu_list[:-1]) #Update the tabu list.
    tabu_list = np.insert(tabu_list, 0, max_index)

print(best_obj)
print(best_soln)
