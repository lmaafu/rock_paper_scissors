import random

# Function go here

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes/no")
            print()

def instructions():
    statement_generator("How To Play", "*")
    print()
    print("Pick an integer that is more than 0")
    print()
    print("Then for each round, choose from rock / paper/ scissors (or xxx to quit)")
    print("You can type r / p / s / xxx if you don't want to type the entire word.")
    print()
    print("The rules are...")
    print("- Rock beats scissors")
    print("- Scissors beats paper")
    print("- Paper beats rock ")
    print()
    print("**** HAVE FUN ****")
    return""


def check_rounds():
  while True: 
    print()
    response = input("How many rounds?: ")

    rounds_error = "Please type either <enter> or an integer that is more than 0"
    if response != "":
      try:
        response = int(response)

        if response <1:
          print(rounds_error)
          continue 

        else:
          return response

      except ValueError:
        print(rounds_error)
        continue

      return response 




def choice_checker(question, valid_list, error):
  
  # Ask user for choice (and put choice in lower case)
  response = input(question).lower()

  # iterstes through list and if resonse is an item
  # in the list (or the first leter of an item), the 
  # full item name is returned

  for item in valid_list:
      if response == item[0] or response == item:
          return item

  # output error if item not in list 
  print(error)
  print()
  


# Main routine goes here 
played_before = yes_no("Have you played the game before? ")

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

if played_before == "no":
    instructions()


# Lists of valid responses 
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before 
# If 'yes', show instructions

#  ask user form the # of rounds then loop......
rounds_played = 0

# intialise lost / drawn counters
rounds_lost = 0 
rounds_drawn = 0


# Ask user for no of rounds, <enter> for infiniye mode

rounds = check_rounds()

end_game = "no"
while end_game == "no":

  # Start of Game Play Loop 

  # Rounds Heading 
  print()
  if rounds == "":
    heading = "Continuous Mode: Round {}".format(rounds_played +1)

  else:
    heading = "Round {} of {}".format(rounds_played + 1,  rounds)

  print(heading)




  # Ask user for choice and check it's valid 

  # get computer choice_checker
  comp_choice = random.choice(rps_list[:-1])   
  print("Comp choice", comp_choice)

  choose = choice_checker("Choose rock / paper / scissors (r/p/s):", rps_list, "Please choose from rock / paper / scissors (or xxx to quit)")

  # End game if exit code is typed 
  if choose == "xxx":
        break 

  # compare choice
  if comp_choice == choose:
      result = "tie"
      rounds_drawn += 1
  elif choose == "rock" and comp_choice == "scissors":
    result = "won"
  elif choose == "paper" and comp_choice == "rock":
    result = "won"
  elif choose == "scissors" and comp_choice == "paper":
    result = "won"
  else:
    result = "lost"
    rounds_lost +=1

  if result == "tie":
    feedback = "It's a tie"
  else:
    feedback ="{} vs {} - you {}".format(choose, comp_choice, result)

    # Output results....
    print(feedback)


    rounds_played += 1

  # end game if requested # of rounds has been played 


    

# Ask user if they want to see their game history.
# If 'yes' show game history 

# Show game statitics
rounds_won = rounds_played - rounds_lost - rounds_drawn

# End of Game Statements 
print()
print('***** End Game Summary *****')
print("Won: {} \t|\t Lost {} \t|\t Draw {}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thank you for playing")
