"""
This module asks for the package requirements
"""


def size()->list:
    """DD...Asks for the size of the package"""
    size = []
    size.append(int(input("Enter the wide of the package in centimeters: ")))
    size.append(int(input("Enter the lenght of the package in centimeters: ")))
    size.append(int(input("Enter the high of the package in centimeters: ")))
    size.sort(reverse = True)
    return size



def provider()->list:
    """DD...Asks for possible providers"""
    chosen_provider = []
    possible_provider = ("dhl", "hermes", "ups", "dps", "gls")

    #Gibt mögliche Anbieter aus
    print("\nYou can choose from following providers:")
    for number, name in enumerate(possible_provider):
        print("* ", name)
        
        
    #Fragt gewünschte Anbieter ab
    while True:
        eingabe = input("Enter the providers which you want to be considerated and quit with 'quit':")
        # Abfrage beenden
        if eingabe == "quit":
            if chosen_provider == []:
                print("\n!!!You have to chose at least one provider!!!\n")
            else:
                break
            
        # Kontrolle ob Eingabe sich unter möglichen Antworten befindet
        elif eingabe in possible_provider:
            
            # Verhindern von doppelter Eingabe
            if eingabe not in chosen_provider:
                chosen_provider.append(eingabe)
            else:
                print("!!!You have already chosen this provider!!!")
        
        # Falsche Eingabe
        else:
            print("invalid input")
    
    #Anzeige ausgewählter Anbieter
    print("\nYou chose following provider: ")
    for number, name in enumerate(chosen_provider):
        print("* ", name)
    print("\n")
    
    #Rückgabe
    return chosen_provider


def max_time()->int:
    """DD...Asks for max delivery time"""
    return int(input("In how many days should your package be delivered?: "))

def mass()->float:
    """DD...Asks for value of the packet"""
    return float(input("Enter the wight of the package in kilogram: "))

def value()->float:
    """DD...Asks for the value of the packet"""
    return float(input("Enter the value of the package in euros: "))

def insurance()->bool:
    """DD...Asks whether a insurance is wanted"""
    while True:
        eingabe = input("Do you want your package to be insured? Enter 'yes'or 'no': ")
        if eingabe == "yes":# Versicherung erwünscht
            return True
        elif eingabe == "no":# Versicherung nicht erwünscht
            return False
        else:# Falsche Eingabe
            print("!!!Wrong input!!!")

def pickup()->bool:
    """DD...Asks whether a pickup is wanted"""
    while True:
        eingabe = input("Do you want your package to be picked up? Enter 'yes'or 'no': ")
        if eingabe == "yes":# Abholung erwünscht
            return True
        elif eingabe == "no":# Abholung nicht erwünscht
            return False
        else:# Falsche Eingabe
            print("!!!Wrong input!!!")

def international()->bool:
    """DD...Asks whether shipping is international"""
    while True:
        eingabe = input("Has your package to be shipped international? Enter 'yes'or 'no': ")
        if eingabe == "yes":# International
            return True
        elif eingabe == "no":# National
            return False     
        else:# Falsche Eingabe
            print("!!!Wrong input!!!")









"""___________Test Block___________"""


# size test
if __name__ == "__main__":
    print(size())
else:
    pass


#provider test
if __name__ == "__main__":
    print(provider())
else:
    pass
    

#max_time test
if __name__ == "__main__":
    print(max_time())
else:
    pass
    

#mass test
if __name__ == "__main__":
    print(mass())
else:
    pass
    


#insurance test
if __name__ == "__main__":
    print(insurance())
else:
    pass
    


#pickup test
if __name__ == "__main__":
    print(pickup())
else:
    pass



#pickup test
if __name__ == "__main__":
    print(international())
else:
    pass

