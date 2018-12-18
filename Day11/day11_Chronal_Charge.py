
"""
************************************************************************************************
--- Day 10: The Stars Align ---

part I:

Each fuel cell has a coordinate ranging from 1 to 300 in both the X (horizontal) and Y (vertical) direction. 
In X,Y notation, the top-left cell is 1,1, and the top-right cell is 300,1.

The interface lets you select any 3x3 square of fuel cells. To increase your chances of getting 
to your destination, you decide to choose the 3x3 square with the largest total power.

The power level in a given fuel cell can be found through the following process:

Find the fuel cell's rack ID, which is its X coordinate plus 10.
--Begin with a power level of the rack ID times the Y coordinate.
--ncrease the power level by the value of the grid serial number (your puzzle input).
--Set the power level to itself multiplied by the rack ID.
--Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
--Subtract 5 from the power level.
    

--- Part Two ---

--- Part Two ---
You discover a dial on the side of the device; it seems to let you select a square of any size, 
not just 3x3. Sizes from 1x1 to 300x300 are supported.

Realizing this, you now must find the square of any size with the largest total power. 
Identify this square by including its size as a third parameter after the top-left coordinate: 
a 9x9 square with a top-left corner of 3,5 is identified as 3,5,9.

What is the X,Y,size identifier of the square with the largest total power?

************************************************************************************************

Completed:  12/17/18
************************************************************************************************
"""


def main():
    
    SERIAL_NUMBER = 6878
    n = 300
    max_sum = max_size = max_x = max_y = 0
    sum = 0
    fuel_cells = [[0 for y in range(300)] for x in range(300)]


    for y in range (0,n):
        for x in range(0,n):
            rack_id = (x) + 10
            power_level = rack_id * (y)
            power_level += SERIAL_NUMBER
            power_level *= rack_id
            # keep only the hundreds digit
            power_level = (power_level // 100)%10
            power_level -=5

            fuel_cells[y][x] = power_level
     


    
    # long way around - something dynamic would be faster
    for z in range(1,301):
        print("DEBUG: z:", z)

        for y in range(0,n-(z-1)):
            for x in range(0,n-(z-1)):
                sum = 0

                for i in range(x,x+z):
                    for j in range(y,y+z):
                        sum+=fuel_cells[i][j]

                if sum > max_sum:
                    max_sum = sum
                    max_y = y
                    max_x = x
                    max_size = z
        print(max_sum, max_y, max_x, max_size)            
    print("sum:", max_sum, "x,y:", max_y, max_x, "size:", max_size)


if __name__ == "__main__":
    main()
