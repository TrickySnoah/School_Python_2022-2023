#Imports
#-----#
import retailitem as ri
import time
import pickle

#-----#

#Notes
#-----#

#OPEN AND CLOSE THE FILES EVERYTIME A FILE IS USED, PER FUNCTION

#-----#

#---------------------------Main Menu Functions---------------------------#

#A main function to call other functions within the main function
def main_menu():
    
    #Create a variable to check if the user wants to continue
    m = 'open'
    
    #Loop until the user chooses to leave the program
    while True:
        
        #Before anything, try to open the file, inventory.dat, and try to pickle things.
        try:
            infile = open('inventory.dat', 'rb')
            #If that works, move things from the file into the list
            inventory = pickle.load(infile)
            infile.close() #Close the file after unpickling items
        except:
            print('WARNING: Either the file inventory.dat is empty, or the file does not exist.')
            time.sleep(3) #This is here to give the user time to read
            
        #A beginning statement
        print('\n\n\nWelcome to the ACME Main Menu.\n')
        
        #A statement before the options + the options
        print('Please select an action from the following:\n'+
              'Press 1 to access the inventory control system.\n'+
              'Press 2 to access the retail store.\n'+
              'Press 3 to exit the main menu.')
        
        #Loop for validation
        while True:
            
            #Ask the user for an option
            ui = input('Enter your choice: ')
            
            #Check for the user's input
            if ui == '1':
                
                #Check to see if the file exists. Create it if it doesn't
                try:
                    infile = open('inventory.dat', 'rb')
                    infile.close()
                except:
                    print("Inventory file doesn't exist. Creating the file now.")
                    infile = open('inventory.dat', 'w')
                    infile.close()
                ICS()
                break
            
            #If the user choose option 2, open the Retail Store
            elif ui == '2':
                #RS()
                break
            
            #If the user chooses option 3, exit the main menu
            elif ui == '3':
                m='exit'
                break
                
            #VALIDATION
            else:
                print('\nPlease choose an option from the table.\n')
        
        #Check to see if the user chose to exit
        if m == 'exit':
            #Print a closing message
            print('\nGoodbye.')
            break
                
                
#---------------------------Inventory Control System Functions---------------------------#
                
#A function for the Inventory Control System
def ICS():
    
    #Before anything, load the information from the file into the list. VALIDATION WILL BE HERE
    try:
        infile = open('inventory.dat','rb')
        inventory = pickle.load(infile)
        infile.close()
    except:
        inventory = []
    
    #Create a loop here to loop until the players chooses option #4
    while True:
        
        #A beginning statement
        print('\nWelcome to the ACME Inventory Control System.\n')
        
        #A statement before the options + the options
        print('Please select an action from the following:\n'+
              'Press 1 to display the current inventory.\n'+
              'Press 2 to add inventory items to the current inventory.\n'+
              'Press 3 to save the inventory.\n'+
              'Press 4 to exit.')
        
        #Loop for validation
        while True:
            
            #Ask the user to select an option
            ui = input('Select an action(1, 2, or 3. Press 4 to EXIT): ')
            
            #Check for the user's choice
            if ui == '1':
                inventory = display_inventory(inventory)
                break
            elif ui == '2':
                inventory = add_items(inventory)
                break
            elif ui == '3':
                inventory = save_inventory(inventory)
                break
            elif ui == '4':
                inventory = exitting_ISC()
                break
            else:
                print('\nPlease choose an option from the table.\n')
            
        #Check to see if the user chose option #4
        if inventory == 'exit':
            break
    
    #Once the user chooses to exit return the to main menu
    return
          
#Function to show the inventory
def display_inventory(inventory):
    
    #Try to load the contents from the file into a list, check it's length, and move accordingly
    try:
        if len(inventory) < 1:
            p=p
    except:
        #If there is nothing within the list, print this statement
        print('\nThere is nothing within the file.')
        time.sleep(3) #This is here to give the user time to read
    else:
        #Print a message before display everything
        print('\nHere are items within the inventory:')
        
        #If there are items within the file, print every single key
        for key in inventory:
            print(key)
            #print(key.get_name()) <-- this is to check for a description asked by the user
            
        time.sleep(5) #This is here to give the user time to read
            
    #return because the purpose of the function has been served
    return inventory

#Function to add items to the inventory
def add_items(inventory):
    
    #Loop until the user no longer wants to
    while True:
        
        #Reset the User Input every loop
        ui = 1
        
        #Ask the user for information
        #Loop to check to see if the description alread exists
        while True:
            description = input('\nEnter an item description: ')
            if description in inventory:print('That description already exists');ui = input('Would you like to replace that item information? (y/n) ')
            if ui == 'y' or ui == 1: break
            else: continue
        units = input(f'Enter the number of units for {description}: ')
        price = input(f'Enter the price per unit for {description}: ')
        
        #Create an object for that item
        item_info = ri.RetailItem(description, units, price)
        
        #Append the item info into the list
        inventory.append(item_info)
        
        #Ask the user if they would like to continue
        cont = input('Would you like to continue? (y/n) ')
        
        #Check the user's input and move accordingly
        if cont == 'y':
            continue
        else:
            break
    
    #Return because this function's purpose has been served
    return inventory

#Function for saving the changes made to the file
def save_inventory(inventory):
    
    #Open the file, dump the info, and tell the user if this was successful
    try:
        infile = open('inventory.dat','wb') #open file
        pickle.dump(inventory, infile)
        infile.close() #close file
        print('\nThe changes have been successfully saved.')
    except:
        print('\nThere was a problem trying to save the data.')
    time.sleep(3) #This is here to give the user time to read
    
    #Return because the purpose has been served
    return inventory
    

def exitting_ISC():
    
    #Return the key word to leave the inventory
    return 'exit'

#---------------------------Retail Store Functions---------------------------#




main_menu()