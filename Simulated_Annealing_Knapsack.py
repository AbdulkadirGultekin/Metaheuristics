#This will become simulated annealing for a one dimension binary knapsack problem

import numpy as np
import random
from Knapsack_constructor import knapsack_construct
from Obj_value_calculate import calc_obj
from Find_neighbours import find_neighbours
import math

#Adjust Problem Values
obj_func_coeffs = np.array([3, 5, 4, 11, 8, 2, 3, 10, 8])
weights = np.array([2, 3, 3, 10, 3, 5, 1, 3, 7])
capacity = 20
iters = 50
temp = 30
temp_update_steps = 1
temp_update_ratio = 0.95

#Get initial solution
initial_soln = knapsack_construct(obj_func_coeffs, weights, capacity)

#Set current best solution to the initial solution and best obj. value to initial solutions obj. value
best_soln = np.array(initial_soln)
best_obj = calc_obj(obj_func_coeffs, initial_soln, weights, capacity)

#Set the current solution as the initial solution
current_soln = np.array(initial_soln)
current_obj = calc_obj(obj_func_coeffs,initial_soln,weights,capacity)

#The loop for simulated annealing
for i in range(iters):
    neighbour = find_neighbours(current_soln) #Find one random neighbour of the current solution. (Note to self: different than tabu search neighbout find)
    neighbour_obj = calc_obj(obj_func_coeffs, neighbour, weights, capacity)
    if  neighbour_obj > current_obj: #If the neighbour has a better obj. function value than the current solution, move to it.
        current_soln = np.array(neighbour)
        current_obj = calc_obj(obj_func_coeffs,current_soln,weights,capacity)
    else: #Otherwise use the acceptance probability. 
        rand_value = random.uniform(0, 1)
        e_value = math.exp((neighbour_obj - current_obj)/temp)
        if rand_value < e_value:
            current_soln = np.array(neighbour)
            current_obj = calc_obj(obj_func_coeffs,current_soln,weights,capacity)
    if current_obj > best_obj: #If newly found solution is better than the best solution, update the best solution.
        best_obj = current_obj
        best_soln = np.array(current_soln)
    if  i % temp_update_steps == 0: #If the iteration is a multiple of the number of steps after which temperature will be updated, update it.
        temp = temp * temp_update_ratio
    print(best_obj)
    print(current_obj)
    print(neighbour_obj)
    print(temp)
    print(e_value)