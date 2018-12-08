
"""
************************************************************************************************
--- Day 6: Chronal Coordinates ---
The device on your wrist beeps several times, and once again you feel like you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal interference 
detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they places it 
thinks are safe or dangerous? It recommends you check manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives 
the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by counting 
the number of integer X,Y locations that are closest to that coordinate (and aren't tied 
in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite.


************************************************************************************************

Completed:  12/6/18

************************************************************************************************
"""


def init_matrix(locations, grid):

    locations = [[0 for i in range(grid)] for j in range(grid)]

    return locations

def populate(locations, coordinates):

    for point in coordinates:
        locations[point[2]][point[1]] = "x"+str(point[0])

    return locations    

def calc_distance(point, point2):

    dist = abs(point[1] - point2[1]) + abs(point[0] - point2[0])

    return dist

def main():
  
    max_x = 0
    max_y = 0
    coordinates = []
    locations = []
    count = 0

    with open('day06_input.txt','r') as input_file:
    #with open('day06_testinput.txt','r') as input_file:
        for point in input_file:
            point = point.rstrip('\r\n')
            point = point.replace(',','')
            point = point.split(' ')
            max_x = max(max_x, int(point[0]))
            max_y = max(max_y, int(point[1]))
            coordinates.append( (int(point[0]),int(point[1])) )

    grid = max(max_x, max_y) + 50    

    #initialize matrix equal x,y from max coordinate given
    locations = init_matrix(locations, grid)

    # calculate distances for each combo in a list
    for i in range(0,grid):  
        for j in range(0,grid):  
            # lambda  for every point in empty locations matrix,calc distance from every given coordinate
            distance = list(map(lambda point: calc_distance(point, (j,i)), coordinates ))

            # for Part II:
            sum_distance = sum(distance)
            if sum_distance <10000:
                count+=1

            # figure out which is the lowest distance and get the index of the closest provided coordinate
            min_dist = min(distance)
            min_index = distance.index(min_dist)
            
            #unique minimum distance (no tie and is minimum)
            if distance.count(min_dist) == 1:
                 locations[j][i] = min_index+1
              
    # gind unbounded areas -- on the edges of the locations matrix
    unbounded = []

    for i in range(0,grid):
        # top row
        if locations[0][i] > 0:
            unbounded.append(locations[0][i])
        # bottom row
        if locations[grid-1][i] > 0:
            unbounded.append(locations[grid-1][i])    
        
    for j in range(0,grid):
        # left column
        if locations[j][0] > 0:
            unbounded.append(locations[j][0])
        # right column
        if locations[j][grid-1] > 0:
            unbounded.append(locations[j][grid-1])
    
    #pull unique values using set
    unbounded = set(unbounded)
    #print(unbounded)

    # bounded areas = coordinates not in unbounded and not ties (0)
    bounded = set(list(filter(lambda point: (point not in unbounded and point > 0), [x for x in range(len(coordinates))])))
    #print(bounded)

    # get sizes of areas in bounded set and add to dictionary
    max_area = 0
    sizes = {}
    for unbound_point in bounded:
        size = len(list(filter(lambda point: unbound_point == point, [n for line in locations for n in line])))
        sizes[unbound_point] = size
    #print(sizes) # looks legit
    
    # get max size area
    max_area = max(sizes, key=lambda point: sizes[point]) #key
    print("\nSize of max unbounded area:", sizes[max_area], "\n") #value



    #PART II

    print("total count <10000:", count, "\n")  



if __name__ == "__main__":
    main()
