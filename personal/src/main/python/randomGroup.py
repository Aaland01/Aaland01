import random

def randomgroups(elever,gruppestørrelse):
    "Oppretter tilfeldige grupper av elevene, basert på ønsket gruppestørrelse"
    "Param: Liste som skal tilfeldig fordeles, og ønsket gruppestørrelse"
    "Returns: En liste med tilfeldige grupper i lister."
    #Validering
    if ( not (isinstance(elever,list))):
        print("Trenger en liste!")
        return
    if ( not (isinstance(gruppestørrelse,int))):
        print("Gruppestørrelse må være et tall")
        
    else:
        antallElever = len(elever)
        antallGrupper = antallElever//gruppestørrelse
        tilOvers = antallElever%gruppestørrelse
        print(f'Antall grupper: {antallGrupper}, til overs: {tilOvers}')
        
        random.shuffle(elever)
        print(f'Shuffle: {elever}')
        
        tilfeldigeGrupper = []
        for i in range(0,antallGrupper):
            gruppe = []
            for i in range(gruppestørrelse):
                gruppe.append(elever.pop(0))
            tilfeldigeGrupper.append(gruppe)
            
        # Om elever til overs er mer enn halve gruppestørrelsen, blir de egen gruppe
        if (tilOvers > gruppestørrelse//2):
            tilfeldigeGrupper.append(elever)
        else: 
            while not tilOvers<=0:
                print(f'Til overs: {tilOvers}')
                elev = elever.pop()
                tilOvers -= 1
                tilfeldigeGrupper[tilOvers].append(elev)
        finPrint(tilfeldigeGrupper)
        return tilfeldigeGrupper
    
    
def finPrint(liste):
    counter = 0
    for gruppe in liste:
        counter+=1
        print(f'Gruppe {counter}: {gruppe}')
    
testListe = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
randomgroups(testListe,4)

      