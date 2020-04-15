# Function to convert decimal to binary, octal and hexadecimal
# Convert decimal to binary and return a string
def decimal_to_binary(dec):
    decimal = int(dec)
    binary_num = str(bin(decimal))
    # return a string without the useless first characters
    return binary_num[2:] 

# Convert decimal to octal and return a string
def decimal_to_octal(dec):
    decimal = int(dec)
    octal_num = str(oct(decimal))
    # return a string without the useless first characters
    return octal_num[2:]

# Convert decimal to hexadecimal and return a string
def decimal_to_hexadecimal(dec):
    decimal = int(dec)
    hexa_num = str(hex(decimal))
    # return a capitalize string without the useless first characters
    return hexa_num[2:].capitalize()
    

def print_formatted(number):
    
    num = 1
    # Width of number in binary
    width = len(decimal_to_binary(number))
    your_list = []

    # Iterate for each number
    while (num <= number):
        #add numbers
        your_list.append(num)
        your_list.append(decimal_to_octal(num))
        your_list.append(decimal_to_hexadecimal(num))
        your_list.append(decimal_to_binary(num))

        #print
        for element in your_list:
            print(str(element).rjust(width)+" ", end="")

        your_list = []
        num+=1
        print("")

    


if __name__ == '__main__':
	print_formatted(99)
