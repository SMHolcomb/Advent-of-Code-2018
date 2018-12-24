
MARBLES = 7148200
PLAYERS = 424
OFFSET = 7  #shift in index

curr_player = 1
curr_mIndex = 0

circle=[]
scores = [0 for x in range(PLAYERS)]

circle.insert(0 , 0)


# now add 1 between curr_mIndex+1 and curr_mIndex+2 but wrapping around if needed.
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


#print(circle)
#print(scores)
print("Max Score:", max(scores), "for player", scores.index(max(scores))+1)
	


