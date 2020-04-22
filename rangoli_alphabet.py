# This code prints a rangol alphabet given a integer. For example with argument 5 :
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

def print_rangoli(size):
    # your code goes here
    # the alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # List of string to store the second part of lines after the middle one
    doubleList = []
    # Max size of each line
    maxSize = size*4 - 3
    # Variable defining the basic line
    line = ["-"] * maxSize
    # Copy of line for futur initialisation
    copy = line
    # middle of each line
    middle = int(maxSize/2)
    # variable to increase or decrease for each line printed
    n = 1
    lineNumber = 1

    # While to print each line until the midle one
    while(lineNumber<=size):
        # get the middle letter for the line
        letter = alphabet[size-lineNumber]
        # add middle letter
        line[middle] = letter

        # Add letters to line
        while(n<lineNumber):
            it = lineNumber
            # get next letter
            letter = alphabet[size-(it-n)]

            line[int(middle-(n*2))] = letter
            line[int(middle+(n*2))] = letter

            # Changing letters
            n+=1

        # Empty string
        word = ""

        # Print line
        for item in line:
            print(item, end="")
            word+=str(item)
        print("")

        # Adding line to list for futur print
        doubleList.append(word)

        # Empty line with "-" characters
        line = copy

        n = 1
        lineNumber+=1

    # Second printing
    # Deletes middle line of the drawing
    doubleList.pop(size-1)
    # Reverse list for printing
    doubleList.reverse()
    for item in doubleList:
        print(item)



if __name__ == '__main__':
	n = int(input())
    	print_rangoli(n)

#########################################################################
# Second solution more efficient, based on discussion on hackerRank.com
import string

def print_rangoli(size):
# ascii_lowercase is all alphabet letters 
   alpha = string.ascii_lowercase

    n = size
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
