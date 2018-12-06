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

    new_string = ""
    flg = False
    #pstring = "dabAcCaCBAcCcaDA" 

    with open('day05_input.txt','r') as input_file:
        pstring = input_file.read().rstrip('\r\n')
           
    while not flg:
        pstring = compare(pstring)
        #print(pstring)

        # check for condition
        flg = check(pstring, flg)
        #print(flg)

    print(pstring, "length",len(pstring))

if __name__ == "__main__":
    main()
