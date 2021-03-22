# Function used to check input is valid

def check_rounds():
  while True: 
    response = input("How many rounds: ")

    rounds_error = "Please type either <enter>or an intege that is more than 0"
    if response != "":
      try:
        response = int(response)

        if response <1:
          print(rounds_error)
          continue 

      except ValueError:
          print(rounds_error)
          continue




# Main routine goes here .....


rounds_played = 0
choose_instructions = "Please choose rock (r), paper (p) or scissors(s)"

# Ask user for # of rounds, <enter> for infiniye mode 
rounds = check_rounds()


end_game = "no"
while end_game == "no":

  # Start of game 

 # Rounds Heading 
  print()
  if rounds == "":
    heading = "Continuous Mode: Round {}".format(rounds_played)
    print(heading)
    choose = input ("{} or'xxx' to end: ".format(choose_instructions))

    if choose == "xxx":
      break

  else:
    heading = "Round {} of {}".format(rounds_played + 1, rounds)
    print(heading)
    choose = input("{} or 'xxx'to end:".format(choose_instructions))

    # rest of loop / game
print("You chose {}".format(choose))

rounds_played += 1

print("Thank you for playing")

