import random, time, os

players = {}

players["Kobe Bryant"] = {"shooting": 100, "iq": 97, "passing": 85, "clutchness": 100}
players["Lebron James"] = {"shooting": 87, "iq": 99, "passing": 95, "clutchness": 72}
players["Michael Jordan"] = {"shooting": 97, "iq": 91, "passing": 95, "clutchness": 100}
players["Kevin Durant"] = {"shooting": 94, "iq": 83, "passing": 69, "clutchness": 60}

def prettyPrint():
  for key in players.keys():
    print(key)
  print()

computerWins = 0
playerWins = 0
while True:
  print(f"NBA2K Battle                 You:{playerWins}  |  Computer:{computerWins}")
  print("--------------------------------------------------------")
  print()
  print("Players")
  print()
  prettyPrint()

  addPlayer = input("Would you like to add a player? > ").strip().lower()
  print()

  if addPlayer[0] == "y":
    addPlayer = True
    while addPlayer:
      name = input("What's their name? > ").strip().title()
      shooting = int(input("What's their shooting score? > "))
      iq = int(input("What's their IQ score? > "))
      passing = int(input("What's their passing score? > "))
      clutchness = int(input("What their clutchness score? > "))

      players[name] = {"shooting": shooting, "iq": iq, "passing": passing, "clutchness": clutchness}
      askAgain = input("Add more? > ").strip().lower()
      if askAgain[0] == "y":
        addPlayer = True
      else:
        time.sleep(1)
        os.system("clear")
        print(f"NBA2K Battle                 You:{playerWins}  |  Computer:{computerWins}")
        print("--------------------------------------------------------")
        print()
        print("Players")
        print()
        prettyPrint()
        break

      time.sleep(1)
      os.system("clear")
      prettyPrint()
      
    print()

  list = []
  for key,value in players.items():
    list.append(key)

  player = input("Pick your player\n> ").strip().title()
  computer = random.choice(list)
  while True:
    if computer == player:
      random.choice(list)
    else:
      break

  print(f"> Computer has picked {computer}")
  print()
  stat = input("Choose your stat: Shooting, IQ, Passing, Clutchness\n> ").strip().lower()

  print()
  print(f"{player}: {players[player][stat]}")
  print(f"{computer}: {players[computer][stat]}")
  print()

  if players[player][stat] > players[computer][stat]:
    print(f"{player} wins!")
    playerWins += 1
  elif players[player][stat] < players[computer][stat]:
    print(f"{computer} wins!")
    computerWins += 1
  elif players[player][stat] == players[computer][stat]:
    print("That's tie! NO POINTS GIVEN")

  time.sleep(2)
  os.system("clear")
