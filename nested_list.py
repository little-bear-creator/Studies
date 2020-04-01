# Given the names and grades for each student in a Physics class of  students, 
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# hackerrank.com
if __name__ == '__main__':

    worst = second = 100
    result_names = []
    worst_names = []

    #Loop though all the element
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        
        # If the current element is smaller than worst, then update worst and second. 
        if (score <= worst):
            if (score == worst):
                worst_names.append(name)
            else:
                result_names = []
                result_names.extend(worst_names)
                worst_names = []
                worst_names.append(name)
                # assign new values
                second = worst
                worst = score
            
        # Else if the current element is smaller than second then update second
        elif (score <= second):
            if (score == second):
                result_names.append(name)
            else:
                second = score
                result_names = []
                result_names.append(name)
        
       

    #sorted()
    x = sorted(result_names)
    for item in x:
        print(item)
