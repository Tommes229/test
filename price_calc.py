"""
This modul calculates the price for the different providers
"""



def dhl(mass:float, size:list, package_value:float)->dict:
    """DD...Calculates the price for your package with dhl"""
    dhl_options = {"2 kg - Päckchen S": 3.99, "2 kg - Päckchen M": 4.75, "2 kg Paket": 5.49, "5 kg Paket": 6.99,"10 kg Paket": 9.49,"31,5 kg Paket": 16.49}
    
    #Auswahl nach Masse
    if mass > 31.5:
        dhl_options.clear()  
    elif mass > 10:
        removed_option = dhl_options.pop("2 kg - Päckchen S", "x")
        removed_option = dhl_options.pop("2 kg - Päckchen M", "x")
        removed_option = dhl_options.pop("2 kg Paket", "x")
        removed_option = dhl_options.pop("5 kg Paket", "x")
        removed_option = dhl_options.pop("10 kg Paket", "x")
    elif mass > 5:
        removed_option = dhl_options.pop("2 kg - Päckchen S", "x")
        removed_option = dhl_options.pop("2 kg - Päckchen M", "x")
        removed_option = dhl_options.pop("2 kg Paket", "x")
        removed_option = dhl_options.pop("5 kg Paket", "x")
    elif mass > 2:
        removed_option = dhl_options.pop("2 kg - Päckchen S", "x")
        removed_option = dhl_options.pop("2 kg - Päckchen M", "x")
        removed_option = dhl_options.pop("2 kg Paket", "x")
    else:
        pass
    

    #Auswahl nach Größe    
    if size[0] > 120 or size[1] > 60 or size[2] > 60:
        dhl_options.clear()
        
    elif size[0] > 60 or size[1] > 30 or size[2] > 15:
        removed_option = dhl_options.pop("2 kg - Päckchen S", "x")
        removed_option = dhl_options.pop("2 kg - Päckchen M", "x")
        removed_option = dhl_options.pop("2 kg - Paket", "x")

    elif size[0] > 35 or size[1] > 25 or size[2] > 10:
        removed_option = dhl_options.pop("2 kg - Päckchen S", "x")
    else:
        pass
    
    #Versicherung Ausschluss
    if package_value > 0:
        removed_option = dhl_options.pop("2 kg - Päckchen S", "x")
        removed_option = dhl_options.pop("2 kg - Päckchen M", "x")
    if package_value > 25000: # Keine Versicherung bei Wert über 25000€ möglich
        dhl_options.clear()
        
    
    #Beste Option
    try:
        dhl_best_option = {next(iter(dhl_options)): dhl_options.get(next(iter(dhl_options)))}
    except StopIteration:
        dhl_best_option = None
    
    
    #Versicherung Preis Addition
    if dhl_best_option != None:
        if package_value > 0 and package_value <=500:
            dhl_best_option = {(next(iter(dhl_options)), "mit inkludierter Versicherung bis 500€"): dhl_options.get(next(iter(dhl_options)))}
        elif package_value > 500 and package_value <= 2500:
            dhl_best_option = {(next(iter(dhl_options)), "mit Zusatzversicherung bis 2500€"): (dhl_options.get(next(iter(dhl_options))) + 6)}
        elif package_value > 2500 and package_value <= 25000:
            dhl_best_option = {(next(iter(dhl_options)), "mit Zusatzversicherung bis 25000€"): round((dhl_options.get(next(iter(dhl_options))) + 18), 2)}
        
    #Return
    return dhl_best_option
    
    
    
    
    
def hermes(mass:float, size:list, package_value:float)->dict:
    """DD...Calculates the price for your package with ups"""
    hermes_options = {"Onlinepreis Hermes Päckchen": 4.50, "Onlinepreis S-Paket": 4.95, "Onlinepreis M-Paket": 5.95, "Onlinepreis L-Paket": 10.95}
    
    #Auswahl nach Masse
    if mass > 25:
        hermes_options.clear()
    
    #Auswahl nach Größe
    if (size[0] + size[2]) > 120:
        hermes_options.clear()
    elif (size[0] + size[2]) > 80:
        removed_option = hermes_options.pop("Onlinepreis Hermes Päckchen", "x")
        removed_option = hermes_options.pop("Onlinepreis S-Paket", "x")
        removed_option = hermes_options.pop("Onlinepreis M-Paket", "x")
    elif (size[0] + size[2]) > 50:
        removed_option = hermes_options.pop("Onlinepreis Hermes Päckchen", "x")
        removed_option = hermes_options.pop("Onlinepreis S-Paket", "x")
    elif (size[0] + size[2]) > 37:
        removed_option = hermes_options.pop("Onlinepreis Hermes Päckchen", "x")
        
    #Auswahl nach Versicherung
    if package_value > 50:
        removed_option = hermes_options.pop("Onlinepreis Hermes Päckchen", "x")
    if package_value > 500: # Keine Versicherung bei Wert über 500€ möglich
        hermes_options.clear()
        
    #Beste Option
    try:
        hermes_best_option = {next(iter(hermes_options)): hermes_options.get(next(iter(hermes_options)))}
    except StopIteration:
        hermes_best_option = None
        
    #Versicherung Preis Addition
    if hermes_best_option != None:
        if package_value > 0 and package_value <=50:
            hermes_best_option = {(next(iter(hermes_options)), "mit inkludierter Versicherung bis 50€"): hermes_options.get(next(iter(hermes_options)))}
        if package_value > 50:
             hermes_best_option = {(next(iter(hermes_options)), "mit inkludierter Versicherung bis 500€"): hermes_options.get(next(iter(hermes_options)))}

    #Return
    return hermes_best_option
    

def ups(mass:float, size:list, package_value:float)->dict:
    """Calculates the price for your package with ups"""
    ups_options = {"Onlinepreis Extrakleines": 6.38, "Onlinepreis Kleines": 8.50, "Onlinepreis Mittleres": 14.17, "Onlinepreis Großes": 17.71, "Onlinepreis Extragroß": 22.66}
    
    #Auswahl nach Masse
    if mass > 70:
        ups_options.clear()  
    

    #Auswahl nach Größe
    #Faktor aus Länge, Höhe, Breite
    if (size[0] * size[1] * size[2]) > 100000:
        dhl_options.clear()
        
    elif (size[0] * size[1] * size[2]) > 75000:
        removed_option = ups_options.pop("Onlinepreis Extrakleines", "x")
        removed_option = ups_options.pop("Onlinepreis Kleines", "x")
        removed_option = ups_options.pop("Onlinepreis Mittleres", "x")
        removed_option = ups_options.pop("Onlinepreis Großes", "x")
        
    elif (size[0] * size[1] * size[2]) > 50000:
        removed_option = ups_options.pop("Onlinepreis Extrakleines", "x")
        removed_option = ups_options.pop("Onlinepreis Kleines", "x")
        removed_option = ups_options.pop("Onlinepreis Mittleres", "x")
        
    elif (size[0] * size[1] * size[2]) > 25000:
        removed_option = ups_options.pop("Onlinepreis Extrakleines", "x")
        removed_option = ups_options.pop("Onlinepreis Kleines", "x")
        
    elif (size[0] * size[1] * size[2]) > 10000:
        removed_option = ups_options.pop("Onlinepreis Extrakleines", "x")
        
    else:
        pass
    
    #Versicherung Ausschluss
    #Bis 510€ Automatisch Versichert
    
        
    
    #Beste Option
    try:
        ups_best_option = {next(iter(ups_options)): ups_options.get(next(iter(ups_options)))}
    except StopIteration:
        ups_best_option = None
    
    if ups_best_option != None:
        if package_value > 0 and package_value <=510:
            ups_best_option = {(next(iter(ups_options)), "mit inkludierter Versicherung bis 510€"): ups_options.get(next(iter(ups_options)))}
        elif package_value > 510:
            ups_best_option = {(next(iter(ups_options)), "versichert in Höhe von 510€"): (ups_options.get(next(iter(ups_options))))}
            
    #Return
    return ups_best_option
    

def dpd(mass:float, size:list, package_value:float)->dict:
    """Calculates the price for your package with dpd"""
    dpd_options = {"XS- Paket": 4, "S- Paket": 4.50, "M- Paket": 5.90, "L- Paket": 9.70,"XL- Paket": 16.90}
    
    #Auswahl nach Masse
    if mass > 31.5:
        dpd_options.clear()  
    
    else:
        pass
        

    #Auswahl nach Größe
    #Summe aus längster und kürzester Seite
    size.sort()
    lowest = size[0]
    highest = size[-1]
    
    if highest + lowest > 300:
        dpd_options.clear()
    
    elif highest + lowest > 90:
        removed_option = dpd_options.pop("XS- Paket", "x")
        removed_option = dpd_options.pop("S- Paket", "x")
        removed_option = dpd_options.pop("M- Paket", "x")
        removed_option = dpd_options.pop("L- Paket", "x")
        
    elif highest + lowest > 70:
        removed_option = dpd_options.pop("XS- Paket", "x")
        removed_option = dpd_options.pop("S- Paket", "x")
        removed_option = dpd_options.pop("M- Paket", "x")
        
    elif highest + lowest > 50:
        removed_option = dpd_options.pop("XS- Paket", "x")
        removed_option = dpd_options.pop("S- Paket", "x")
        
    elif highest + lowest > 35:
        removed_option = dpd_options.pop("XS- Paket", "x")
        
    else:
        pass
        
    
    #Versicherung Ausschluss
    #Bis 520€ Automatisch Versichert
        
    
    #Beste Option
    try:
        dpd_best_option = {next(iter(dpd_options)): dpd_options.get(next(iter(dpd_options)))}
    except StopIteration:
        dpd_best_option = None
    
    
    #Versicherung Preis Addition
    if dpd_best_option != None:
        if package_value > 0 and package_value <=520:
            dpd_best_option = {(next(iter(dpd_options)), "mit inkludierter Versicherung bis 520€"): dpd_options.get(next(iter(dpd_options)))}
        elif package_value > 520:
            dpd_best_option = {(next(iter(dpd_options)), "Versichert in Höhe von 520€"): (dpd_options.get(next(iter(dpd_options))))}
        
        
    #Return
    return dpd_best_option

def gls(mass:float, size:list, package_value:float)->dict:
    """Calculates the price for your package with gls"""
    pass




"""___________Test Block___________"""


# dhl test
if __name__ == "__main__":
    print(dhl(6, [1,2,3], 510))
else:
    pass
    


# hermes test
if __name__ == "__main__":
    print(hermes(6, [1,2,3], 56))
else:
    pass

#ups test
if __name__ == "__main__":
    print(ups(5, [50,80,10], 550))
else:
    pass

#dpd test
if __name__ == "__main__":
    print(dpd(5, [7,40,9], 520))
else:
    pass