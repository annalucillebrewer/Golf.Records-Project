#Anna Brewer

#Assignment 10

#Part 1: This program read's a player's name and score
#from user input and saves them in golf.txt

#Part 2: This program reads the records
#from golf.txt file & displays them


#part 1
def main():

    #create golf.txt file
    golf_file = open('golf.txt', 'w')
    
    #get number of players
    num_players = int(input("Enter the number of players: "))

    for count in range (1, num_players + 1):
        #get name of each player
        print(f'Enter the name and score of player #{count}: ')
        name = input("Player's Name: ")

        #get score of each player
        score = input("Player's Score: ")

        #write name in file
        golf_file.write(f'{name}\n')
                         
        #write score in file
        golf_file.write(f'{score}\n')

        #display blank line
        print()

    #close file
    golf_file.close()

    #tell user data has been written to file
    print("Golf records have been written to golf.txt.")
    print()
    print()
    
main()

                      
#part 2

def records():

    #open a file to read
    golf_file = open('golf.txt', 'r')

    #read first line (which is a player's name)
    name = golf_file.readline()

    #if data is available continue reading file
    while name != '':

        #read player's score
        score = golf_file.readline()
        
        #display the records
        print(f'Player: {name}')
        print(f'Score: {score}')
        print()

        #strip newlines
        name = name.rstrip('\n')
        score = score.rstrip('\n')

        #read the next line in file
        name = golf_file.readline()
   
    #close file
    golf_file.close()

#call function
records()
