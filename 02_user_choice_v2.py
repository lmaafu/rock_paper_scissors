# Version 2 - error message included when calling function


# Function go here
def choice_checker(question):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        if response == "r" or response == "rock":
            return response
        elif response == "p" or response == "paper":
            return response

        elif response == "s" or response == "scissors":
            return response

# check foe exit code
        elif response == "xxx":
            return response
        else:
            print()


# Main routine goes here

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user choice and check it's valid
    user_choice = choice_checker(
        "Choose rock / paper/ scissors "
        " (r/p/s): ","Please choose rock / paper / scissors (or xxx to quit)")
        
    # Print ot choice for comparison purposes
    print("You chose {}".format(user_choice))
