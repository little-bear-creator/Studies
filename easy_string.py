# Answer of easy string challenge on HackerRank.com just to remenber some tips
# To replace a character in a string you can't do string[5] = "a"
# Below we can see anoter way to do it :
string = string[:position]+character+string[position+1:]

# Below is the code to count how many times a substring is in string :
import string
def count_substring(string, sub_string):
    result = 0
    id = 0
    while(id < len(string) and (id !=-1)):
        n = string.find(sub_string, id, len(string))
        if(n != -1):
            result+=1
            id = n+1
        else:
            id = -1
            
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# Code that reminds usefull boolean method to test string
if __name__ == '__main__':
    s = input()

    #Create a list of string ("False") for result and tests
    result = ["False"] * 5

    # read every char of the string to find out
    for n in range(len(s)):
        # First test : if all value of result are true, stop the loop
        if (result.count("True") == 5):
            break

        # alphanumeric char
        if(s[n].isalnum()):
            result[0] = "True"

            # alphabetical char
            if(s[n].isalpha()):
                result[1] = "True"
                # lowercase char
                if (s[n].islower()):
                    result[3] = "True"
                # upper case char
                else:
                    result[4] = "True"

            # is a digit (0-9)
            elif(s[n].isdigit()):
                result[2] = "True"
            

    # Loop of output print
    for item in result:
        print(item)
