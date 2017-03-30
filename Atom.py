import time
import random
import sys

#Menu
def game():
	print("░░░░░░░░░░░░░░░░░░░░░")
	print("░S░p░a░c░e░ ░W░a░l░k░")
	print("░░░░░░░░░░░░░░░░░░░░░")
	time.sleep(2)
	print()	
	
	ch1 = str(input("Continue [y/n]: "))

	if ch1 in ['y', 'Y', 'Yes', 'YES', 'yes']:
		time.sleep(2)
		print("As the SPC_Falcon09 International Space station orbits the planet Xeno you look down on it, sudently you feel vibrations of the ship rumble. Sector A SPC_Falcon09 was just with an asteroid Mayday, Mayday SPC_Falcon09 was just hit with an asteroid all personel go to emergency pods ,was yelled over the intercoms. The area around you was fill with sudent flashes of light , down below you could see all sectors A, B, C were being destoryed by a storm of asteroids. The vibrations knocked you on your head, only to wake up on a destoryed ship. As you walk out of your pod only to be invited to a void of lonelyness, no matter how high you screamed for help no one will respond. You're alone... ")
		print()
		time.sleep(2)
		print("The more you kept walking you could see all emergency pods in Sector D were already release back down to Earth. you are really alone. A sound of crashing was in head of you it could be a sign of hope or danger there was a SD Security Pistol on the ground pick it up or leave it?")
		print()
		ch2 = str(input("Pick it up  [y/n]:"))
		if ch2 in ['y', 'Y', 'Yes', 'YES', 'yes']:
			print()
			print("You have obtained a pistol!")
			pistol = 1							
			print()
			time.sleep(2)
			print("The closer that you come to the buzzing sound ahead, you could finally know what the sound was coming from it was... a ODW Gang Bandit")
			ch3 = str(input("Fight  [y/n]:"))
			if ch3 in ['y', 'Y', 'Yes', 'YES', 'yes']:
				if pistol == 1:
					print("You have a pistol to fight with!")
					time.sleep(1)
					print("You quickly hit the bandit in the back")
					time.sleep(2)
					yourHealth = 30
					enemyHealth = 30
					yourdmg = random.randrange(1, 15)
					enemydmg = random.randrange(1, 15)
					while True:
						if enemyHealth < 0:
							print()
							print ("You have slain the bandit")
							print()
							print ("After killing the bandit you collect of the bandits gear and you see his personal ship. You suit up and prepare for a space towards the ship in the docking bay 0A. Once you are in ship you contact the nearest space station on the radio in the ship. You setup to be lock in and go towards the space station... You're not alone anymore. ")
							print()
							print ("░You Win")
							print()
							
							ch4 = str(input("Try Again [y/n]: "))
							if ch4 in ['y', 'Y', 'Yes', 'YES', 'yes']:
								print("test end")
							if ch4 in ['n', 'N', 'No', 'NO', 'no']:
								print ("By: Armand R.")
								print()
								time.sleep(2)
								print ("░Game Over")
								quit
						
						elif yourHealth < 0:
							print ("You have been slain by the bandit")
							print ("By: Armand R.")
							print()
							time.sleep(2)
							print ("░Game Over")
							quit
							
						if enemyHealth <= 0:
							break
							
						elif yourHealth <= 0:
							break
							
						else:
							print()
							print("░Menu")
							print()
							print("1  Attack")
							print("2  Defence")
							choice = input("Enter: ")
							choice = int(choice)
							
						if choice == 1:
							print()
							enemyHealth = enemyHealth - yourdmg
							print ("The bandit health is now " ,enemyHealth , "HP" )
							print ("You attacked the bandit for " , yourdmg , "DMG")							
							print()
							yourHealth = yourHealth - yourdmg
							print ("The bandit attacked you for",enemydmg," DMG!")
							print ("Your health is now ", yourHealth, "HP")
							print()
							
						elif choice == 2:
							print()
							yourHealth = yourHealth - enemydmg 
							print("Your health is now", yourHealth, "HP")
							enemyHealth = enemyHealth - yourHealth / 2
							print("Ememy Health is now", enemyHealth , "HP")

					if ch3 in ['n', 'N', 'No', 'NO', 'no']:
						print()
						print("You tried to run away")
						print()
						print("The bandit heard you run away ")
						if pistol == 0:
							print("You have a pistol to fight with!")
							time.sleep(1)
							print("You quickly hit the bandit in the back")
							time.sleep(2)
							yourHealth = 30
							enemyHealth = 30
							yourdmg = random.randrange(1, 12)
							enemydmg = random.randrange(1, 15)
							
							while True:
								if enemyHealth < 0:
									print()
									print ("You have slain the bandit")
									print()
									print ("After killing the bandit you collect of the bandits gear and you see his personal ship. You suit up and prepare for a space towards the ship in the docking bay 0A. Once you are in ship you contact the nearest space station on the radio in the ship. You setup to be lock in and go towards the space station... You're not alone anymore. ")
									print()
									print ("░You Win")
									print()
									
									ch5 = str(input("Try Again [y/n]: "))
									if ch5 in ['y', 'Y', 'Yes', 'YES', 'yes']:
										print("end test")
										
									if ch5 in ['n', 'N', 'No', 'NO', 'no']:
										print ("By: Armand R.")
										print()
										time.sleep(2)
										print ("░Game Over")
										quit
									
								elif yourHealth < 0:
									print ("You have been slain by the bandit")
									print ("By: Armand R.")
									print()
									time.sleep(2)
									print ("░Game Over")
									quit
								
								if enemyHealth<= 0:
									break
									
								elif yourHealth <= 0:
									break
									
								else:
									print()
									print("░Menu")
									print()
									print("1  Attack")
									print("2  Defence")
									choice = input("Enter: ")
									choice = int(choice)
									
								if choice == 1:
									print()
									enemyHealth = enemyHealth - yourdmg
									print ("The bandit health is now " ,enemyHealth , "HP" )
									print ("You attacked the bandit for " , yourdmg , "DMG")							
									print()
									yourHealth = yourHealth - yourdmg
									print ("The bandit attacked you for",enemydmg," DMG!")
									print ("Your health is now ", yourHealth, "HP")
									print()
									
								elif choice == 2:
									print()
									yourHealth = yourHealth - enemydmg 
									print("Your health is now", yourHealth, "HP")
									enemyHealth = enemyHealth - yourHealth / 2
									print("Ememy Health is now")
			
		if ch2 in ['n', 'N', 'No', 'NO', 'no']:
			print()
			print("You did not take the pistol")
			pistol = 0
	
	if ch1 in ['n', 'N', 'No', 'NO', 'no']:
		print()
		print("By: Armand R. ")
		time.sleep(2)
		print("Quiting")
		quit
 
game() 
