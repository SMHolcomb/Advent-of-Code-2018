
"""
************************************************************************************************

-- Part One --
While the very latest in 1518 alchemical technology might have solved their problem eventually, you can do better. You scan the chemical composition of the suit's material and discover that it is formed by extremely long polymers (one of which is available as your puzzle input).

The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of the same type and opposite polarity are destroyed. Units' types are represented by letters; units' polarity is represented by capitalization. For instance, r and R are units with the same type but opposite polarity, whereas r and s are entirely different types and do not react.

For example:

In aA, a and A react, leaving nothing behind.
In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
In abAB, no two adjacent units are of the same type, and so nothing happens.
In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.

How many units remain after fully reacting the polymer you scanned?

--- Part Two ---
Time to improve the polymer.

One of the unit types is causing problems; it's preventing the polymer from collapsing as much as it should. Your goal is to figure out which unit type is causing the most problems, remove all instances of it (regardless of polarity), fully react the remaining polymer, and measure its length.

For example, again using the polymer dabAcCaCBAcCcaDA from above:

Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer produces dbCBcD, which has length 6.
Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer produces daCAcaDA, which has length 8.
Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer produces daDA, which has length 4.
Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer produces abCBAc, which has length 6.
In this example, removing all C/c units was best, producing the answer 4.

What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?


************************************************************************************************

Completed: Part 1: 12/5/18   , Part 2: 12/6/18

************************************************************************************************
"""




def compare(pstring):
    new_string = ""
    i = 0
    #for i in range(len(pstring)-1):
    while i < len(pstring)-1:
    
        # if ctr == (len(msg) - 1):
        #     msg += msg[ctr]
        #     return msg
        #print("comparing", pstring[i], "and", pstring[i+1], "index is", i)
        if pstring[i] != pstring[i+1].swapcase():
            # then we're ok
            new_string = new_string + pstring[i]
            i +=1
        else:
            #if pstring[i] == pstring[i+1].swapcase():
            i+=2

        #print(new_string)
    
    # add on the last character
    if i < len(pstring):
        new_string = new_string+pstring[len(pstring)-1]    
    #print("i at end:",i)
    return new_string

def check(new_string,flg):
    
    flg = True
    for i in range(0,len(new_string)-1):
        if new_string[i] == new_string[i+1].swapcase():
            # then we're not done
            flg = False
    
    return flg    

def main():
    
    # PART I:

    new_string = ""
    flg = False
    #pstring = "dabAcCaCBAcCcaDA" 

    with open('day05_input.txt','r') as input_file:
    #with open('day05_testinput.txt','r') as input_file:
        pstring = input_file.read().rstrip('\r\n')
           
    while not flg:
        pstring = compare(pstring)
        #print(pstring)

        # check for condition
        flg = check(pstring, flg)
        #print(flg)

    #print(pstring, "length",len(pstring))
    print("length of polymer:", len(pstring))
    
    

    # PART II:

    temp = ""
    flg = False

    with open('day05_input.txt','r') as input_file:
    #with open('day05_testinput.txt','r') as input_file:
        pstring = input_file.read().rstrip('\r\n')

    min_length = len(pstring)

    for letter in range(ord('a'), ord('z') + 1):
        #print(chr(letter))
        flg = False
        temp = pstring[:]

        temp = temp.replace(chr(letter),'')
        temp = temp.replace(chr(letter).swapcase(), '')

        while not flg:
            temp = compare(temp)
            flg = check(temp, flg)
            tlength = len(temp)
            min_length = min(tlength, min_length)
        
 
    print("Length of shortest polymer:", min_length)


if __name__ == "__main__":
    main()
