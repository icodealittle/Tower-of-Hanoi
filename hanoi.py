from hanoi_viz import *

num_disk = 5
max_disk = 8
min_disk = 1
target = "Luna" #Tower name
source = "Tuna" #Tower name
help_t = "Fish" #Tower name

def disks():
    '''Function: disks
        Input: None.
        Returns: the number of disks that the user would want to play with – in int form. 
        Do: Promt the user to see the amount of disks they want to play with. There are different conditionals that make sure the
                user to input correct range in the specify input prompt.
    '''

    while True:
        input_user = input('What is the number of disk (2 - 8)?  ') #Ask user to input an integer range form 2 to 8, whereas 8 is max disk.
        no_special_charac = input_user.isdigit()

        if no_special_charac == False:
            print('It is not a valid numbers!!!') #prompt user input integer within the digit function range and no special characters

        else:
            num_in_int = int(input_user)
            if num_in_int < min_disk or num_in_int > max_disk: #Check to see if the user input numbers within the range of 1 to 8
                print('It is not a valid numbers!!!')
            else:
                return num_in_int
                break
            
def move_tower(num_disk, source, target, help_t, towers):
    ''' Function: move_tower
        Input: num_disk – int, source, target, and help_t – index of list, towers – intiative_towers function variable
        Return: Nothing
        Do: Based of a game, "Tower of Hanoi" – where the disk(s) move from one tower to another tower. Inside this function, the
                disks are being move from the source (Tuna) to the target (Luna) while using help_t (Fish) as a placeholder.
    '''
    
    #base case
    if num_disk == 1:
        move_disk(source, target, towers) #one just left move. move final disk to the tower
    else:
        #Using recursion function to make the subproblem smaller...?
        move_tower(num_disk - 1, source, help_t, target, towers)
        move_disk(source, target, towers)
        move_tower(num_disk - 1, help_t, target, source, towers)

def main():
    num_disk = disks()
    towers = initialize_towers(num_disk, source, target, help_t) #Called function into the main function
    move_tower(num_disk, source, target, help_t, towers)

main()
