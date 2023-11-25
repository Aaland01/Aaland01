
# Inneholder nyttige metoder for database logging
# Metoder for database aksess er byttet ut med prints

def addRecord(Tabell,values): 
    "Generisk funksjon for å legge til data"
    "Param: Navnet på tabellen som skal INSERTes INTO, og verdier/liste med verdier"
    "Antar at verdier som legges inn kommer som liste eller tuple"
    
    try:
        db = create_connection()
        #cursor = create_connection().cursor()
        
        #sql = "INSERT INTO "+ Tabell + " VALUES (?" + ",?"*(value_count-1) +")"
        print("Accessing "+Tabell+"...")

        if isinstance(values,list):
            value_count = len(values[0])
            sql = "INSERT INTO "+ Tabell + " VALUES (?" + ",?"*(value_count-1) +")"
            print(sql)
            print(values[0])
            #cursor.executemany(sql,values)
        else:
            value_count = len(values)   #Values is a tuple
            sql = "INSERT INTO "+ Tabell + " VALUES (?" + ",?"*(value_count-1) +")"
            print(sql)
            print(values)
            #cursor.execute(sql,values)
        
        #db.commit()
        
        print("Added values to " + Tabell)
    
    except:
    #except sqlite3.Error as error:
        print("Something went wrong:")
        #print(error)
    finally:
        if db:
            print("Closing..")
            #db.close()
            
            
# Mock method
def create_connection():
    "Tilgang til \"databasen\""
    "Param: none"
    "Return: Access or none"
    
    db = None

    try: 
        # Connect til databasen
        #db = sqlite3.connect("jernbaneDB.db")
        db = "Database"
    except:
        print("No connection.")
    return db

def main():
    operatør = (1,"Tog firma")
    addRecord("Operatør",operatør)
    vognoppsett = [(1,0,2),(2,1,1),(3,0,1)]
    addRecord("Vognoppsett",vognoppsett)
    
main()