

"""

"""
# debug variable to control printed outputs used in troubleshooting 
degbugText = False


alphabet_Digit = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
    'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
    'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
    10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q',
    18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
}
#<------------------------------------------------------------------------------>
def first_alphabetical_char(input_string):
    firstChar = input_string[0] # get the first character in the string, this is the one that was hot-swapped
    if firstChar == ' ': # if the first character is a empty space, move along until a english letter is found.
        index = 1
        while True: # catch for if the first character being a space, if it is it moves the "first character" to the first aphabetical character
            firstChar = input_string[index]
            if firstChar != ' ': break
            else: index += 1
    return firstChar

def reverse_hot_swap(input_string, hotSwapDegree):
    result = []
    encodedFirstChar = first_alphabetical_char(input_string) # get first alphabetical char
    encodedFirstDigit = alphabet_Digit.get(encodedFirstChar.lower()) # Get that characters corrisponding digit
    decodedFirstDigit = encodedFirstDigit - int(hotSwapDegree) # Shift it back with the HsD 
    while decodedFirstDigit < 0: # make sure its not negative and within range of the alphabet
        decodedFirstDigit += 26
    decodedFirstChar = alphabet_Digit.get(decodedFirstDigit) # turn it back into a letter
    if degbugText: print(f"DEBUG TEXT:: RevHS, {encodedFirstChar}:{encodedFirstDigit} -> {decodedFirstChar}:{decodedFirstDigit}")
    
    for index in input_string: # cyles through the encoded string's index and replaces the hot-swapped character with original
        if index.lower() == encodedFirstChar: result.append(decodedFirstChar)
        elif index.lower() == decodedFirstChar: result.append(encodedFirstChar)
        else: result.append(index)
    
    return result # return de-shifted letter

def reverse_censor_char(input_string, censor_char_digit):
    result = []
    censored_char = alphabet_Digit.get(censor_char_digit) # exchanges the 'censor_char_digit' for an aplhabetical character
    for char in input_string: # for every character in the 'input_string' if the character is "^" AKA the censor symbol, swap it back to the 'censored_char'
        if char.lower() == "^":
            result.append(censored_char)
        else: result.append(char)
    return result # return uncensored result list

def main():
    #<-----------------------------------User Input------------------------------------------->
    encodedStringInput = "" # get input from user
    
    encodedList = list(encodedStringInput) # convert user string to list of characters
    
    inputID = "" # get string info from user like "15.3.54.26" 
    inputID = inputID.split(".") # and break it into a list and extract info from the indexes
    
    decodeKey = int(inputID[0]) # decode key from COVEY
    rozFactor = int(inputID[1]) # roz factor from COVEY
    hotSwapDegree = int(inputID[2]) # Hot-swap degree from COVEY
    censorchar = int(inputID[3]) # Censored Char Digit from COVEY

    
    outputbuild = [] # where the output is built
    
    #<------------------------------------Censor Reversal------------------------------------------>
    
    uncensored_list = reverse_censor_char(encodedList,censorchar) # created a version of the string with the censor undone
    
    #<------------------------------------Hot Swap Reversal------------------------------------------>
    
    reverse_hot_swap_list = reverse_hot_swap(uncensored_list,hotSwapDegree) # creates a version of the string with the FirstCharacter Hot-Swap undone
    
    #<------------------------------placeholder space creation------------------------------------------>
    
    for char in reverse_hot_swap_list:  # this puts in a '$' for each character in the OG string
        outputbuild.append('$')    
    outputbuild[0] = reverse_hot_swap_list[0] # places the first character
    
    #<--------------------------------Cycle 1 Character Placement-------------------------------------------->
    
    for num in range(decodeKey): # loops for every cycle 1 character AKA the decodekey
        indexPosition = num + 1 # makes the position it'll start looking at the encoded string at [1] to account for the first character constant
        outIndex = indexPosition*rozFactor # gets the position of the current character to be placed based on the current position in the encoded string * the rozKey, or cycle 1 step degree
        outputbuild[outIndex] = reverse_hot_swap_list[indexPosition] # take the character from the encoded string and places it in the correct spot in the decoded output
        
    #<--------------------------------Cycle 2 Character Placement-------------------------------------------->
    
    remainders = reverse_hot_swap_list # makes a copy of the encoded list, after the censor and Hs have been undone, named 'remainders'
    for val in range(decodeKey+1): # this removes all the cycle 1 characters, +the first character, leaving the remainders list all cycle 2 characters
        remainders.pop(0)
    if degbugText: print(f"--DEBUG TEXT :: remainders:\n{remainders}\n-----")
    
    position = 0 # current position of the for loop in the output list 
    usedbank = 0 # current position of the for loop in the remainders list
    for item in outputbuild: # takes the remainders list and replaces the blank '-' spaces in the outputbuild with the cycle 2 characters in order
        if item == '$':
            outputbuild[position] = remainders[usedbank]
            usedbank +=1
        position += 1
    
    #<--------------------------------Output Handling------------------------------------------------------>
    
    if degbugText: print(f"DEBUG TEXT:: outputbuild list:\n{outputbuild}\n-----")
    # print(f"OUT: >{''.join(outputbuild)}<")



main()
