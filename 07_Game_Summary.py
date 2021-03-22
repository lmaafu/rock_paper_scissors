game_summary = []

rounds_lost = 0
rounds_drawn = 0
rounds_played = 5

for item in range(0, 5):
  results = input("choose results: ")

  outcome = "Round {}: {}".format(item, results)

  if results == "lost":
    rounds_lost += 1
    elif results == "tie":
      rounds-drawn += 1

      game_summary.append(outcome)

rounds_won = rounds_played - rounds_lost - rounds_drawn