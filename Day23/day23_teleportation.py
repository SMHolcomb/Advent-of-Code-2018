
"""
************************************************************************************************
--- Day 23: Experimental Emergency Teleportation ---

The device lists the X,Y,Z position (pos) for each nanobot as well as its signal radius (r) on its tiny 
screen (your puzzle input).

Each nanobot can transmit signals to any integer coordinate which is a distance away from it less than or 
equal to its signal radius (as measured by Manhattan distance). Coordinates a distance away of less 
than or equal to a nanobot's signal radius are said to be in range of that nanobot.

Before you start the teleportation process, you should determine which nanobot is the strongest 
(that is, which has the largest signal radius) and then, for that nanobot, the total number of 
nanobots that are in range of it, including itself.
    
Find the nanobot with the largest signal radius. How many nanobots are in range of its signals?

--- Part Two ---

************************************************************************************************

Completed:  1/5/19
************************************************************************************************
"""
import re



def main():
    
    nanobots = {}
    i = 0    
    counter = 0

    with open('day23_input.txt','r') as input_file:
    #with open('day23_testinput.txt','r') as input_file:
        for n in input_file:
            match = re.findall(r'-?\d+', n)   
            x = ( [int(match[0]),int(match[1]), int(match[2]), int(match[3])] )
            nanobots[i] = x
            i+=1   

    max_nano = max(nanobots, key=lambda x: nanobots.get(x)[3])
    max_range = nanobots.get(max_nano)[3]


    for bot in nanobots:
        dist = abs(nanobots.get(max_nano)[0] - nanobots.get(bot)[0]) +  \
            abs(nanobots.get(max_nano)[1] - nanobots.get(bot)[1]) + \
            abs(nanobots.get(max_nano)[2] - nanobots.get(bot)[2]) 
        if dist <= max_range:
            counter+=1

    print("Part I - Nanobots within range:", counter)




if __name__ == "__main__":
    main()
