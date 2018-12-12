
"""
************************************************************************************************
--- Day 7: The Sum of Its Parts ---
You must help us assemble this 'sleigh' at once!" They start excitedly 
pulling more parts out of the box.

The instructions specify a series of steps and requirements about which steps must be finished 
before others can begin (your puzzle input). Each step is designated by a single letter. 
For example, suppose you have the following instructions:
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.

Your first goal is to determine the order in which the steps should be completed. 
If more than one step is ready, choose the step which is first alphabetically


************************************************************************************************

Completed:  12/12/18

************************************************************************************************
"""

from collections import defaultdict

def print_answer(visited):

    #for step in visited:
        #print(step)
    print(''.join(str(i) for i in visited))
    return

def main():

    #https://www.hackerrank.com/challenges/defaultdict-tutorial
    
    #edges = dict()
    #indegrees = dict()

    indegrees = defaultdict(int)
    edges = defaultdict(list)
    
    next_up = []  # "queue" to hold next possible steps
    visited = []  #to keep track of processed steps 

    with open('day07_input.txt','r') as input_file:
    #with open('day07_testinput.txt','r') as input_file:
        for point in input_file:
            instruction = point.split(' ')
            x = instruction[1]
            y = instruction[7]

            edges[x].append(y)
            
            indegrees[y] +=1  #y values have x value coming in so add 1 to indegrees count for y


    for edge in edges:
            # defaultdict instead of checking for 'in'
        if indegrees[edge] == 0:
            next_up.append(edge)


    while next_up:

        next = sorted(next_up)[0]
        visited.append(next)
    
        # remove first alpha value from next_up
        # while next in next_up: 
        #   next_up.remove(next) 
        #   del next_up(next)

        next_up = [k for k in next_up if k!=next]

        # decrement indegree counts for any step where next was origin point
        for step in edges[next]:
            indegrees[step] -=1

        # if any step now has indegree value of 0 add it to the next up queue
        for step in edges[next]:
            if indegrees[step] == 0:
                next_up.append(step)

            
    print_answer(visited)



if __name__ == "__main__":
    main()
