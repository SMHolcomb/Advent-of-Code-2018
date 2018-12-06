"""
************************************************************************************************
PART I:
As you search the closet for anything that might help, you discover that you're not the first person to want to sneak in. Covering the walls, someone has spent an hour starting every midnight for the past few months secretly observing this guard post! They've been writing down the ID of the one guard on duty that night - the Elves seem to have decided that one guard was enough for the overnight shift - as well as when they fall asleep or wake up while at their post (your puzzle input).

[ see test input]

Timestamps are written using year-month-day hour:minute format. The guard falling asleep or waking up is always the one whose shift most recently started. Because all asleep/awake times are during the midnight hour (00:00 - 00:59), only the minute portion (00 - 59) is relevant for those events.

Visually, these records show that the guards are asleep at these times:

Date   ID   Minute
            000000000011111111112222222222333333333344444444445555555555
            012345678901234567890123456789012345678901234567890123456789
11-01  #10  .....####################.....#########################.....
11-02  #99  ........................................##########..........
11-03  #10  ........................#####...............................
11-04  #99  ....................................##########..............
11-05  #99  .............................................##########.....

The columns are Date, which shows the month-day portion of the relevant day; ID, which shows the guard on duty that day; and Minute, which shows the minutes during which the guard was asleep within the midnight hour. (The Minute column's header shows the minute's ten's digit in the first row and the one's digit in the second row.) Awake is shown as ., and asleep is shown as #.

Note that guards count as asleep on the minute they fall asleep, and they count as awake on the minute they wake up. For example, because Guard #10 wakes up at 00:25 on 1518-11-01, minute 25 is marked as awake.

If you can figure out the guard most likely to be asleep at a specific time, you might be able to trick that guard into working tonight so you can have the best chance of sneaking in. You have two strategies for choosing the best guard/minute combination.

Strategy 1: Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?

In the example above, Guard #10 spent the most minutes asleep, a total of 50 minutes (20+25+5), while Guard #99 only slept for a total of 30 minutes (10+10+10). Guard #10 was asleep most during minute 24 (on two days, whereas any other minute the guard was asleep was only seen on one day).

While this example listed the entries in chronological order, your entries are in the order you found them. You'll need to organize them before they can be analyzed.

What is the ID of the guard you chose multiplied by the minute you chose? (In the above example, the answer would be 10 * 24 = 240.)

--- Part Two ---
Strategy 2: Of all guards, which guard is most frequently asleep on the same minute?

In the example above, Guard #99 spent minute 45 asleep more than any other guard or minute - three times in total. (In all other cases, any guard spent any minute asleep at most twice.)

What is the ID of the guard you chose multiplied by the minute you chose? (In the above example, the answer would be 99 * 45 = 4455.)

************************************************************************************************

Completed: 12/4/18

************************************************************************************************
"""
def init_matrix(times):

	times = [[0 for i in range(61)] for j in range(1000)]
	return times

def print_log(log):
	for entry in log:
		print(entry)
	return

def sortkey(log,index):
	return log[index]

def main():
	
	log = []
	times = []
	guard_id = 0
	start_min = 0
	end_min = 0
	date_id = '9999-99-99'
	line_index = -1
	# import data and sort chronologically

	
	with open('day04_input.txt','r') as input_file:
	#with open('day04_testinput.txt','r') as input_file:
		for entry in input_file:
			entry = entry.rstrip('\r\n')
			entry = entry.replace('[','')
			entry = entry.replace(']','')
			entry = entry.replace('#','')
			entry = entry.split(" ", 2) 

			log.append(entry)
	#print_log(log)

	log = sorted(log,key=lambda x: (x[0], x[1]))

	# set up times matrix
	times = init_matrix(times)
	

	# parse log entries
	for line in log:

		if (line[2][0:5] == 'Guard'):
			line_index +=1

			date_id = line[0]
			times[line_index][0] = date_id

			guard_id = line[2].split(' ',2)[1]
			times[line_index][1] = guard_id


		if (line[2][0:5] != 'Guard'):	


			if(line[2][0:5] == 'falls'):
				start_min = int(line[1][3:5])


			if(line[2][0:5] == 'wakes'):
				end_min = int(line[1][3:5])


				for i in range(start_min, end_min):
					times[line_index][i+1] = 1

	

	# remove blank rows
	times = [time for time in times if time[0] != 0]

	# PART I

	#group and sum by guard
	guards = {}
	for time in times:
		#print(time[1])
		if time[1] not in guards:
			sum = 0
			for value in time[2:]:
				sum = sum + value
			guards[time[1]] = sum
		else:
			#In the case that the guard is already in guards, add the new sum
			sum = 0
			for value in time[2:]:
				sum = sum + value
			guards[time[1]] +=sum
	
	
	# get guard with the most minutes
	inverse = [(value, key) for key, value in guards.items()]
	
	
	#for that guard, get minute they were asleep the most
	minutes = [time for time in times if time[1] == max(inverse)[1]]

	

	# sum the columns for all rows
	# take the long way around
	temp=[]
	for j in range(2,len(minutes[0])):
		sum = 0
		
		for i in range(0,len(minutes)):
			sum += minutes[i][j]
		temp.append(sum)



	# get row of max minute
	max_total = 0
	max_minute = 0
	count = -1

	for minute in temp:
		count+=1
		#print(minute)
		if minute > max_total:
			max_total = minute
			max_minute = count

	print("Guard:",int(max(inverse)[1]) , " minute: " , (max_minute+1) )
	print("Answer:", int(max(inverse)[1]) * (max_minute+1))
	# find the index with max value

	# PART II
	guards = {}
	for time in times:
		#print(time[1])
		if time[1] not in guards:  #guard doesn't exist yet
			#subset guard records and sum all columns
			minutes = [item for item in times if item[1] == time[1]]
			guards[time[1]] = []

			#loop through and sum columns
			temp = []
			for j in range(2,len(minutes[0])):
				sum = 0
				for i in range(0,len(minutes)):
					sum += minutes[i][j]
				temp.append(sum)
				#print(sum)
			guards[time[1]] = temp

	# now go through guards dictionary and find max minutes

	max_total_minutes = 0
	max_guard = 0

	for guard in guards:
		count = 0
		for minute in guards[guard]:
			count +=1
			#print("count:" , count , "max_total_minutes so far:", max_total_minutes, "minutes:", minute, )
			if minute > max_total_minutes:
				max_total_minutes = minute
				max_count= count 
				max_guard = guard

	print("Guard:", max_guard, "Max minutes:", max_total_minutes, "Minute #:" , max_count)
	print("Answer: " , (int(max_guard) * max_count))



if __name__ == '__main__':
	main()
