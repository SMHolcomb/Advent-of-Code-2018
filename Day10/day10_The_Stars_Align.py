
"""
************************************************************************************************
--- Day 10: The Stars Align ---

You can see these points of light floating in the distance, and record their position in the 
sky and their velocity, the relative change in position per second (your puzzle input). The 
coordinates are all given from your perspective; given enough time, those positions and velocities will move 
the points into a cohesive message!
    

--- Part Two ---
Good thing you didn't have to wait, because that would have taken a long time - much longer than the 3 
seconds in the example above.

Impressed by your sub-hour communication capabilities, the Elves are curious: 
exactly how many seconds would they have needed to wait for that message to appear?                 
************************************************************************************************

Completed:  12/17/18
************************************************************************************************
"""
import re
import copy

def print_points(points):
    for p in points:
        print(p)
    return

def move_points(p):
    p[0] += p[2]
    p[1] += p[3]

    return p

def get_size(points):
    min_x = max_x = min_y = max_y = 0
    max_x = max(map(lambda x:x[0], points))
    min_x = min(map(lambda x:x[0], points))
    max_y = max(map(lambda y:y[1], points))
    min_y = min(map(lambda y:y[1], points))

    return ( ( (max_x - min_x) + 1) * ( ( max_y - min_y) + 1) )

def show_message(prev_points):

    max_x = max(map(lambda x:x[0], prev_points))
    min_x = min(map(lambda x:x[0], prev_points))
    max_y = max(map(lambda y:y[1], prev_points))
    min_y = min(map(lambda y:y[1], prev_points))

    d_points = set()  # x,y points only to display
    for point in prev_points:
        p = (point[0],point[1])
        d_points.add(p)
    #print(d_points)


    for y in range(min_y,max_y+1):
        line = ""
        #line=[]
        for x in range(min_x, max_x+1):
            if (x,y) in d_points:
                #line.append("#")
                line +="#"
            else:
                #line.append(" ")
                line +=" "
        
        #print("".join(line))
        print(line)

    #return

def main():
    
    points = []
    prev_points = []
    prev_size = curr_size = 0
    time = 0

    with open('day10_input.txt','r') as input_file:
    #with open('day10_testinput.txt','r') as input_file:
        for p in input_file:
            match = re.findall(r'-?\d+', p)   
            points.append( [int(match[0]),int(match[1]), int(match[2]), int(match[3])] )

    while True:
        time +=1
        prev_points = copy.deepcopy(points)
        prev_size = get_size(points)
       
        for p in points:
            move_points(p)  

        # get new size of matrix needed to hold points -- theoretically should get smaller
        curr_size = get_size(points)

        if curr_size > prev_size:    # matrix is growing 
            # revert to prev_points and print out message
            print("\n")
            show_message(prev_points)
            break
    print("\nTime:" , time-1, "\n")


if __name__ == "__main__":
    main()
