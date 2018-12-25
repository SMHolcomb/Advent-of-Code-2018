
"""
************************************************************************************************
--- Day 9: Marble Mania ---

The Elves play this game by taking turns arranging the marbles in a circle according to very particular 
rules. The marbles are numbered starting with 0 and increasing by 1 until every marble has a number.

First, the marble numbered 0 is placed in the circle. At this point, while it contains only a 
single marble, it is still a circle: the marble is both clockwise from itself and counter-clockwise 
from itself. This marble is designated the current marble.

Then, each Elf takes a turn placing the lowest-numbered remaining marble into the circle between 
the marbles that are 1 and 2 marbles clockwise of the current marble. (When the circle is large 
enough, this means that there is one marble between the marble that was just placed and the current 
arble.) The marble that was just placed then becomes the current marble.

However, if the marble that is about to be placed has a number which is a multiple of 23, 
something entirely different happens. First, the current player keeps the marble they would 
have placed, adding it to their score. In addition, the marble 7 marbles counter-clockwise 
from the current marble is removed from the circle and also added to the current player's 
score. The marble located immediately clockwise of the marble that was removed 
becomes the new current marble.

# MY PUZZLE INPUT:  424 players; last marble is worth 71482 points

--- Part Two ---
Amused by the speed of your answer, the Elves are curious:

What would the new winning Elf's score be if the number of the last marble were 100 times larger?


************************************************************************************************

Completed:  12/24/18

************************************************************************************************
"""

class Marble:

    def __init__(self, i):

        self.next = self.prev = None
        self.marble = i
        self.value = i

    def insert(self,marble):
        marble.left = self
        marble.right = self.right
        self.right.left = marble
        self.right = marble
    
    def remove(self):
        self.left.right = self.right
        self.right.left = self.left



def main():

    MARBLES = 71482
    PLAYERS = 424
    OFFSET = 7  #shift in index

    curr_player = 1
    curr_mIndex = 0

    circle=[]
    scores = [0 for x in range(PLAYERS)]

    circle.insert(0 , 0)


    for i in range(1,MARBLES+1):

        if i%23 != 0:

            if curr_mIndex == len(circle)-2:
                new_mIndex = curr_mIndex+2
                circle.insert( new_mIndex , i)
                curr_mIndex = new_mIndex

            elif curr_mIndex == len(circle)-1:
                new_mIndex = 1
                circle.insert(new_mIndex, i)
                curr_mIndex = 1

            elif curr_mIndex > len(circle)-2:
                new_mIndex = ( (len(circle) % curr_mIndex) if curr_mIndex>0 else 0 ) + 1
                circle.insert( new_mIndex , i)
                curr_mIndex = new_mIndex

            else:
                new_mIndex +=2
                circle.insert(new_mIndex , i)
                curr_mIndex = new_mIndex
        

        else:


            # get index that is 7 counterclockwise from current index

            if curr_mIndex < 7:
                curr_mIndex = len(circle) - (OFFSET - curr_mIndex)
            
            else:
                curr_mIndex = curr_mIndex-7

            scores[curr_player-1] += i

            scores[curr_player-1]+=circle[curr_mIndex]  
            del circle[curr_mIndex]

            new_mIndex = curr_mIndex


        if curr_player == PLAYERS:
            curr_player = 1
        
        else:
            curr_player+=1


    print("Part I:  Max Score:", max(scores), "for player", scores.index(max(scores))+1)
    
    # Part II:  rewritten using doubly linked list:
    #https://www.geeksforgeeks.org/doubly-linked-list/

    PLAYERS = 424
    MARBLES = 7148200
    OFFSET = 7
    scores = [0 for x in range(PLAYERS)]
    curr_marble = curr_marble.left = curr_marble.right = Marble(0)
    curr_player = 1

    for i in range(1,MARBLES+1):

        if i%23 == 0:
            for v in range(OFFSET):
                #move counter 7 spots
                curr_marble = curr_marble.left

            scores[curr_player-1]+=curr_marble.value
            scores[curr_player-1]+=i 

            curr_marble.remove()
            curr_marble = curr_marble.right

        else:

            curr_marble = curr_marble.right
            curr_marble.insert(Marble(i))
            curr_marble = curr_marble.right

            
        if curr_player == PLAYERS:
            curr_player = 1
        
        else:
            curr_player+=1

    print("Part II: Max Score:", max(scores), "for player", scores.index(max(scores))+1)


if __name__ == "__main__":
    main()
