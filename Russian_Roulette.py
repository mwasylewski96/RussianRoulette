"""Russian Roulette"""
import random
import time
#from playsound import playsound
#playsound("C:\\Users\\mwasy\\OneDrive\\Pulpit\\Rewolwerglos.mp3")

#naboje pełne - full są 3
#naboje puste - empty jest 6
#Program losuje kolejnosc liczb od 0 do 8 w liscie rewolwer i strzela pokolei
def napełnianie_rewolweru_nabojami(rewolwer):
    choicelist = ["full", "empty"]
    fullcounter = 0
    emptycounter = 0
    while len(rewolwer) != 9:
        y = random.choices(choicelist, [30, 70], k=1)
        y = y[0]
        if (y == "full" and fullcounter !=3):
            rewolwer.append(y)
            fullcounter += 1
        if (y == "empty" and emptycounter !=6):
            rewolwer.append(y)
            emptycounter += 1
    return rewolwer
def strzelanie(rewolwer):
    for i in rewolwer:
        time.sleep(4)
        print("STRZEL! - enter")
        a = input()
        time.sleep(1)
        if i == "full":
            print("Oooopsss..........killed!")
        else:
            print("Uffff! Masz szczescie")
def ponowna_gra(turn_on):
    print("Grasz dalej? Wybierz y na tak lub cokolwiek innego na nie")
    choice = input()
    if choice == "y":
        turn_on = True
    else:
        turn_on = False
    return turn_on
choice = "Y"
turn_on = True
while turn_on == True:
    rewolwer = [] #pusty rewolwer
    napełnianie_rewolweru_nabojami(rewolwer)
    strzelanie(rewolwer)
    if ponowna_gra(turn_on) == False:
        break
