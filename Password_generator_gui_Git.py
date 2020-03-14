''' This is a window based application, you can use auto-to-py-exe to make it real Windows app'''
from tkinter import *
from random import *
import os

''' We will write all of passwords and place of application in txt file with name Passwords '''

''' Here we have all of data which will be needed to make a secure password'''
list_of_capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
locl_length = len(list_of_capital_letters) - 1
list_of_small_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
losl_length = len(list_of_small_letters) - 1
list_of_special_signs = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', "'\'", '|', ";", ":", "'", '"', ',', '<', '>', '.', '/', '?', '`', '~']
loss_length = len(list_of_special_signs) - 1

file_with_passwords = "Passwords.txt"  # Name of file where we will save all our passwords

dir_path = os.path.dirname(os.path.realpath(__file__)) # Get the real path to py file for checking if txt file exist if not the program will create a new one

done_text = "Done!"

error_counter = 0   # help us to control errors because sometimes try-except will be interfere 

''' Start the application window'''
window = Tk()
window.title("Password generator")
window.geometry('500x150+400+150')

''' Initializing all of labels and textfields'''
lable_place_of_application = Label(window, text="Where you will use this password? ")
lable_place_of_application.grid(column=0, row=0)

textfield_place_of_application = Entry(window,width=20)
textfield_place_of_application.grid(column=2, row=0)

label_numbers = Label(window, text="Amount of numbers in password: ")
label_numbers.grid(column=0, row=1)

textfield_numbers = Entry(window,width=20)
textfield_numbers.grid(column=2, row=1)

label_letters = Label(window, text="Amount of letters in password: ")
label_letters.grid(column=0, row=2)

textfield_letters = Entry(window,width=20)
textfield_letters.grid(column=2, row=2)

label_signs = Label(window, text="Amount of special signs in password: ")
label_signs.grid(column=0, row=3)

textfield_signs = Entry(window,width=20)
textfield_signs.grid(column=2, row=3)

label_result = Label(window, text="Here will be your password", fg="blue")
label_result.grid(column=1, row=4)

label_done = Label(window, text="", fg="green")
label_done.grid(column=1, row=6)

def clicked():

    ''' Here we use try-except construction to catch problems with file oppening(file can be opened and we can't add new information)'''
    try:
        file=open( dir_path + '/' + file_with_passwords, "a+") # Open file Passwords only for adding(a+) if it not exist we make it
    except:
        label_done.configure(text="Please check the file. Maybe you should close it", fg="red")

    place_of_application = str(textfield_place_of_application.get())
    ''' All of this try-except constructions we have to prevent user mistake'''
    try:
        numbers_in_password = int(textfield_numbers.get())
    except:
        label_done.configure(text="Check input!", fg="red")
    try:    
        letters_in_password = int(textfield_letters.get())
    except:
        label_done.configure(text="Check input!", fg="red")   
    try:      
        special_signs_in_password = int(textfield_signs.get())
    except:
        label_done.configure(text="Check input!", fg="red")

    ''' Free the pasword variable to get new, clean password'''
    unfinished_password = []
    mixed_password = []
    finished_password = ""
    ''' Separate all parts of our pasword for easy work with it'''
    prepared_numbers = []
    prepared_capital_letters = []
    prepared_small_letters = []
    prepared_special_signs = []

    random_password_indexes = []

    try:
        ''' Random generator for numbers '''
        for i in range(numbers_in_password):
            drawn_number = randint(0, 10)
            prepared_numbers.append(str(drawn_number))

        ''' Random generator for letters '''
        amount_of_capital_letters = randint(0, letters_in_password) 
        for i in range(amount_of_capital_letters):      
            possition = randint(0, locl_length)
            prepared_capital_letters.append(list_of_capital_letters[possition])

        amount_of_small_letters = letters_in_password - amount_of_capital_letters
        for i in range(amount_of_small_letters):
            possition = randint(0, losl_length)
            prepared_small_letters.append(list_of_small_letters[possition])
       
        ''' Random generator for special signs '''
        for i in range(special_signs_in_password):
            possition = randint(0, loss_length)
            prepared_special_signs.append(list_of_special_signs[possition])
    
        ''' Here we connecting all parts of our password to make the stronger one'''
        unfinished_password = prepared_capital_letters + prepared_numbers + prepared_small_letters + prepared_special_signs 
        upl = len(unfinished_password) - 1

        try:
            random_password_indexes = list(sample(range(upl+1), upl)) # if it does not work we will use reserve method
        except:    
            for i in range(upl):                                      # this method we will use. It has less security
                random_password_indexes.append(randint(0, upl))   

        for i in range(upl):
            mixed_password.append(unfinished_password[int(random_password_indexes[i])]) # Here we mixed the password to make it stronger
        error_counter = 0

        ''' Join all of our lists in one string'''
        finished_password = "".join(mixed_password)
        main_string = "This password: " + finished_password + " was used for " + place_of_application

        ''' Writing out password to txt file'''
        file.write(main_string + "\n")   
         
    except:
        error_counter = 1

    if error_counter == 0:
        label_result.configure(text= finished_password, fg="blue") 
        label_done.configure(text= done_text, fg="green")   
    else:
        label_result.configure(text="Here will be your password", fg="blue")

    ''' The end of the work with file writer'''
    file.close()
    
    ''' Open the txt file with our password/s''' 
def open_file():
    os.system(dir_path + '/' + file_with_passwords)

''' Initializing all of our buttons in application'''
button_open_file = Button(window, text="Open file", command=open_file)
button_open_file.grid(column=0, row=5)

button_generate = Button(window, text="Generate", command=clicked)
button_generate.grid(column=2, row=5)

window.mainloop()