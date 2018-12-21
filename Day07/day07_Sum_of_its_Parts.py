
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

--- Part Two ---

Now, you need to account for multiple people working on steps simultaneously. If multiple 
steps are available, workers should still begin them in alphabetical order.

Each step takes 60 seconds plus an amount corresponding to its letter: A=1, B=2, C=3, and 
so on. So, step A takes 60+1=61 seconds, while step Z takes 60+26=86 seconds. No time 
is required between steps.


************************************************************************************************

Completed:  Part 1 12/12/18

************************************************************************************************
"""

from collections import defaultdict


# def get_time(step, base_time):
#     time = ord(step)-64 + base_time
#     #print(time)
#     return time

def print_answer(message, finished):

    print(message, ''.join(str(i) for i in finished))
    return




def main():

    #https://www.hackerrank.com/challenges/defaultdict-tutorial
    
    #edges = dict()
    #indegrees = dict()

    indegrees = defaultdict(int)
    edges = defaultdict(list)
    
    next_up = []  # "queue" to hold next possible steps
    finished = []  #to keep track of processed steps 

    #with open('day07_input.txt','r') as input_file:
    with open('day07_testinput.txt','r') as input_file:
        for point in input_file:
            instruction = point.split(' ')
            x = instruction[1]
            y = instruction[7]

            edges[x].append(y)
            
            indegrees[y] +=1  #y values have x value coming in so add 1 to indegrees count for y

    for vertex in edges:
            # defaultdict instead of checking for 'in'
        if indegrees[vertex] == 0:
            next_up.append(vertex)


    while next_up:

        next = sorted(next_up)[0]
        finished.append(next)
    
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

            
    print_answer("Part I:",finished)
    print("\n")

    #  PART II
    
    #reset
    indegrees = defaultdict(int) 
    edges = defaultdict(list)  # can be reused
    tasks = set()
    next_up = []  # "queue" to hold next possible steps
    finished = [] #set()  #to keep track of processed steps
    f_task = 0

    BASE_TIME = 60
    WORKERS = 5  
    time = [0 for _ in range(WORKERS)]
    work = [None for _ in range(WORKERS)]
    elapsed_time = 0


    # reload indegrees 
    with open('day07_input.txt','r') as input_file:
    #with open('day07_testinput.txt','r') as input_file:
        for point in input_file:
            instruction = point.split(' ')
            x = instruction[1]
            y = instruction[7]

            edges[x].append(y)  #x = set of all vertices
            indegrees[y] +=1  #y values have x value coming in so add 1 to indegrees count for y

    for vertex in edges:
        # if indegrees = 0 then this is our starting step
        if indegrees[vertex] == 0:
            next_up.append(vertex)
    
    # populate tasks using defaultdict to get start and end
    for task in indegrees:
        tasks.add(task)

    

    while tasks:  #while there are still tasks to be assigned

        elapsed_time +=1

        for i in range(0,len(time)):
            if time[i] > 0:

                time[i] -=1

                if time[i] == 0:   # we've just finished a job
                    f_task = work[i]

                    # move task from tasks to finished 
                    tasks.remove(f_task)
                    finished.append(f_task)

                    # remove from up_next
                    #next_up.remove(f_task)

                    # set helpers task to None - remove task
                    work[i] == None

                    # if any step now has indegree value of 0 add it to the next up queue
                    for step in edges[f_task]:
                        indegrees[step] -=1
                    
                        if indegrees[step] == 0:
                            next_up.append(step)


        while 0 in time and len(next_up) > 0:  # there is someone who is free to help and a task available
            free = time.index(0)
            # assign the next up task
            work[free] = next_up[0]
            time[free] = ord(next_up[0])-64 + BASE_TIME

            next_up.remove(next_up[0])


    print_answer("Part II:",finished)
    print("Total Elapsed Time", elapsed_time-1)  
    print("\n")





if __name__ == "__main__":
    main()
