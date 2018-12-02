"""
************************************************************************************************

Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you could cause if you were 
discovered - and use your fancy wrist device to quickly scan every box and produce a list of the likely 
candidates (your puzzle input).

To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number 
that have an ID containing exactly two of any letter and then separately counting those with exactly 
three of any letter. You can multiply those two counts together to get a rudimentary checksum and 
compare it to what your device predicts.

For example, if you see the following box IDs:

abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.
Of these box IDs, four of them contain a letter which appears exactly twice, and three of them 
contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?


--- Part Two ---
Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position 
in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). 
However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is 
found by removing the differing character from either ID, producing fgij.)

************************************************************************************************

Completed: 12/2/18

************************************************************************************************
"""
 

def calc_frequency(boxid):

	frequency = {}
	count2 = 0
	count3 = 0
	final_count = 0

	for letter in boxid:
		frequency[letter] = frequency.get(letter,0)+1

	for k,v in frequency.items():

		if v == 2:
			count2 += 1
			
		if v == 3:
			count3 += 1 

	return count2,count3
	
def calc_match(boxes):

	for boxid in range(0,len(boxes)-1):

			count = 0	
			for boxid2 in range(boxid+1,len(boxes)):
				count = 0

				for i in range(0,len(boxes[boxid])):

					if boxes[boxid][i] != boxes[boxid2][i]:
						count +=1 

				if count == 1:
					return boxes[boxid], boxes[boxid2]

def calc_differences(boxid1,boxid2):
	
	common = []

	for letter in range(0,len(boxid1)):
		if boxid1[letter] == boxid2[letter]:
			common.append(boxid1[letter])
	return common



def main():

	
	# PART I 
	frequency = {}
	count2 = 0
	count3 = 0

	with open('day02_input.txt','r') as input_file:
		for boxid in input_file:
			
			boxid = boxid.rstrip('\r\n')
			temp2, temp3 = calc_frequency(boxid)
			
			if temp2 > 0:
				count2+=1
			if temp3 > 0:
				count3+=1
				
	print("count 2: ", count2)
	print("count 3: ", count3)
	print("checksum: ", count2 * count3, "\n")
	

	# PART I

	boxes = []
	with open('day02_input.txt','r') as input_file:
		for boxid in input_file:
			boxid = boxid.rstrip('\r\n')

			boxes.append(boxid)

		boxid1, boxid2 = calc_match(boxes)		

		common = calc_differences(boxid1,boxid2)
		print(''.join(common),"\n")					


if __name__ == '__main__':
	main()
