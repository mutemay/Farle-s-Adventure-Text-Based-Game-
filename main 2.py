print('''
                           ___
                          ( ((
                           ) ))
  .::.                    / /(
 'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
(J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
 `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
  `::'                    \ \(
                           ) ))
                          (_((

''')
print("Welcome to Farle's Adventure.")
print("On one fateful day, the iconic warrior Farles was exploring a dungeon for loot in Realm 23.") 
print("Your Mission: Help Farles escape alive.")
input("Press enter to continue.")
print("Farles hobbled along the dungeon until he came across two of his favorite weapons --- the sword & the vacuum.")
input("Press enter to continue")
weapon = input("Select your weapon. Type S to select the sword, and V to select the vacuum. \n")
weapon = weapon.upper()
if weapon == "S" :
  print('A wild Yanno has appeared... and it appears to be pinching pennies...')
  print("Farles slices at the Yanno creature making it swifty scuffle back to it's mancave.")
elif weapon != "S" :
  print('A wild Yanno has appeared... and it appears to be pinching pennies...')
  print("THE VACUUM HAS BROKEN! The wild Yanno creature proceeds to massacre our unlucky hero :( ")
  print("GAME OVER!")
  raise SystemExit
input("Press enter to continue Farles journey")
print("A wild Newp has appeared! Newp is shooting cigarette smoke projectiles at Farles and emphatically threatening to call the Adventurer's Guild on Farles.")
print("Farles is at a forked pathway. Farles can escape left and swim through an underwater cave or he can fight the nefarious Newp on dry land.")
path = input("Choose your path. Type L to escape through the underwater cave or type R to fight the nefarious Newp. \n")
path = path.upper()
if path == "L" :
  print("Farles valiently swims through the cave, holding his breath for approximately two minutes...")
else :
  print("*Newp comes out firing his cigarette projectiles* \nFarles swings his mighty blade at Newp, but Newp dodges it and uppercuts Farles! \nFarles then is on the ground screaming in agony 'HELP ME PLEASE SOMEBODY HELP ME!' \nFarles has died... :( ")
  print("GAME OVER!")
  raise SystemExit
input("Press enter to continue Farle's journey.")
print("*Farles descends to one of the deepest tunnels in the cave* \nAs Farles was strolling through the tunnel, he spotted a Giant approximately 15 meters away.")
input("Press enter to continue Farle's journey.")
print("Farles has 3 options, he can attempt to befriend the Giant, bribe him, or flee.")
choice = input("Type B to attempt to befriend the giant, R to attempt to bribe him, or F to flee.")
choice = choice.upper()
if choice == "B" :
  print("The Giant wasn't too friendly, the Giant bites Farles ankle. \nFarles gets infected and dies... :(")
  print("GAME OVER!")
  raise SystemExit
elif choice == "F" :
    print("The Giant was far faster than Farles expected. The Giant hawked Farles down and threw a vicious right hook at him. \nFarles died a pitiful, shameful death.\nIt was nearly instantly... :(")
    print("GAME OVER!")
    raise SystemExit
else :
  print("*Farles throws a toy at the Giant* \nThe Giant has been successfully subdued.")
input("Press enter to continue Farle's journey.")
print("After finessing the giant, Farles continues walking for approximately two hours until he approachs a closed door.")
input("Press enter to kick down door.")
print("The room is adorned with gold and valuable jewels! \nFarles will be set for life!")
input("Press enter to continue")
print("CONGRATS! You have won the game!")
raise SystemExit