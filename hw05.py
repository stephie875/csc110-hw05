"""
Name: (Stephanie Noelle Ndiffotsang Neza)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """ This ask the user to input a an uppercase letter, if the user inputs more than one uppercase letter the program asks it to input the write thting and try agai
         and if the User inputs an upper case letter that is not 'A', 'B' or 'C' then it tells the user it provided the wrong character and the question is asked again untill the right answe is found and the value returned"""
    # remove the default return and add your code
    while True:
        letter = input("Give an single uppercase letter: ")
        if not len(letter) == 1: # if the length of the number is not one then it will fufill the print statement bellow
            print("Error: it needs to be a single character.")
            continue # this skps the next step and restarts the loop untill the condition is met
        if not (letter == "A" or letter == "B" or letter == "C"):
            print("Error: You provided the wrong character.")
            continue
        else:
            return letter
        
def get_digit():
    """ this function asks the user to input a single digit character and if the user fails it tells the user the range within which it should give a value
         and if the right value i snot given yet the loops continues untill the user enters a right value """
    # remove the default return and add your code
    while True:
        digit = input("Give an single number character: ")
        if not digit.isdigit(): # this checks if the string that was inputted is a digit
            print("Error: your input should be only digits.")
            continue
        if not (digit == "1" or digit == "2" or digit == "3"):
            print("Error: a single digit needs to be in [1,3].")
            continue
        else:
            return digit
            
     
def check_pattern(letter, digit, st_list):
    """ it receives the letter character, digit character, and the string list called st_list and checks if any word inside the list contains the letter and number in that order and prints them out """
    # remove the default pass and add your code
    print("Strings with the pattern:")
        
    for word in st_list:
        if (letter in word and digit in word and word.lstrip("@").startswith(letter)):
            print(word, end=" ") # this prints the word then skip some spaces before writing the next word, so no new line 
            continue
        
#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]
    

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------

    # Your code Here
    while True:
        letter = get_letter()
        digit = get_digit()
        check_pattern(letter, digit, st_list)
        print() # this skips a line 
    
        user_input = input("Try Again? (y/n): ") # asks the user if he wants to continue the whole process again
        if (user_input == "y"):
           continue
        else:
            break # this stops the loop 

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()