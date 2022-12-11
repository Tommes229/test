"""
main module: Gives back the best offer
"""

#DD...Import von Funktionen
import price_calc as calc
import get_requirements as req
import time


#DD...Ausgabe einer Überschrift
def print_headline(msg:str)->str:
    """DD...Prints a headline"""
    print(len(msg)* "*")
    print(msg)
    print(len(msg)* "*")
    

#DD...Wilkommensnachricht
headline = "Welcome to optipack.py"
print_headline(headline)
time.sleep(1)
print("\nThis program determines the optimal service provider for your package")
time.sleep(1)


#DD...Abfrage der Anforderungen
provider = req.provider()
mass = req.mass()
size = req.size()
insurance = req.insurance()
package_value = req.value()

#DD...Änderung des Wertes wenn keine Versicheurng erwünscht ist
if insurance == False:
    value = 0

#Erstellen von leerem Dictionary
best_options = {}

#DD...Ausführen von Berechnungen
if "dhl" in provider:
    dhl_best_option = calc.dhl(mass, size, package_value)
    best_options.update(dhl_best_option)

if "hermes" in provider:
    hermes_best_option = calc.hermes(mass, size, package_value)
    best_options.update(hermes_best_option)
    
if "ups" in provider:
    ups_best_option = calc.ups(mass, size, package_value)
    best_options.update(ups_best_option)
    
if "dps" in provider:
    dps_best_option = calc.dps(mass, size, package_value)
    best_options.update(dps_best_option)
    
if "gls" in provider:
    gls_best_option = calc.gls(mass, size, package_value)
    best_options.update(gls_best_option)
        
    
    
    
#Vergleich der Berechnungen
sorted_best_options = dict(sorted(best_options.items(), key=lambda item:item[1])) # Sortieren der Optionen nach aufsteigendem Preis






#Ausgabe des Vergleichs





    

    