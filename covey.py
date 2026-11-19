


"""
I was inspired to create this program by the Engima Machine.
I've created a encryption program before, but learning about 
the Enigma made me see the flaws of my own system. 

So now i've sought out to correct these flaws and create 
a encyrtption program that cannnot be solved bassed on 
character substitution or guess work alone.

Wish me luck.
    -LWK, 11/09/2026 ; 7:20 PM

"""
##########
"""
Notes:

handle uppercase correctly
"""
##########

# debug variables to control certain printed outputs used in troubleshooting
debug_text = False
cypher_text = False




class globalVars:
    StringInput = "abcdefg" # Get string from user
    rozFactor = 0 # Get RozFactor from user
    hotSwapDegree = 0 # Get Hotswap Degree from user
    includeCharCount = "" # ask if string length should be added to HsD
    censorchar = 0 # get censor charcter digit from user
    
    checked_Indexes = [] # store of checked indexes for cycle 1 & 2 
    
    # prework on input string
    rawString = "" # convert it into a list for better manipulation, making everything lowercase so no casematch issues occur
    if debug_text: print(f"------DEBUG TEXT:: PreString: {rawString}")
    
    charCount = 0 # get count of characters in string, used for the letter hot-swap
    if debug_text: print(f"------DEBUG TEXT:: CharCount: {charCount}")
    

alphabet_Digit = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
    'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
    'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
    10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q',
    18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
}

def first_alphabetical_char(encoded):
    firstChar = encoded[0] # get the first character in the string, this is the one that was hot-swapped
    if firstChar == ' ': # if the first character is a empty space, move along until a legitimate symbol or letter is found.
        index = 1
        while True: # catch for if the first character being a space, if it is it moves the "first character" to the first aphabetical character
            firstChar = encoded[index]
            if firstChar != ' ': break
            else: index += 1
    return firstChar

def cycle_1_2(string_input,roz_Factor,cycle):
    output_String = [] # builds the output string here by appending characters from the working index

    if cycle == 1: cypherIncrement = int(roz_Factor) # checks for which cycle its told to run by "cyle" variable, and changes the cypherIncrement accordingly
    else: cypherIncrement = 1
    
    current_Index = 0 # where it keeps track of it's working index
    
    for item in string_input: # loops through the string based on direct length instead of a 'while True' loop like ROZLAND
        if current_Index in globalVars.checked_Indexes: # checks if the working index has been used already in making the output string
            if cypher_text: print(f"--index '{current_Index}' already used, skipping") # skips it if so
        else:
            if current_Index > globalVars.charCount-1: # if not, it checks that the working index is within range of the string
                if cypher_text: print("--Current Index out of range, Shifter cyper to phase 2") # if not in range, it breaks out and ends the cycle
                break
            else: # if it's not used already and in range:
                globalVars.checked_Indexes.append(current_Index) # add working index to list of checked indexes
                output_String.append(globalVars.rawString[current_Index]) # append the working index to the end of the output string
        current_Index += cypherIncrement # move the working index by the cypherInrement, RozFactor for cycle 1, '1' for cycle 2
    if cycle == 1: # if it's cycle 1, the function returns the output string AND the length-1 which is the 'decodekey' used in decryption
        return (output_String,len(output_String)-1)
    return output_String # if cycle 2, just return the output string

def hotSwap(string_input,hotSwapDegree,includeCharCount):
    result = []
    firstChar = first_alphabetical_char(globalVars.rawString)
    
    letterDigit = alphabet_Digit.get(firstChar) # gets the number that corrisponds to the first character
    if debug_text: print(f"------DEBUG TEXT:: FirstLetter: {letterDigit}:{alphabet_Digit.get(letterDigit)}")
    
    if includeCharCount == "y": newletterDigit = letterDigit + globalVars.charCount + hotSwapDegree # uses the first letter digit and adds the character count AND HsD to shift the letter
    elif includeCharCount != "y": newletterDigit = letterDigit + hotSwapDegree # uses the first letter digit and adds the HsD count to shift the letter
    
    while newletterDigit > 26: # if the ending int is > 26, take away 26 until it falls into range, aka wrap to the beginning of the alphabet
        newletterDigit -= 26
    if debug_text: print(f"------DEBUG TEXT:: New Letter:  {newletterDigit}:{alphabet_Digit.get(newletterDigit)}")
    
    shiftedLetter = alphabet_Digit.get(newletterDigit) # convert this new digit number into an actual letter to be hot-swapped into the final output
    
    for char in string_input: # this runs through the input string and swaps the two characters
        if char == firstChar: result.append(shiftedLetter) # swap first character occurances for shifted letter
        elif char == shiftedLetter: result.append(firstChar) # swap shifter letter occurances for first character
        else: result.append(char)
    
    HsD = newletterDigit-letterDigit # wrap the Hotswap Degree around to be a positive number
    while HsD < 0:
        HsD += 26
    
    return (result,HsD)

def censorChar(string_input,input_censor_char_digit):
    result = []
    
    while input_censor_char_digit > globalVars.charCount:
        input_censor_char_digit -= globalVars.charCount
    
    censor_char = string_input[input_censor_char_digit]
    censor_char_digit = alphabet_Digit.get(censor_char)
    
    if censor_char_digit == None: 
        censor_char = string_input[input_censor_char_digit +1]
        censor_char_digit = alphabet_Digit.get(censor_char)
        
    if debug_text: print(f"------DEBUG TEXT:: CensorChar: {censor_char}:{censor_char_digit}")
    
    for char in string_input:
        if char == censor_char:
            result.append("^")
        else: result.append(char)
    
    return (result,censor_char_digit)

def main(web_input):
    
    
    globalVars.rozFactor = 4
    globalVars.hotSwapDegree = 5
    globalVars.includeCharCount = "y"
    globalVars.censorchar = 2
    globalVars.StringInput = web_input
    
    globalVars.rawString = list(web_input.lower())
    rawString = list(web_input.lower())
    globalVars.charCount = len(rawString)
    
    endString = [] # the list where the output is built
    
    
    
    (cycle1String,decodekey) = cycle_1_2(globalVars.rawString,globalVars.rozFactor,1)
    if debug_text: print(f"------DEBUG TEXT: Cycle1 String: {cycle1String}")
    for item in cycle1String:
        endString.append(item)
    
    
    cycle2String = cycle_1_2(globalVars.rawString,globalVars.rozFactor,2)
    if debug_text: print(f"------DEBUG TEXT: Cycle2 String: {cycle2String}")
    for item in cycle2String:
        endString.append(item)
        
    
    (endString,HsD) = hotSwap(endString,globalVars.hotSwapDegree,globalVars.includeCharCount)
    
    (endString, cc) = censorChar(endString,globalVars.censorchar)

    # print(f"OUTPUT:>{''.join(endString)}<")
    # print(f"ID: {decodekey}.{globalVars.rozFactor}.{HsD}.{cc}")
    output = ''.join(endString)
    stringID = f"{decodekey}.{globalVars.rozFactor}.{HsD}.{cc}"
    
    return (output,stringID)
            
    
