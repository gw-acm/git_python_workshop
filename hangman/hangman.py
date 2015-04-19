import random

'''
Title: Command Line Hangman
Authors: Neel Shah and Brannon McGraw
Version: 1.0

Simple hangman where computer randomly selects a word and
lets the user guess letters of it until they win or lose.

The dictionary was provided from http://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=markup

This program was created for the GWU chapter of ACM's Github and Python workshop
which occured on 4/19/2015
'''

word = None             # Global variable that holds the word picked from dictionary
word_len = 0            # Global variable that holds the length of the word
status = []             # Global variable to hold the status of the users play
guessed_letters = []    # Global variable to hold the letters that the user guessed
indicies = []           # Global variable to hold the indicies of where the guessed letter
                        # is in the word. This is reset each guess iteration
lives = 7               # Global variable to hold the total number of lives

'''
This functions prints out a welcome message telling the user the basics of the game.

@param - None
@return - None
'''
def welcome_message():
    print "Command Line hangman"
    print "Man has 7 body parts:"
    print "2 legs, 2 arms, 2 body pieces, 1 head"
    print "have fun!"
    print ""

'''
This function takes no arguments. Its job is to ask the user
for the name of the dictionary file. Then, using that name,
it will open the file and read all of the lines from it.
It will return the list that contains the lines of the
dictionary.

@param - None
@return - A list containing all lines of the file
'''
def get_dictionary():
    # TODO: Fill in this function

    return dictionary

'''
This function randomly selects a word from the dictionary
that is received from the get_dictionary function.
It then turns all letters of the selected word to lowercase.

@param - List of all words read from get_dictionary function
@return - A single word with all lowercase characters
'''
def computer_pick_word(dictionary):
    # TODO: Fill in this function

    return word

'''
This function is used to initially fill the status
list. On first run, it should be filled with all '_'
so the user knows that they have not guessed any letters.
It uses word_len, and the status list.

@param - None
@return - None
'''
def fill_status_init():
    global word_len
    global status

    # TODO: Fill in this function

'''
This function fills the status list with the letters
that the user accurately guessed.  It uses the indicies
list and obviously, the status list.

@param - None
@return - None
'''
def fill_status(guess):
    global status
    global indicies

    # TODO: Fill in this function

'''
This functions prompts the user to guess one letter.
If the user enters anything other a single letter,
it will yell at them and prompt them to enter again
until they get it right.

@param - None
@return - Character entered by user (can leave as string)
'''
def get_letter():
    # TODO: Fill in this function

    return guess

'''
This function takes the character entered by the user
and checks to see if the user guessed it previously.
If they have, it prints out that message and returns -1.
If they have not guessed it previously, it returns 0.
It uses the guessed_letters list to see if the letter
has been guessed previously.

@param - guess, which is the users letter guess
@return - returns -1 if user already guessed, 0 otherwise
'''
def has_guessed(guess):
    global guessed_letters

    # TODO: Fill in this function

'''
This function loops through the word and checks if
the guessed letter is in it. It will then append the
indicies that the letter is at to the indicies list.
This function uses the variables word, word_len, status,
and indicies.
This function 'returns' by setting values inside the indicies
list.

@param - guess, which is the users letter guess
@return - None
'''
def does_word_contain_letter(guess):
    global word
    global word_len
    global status
    global indicies

    # TODO: Fill in this function

'''
This function notifies the user if the guess they made is bad.
It will be called from run_guess_sequence when length of indicies
is 0. This means that does_word_contain_letter found no instances
of it in the word.
This function subtracts one from the lives variable and prints out a
message notifying the user that their guess is bad.

@param - guess, which is the users letter guess
@return - None
'''
def bad_guess(guess):
    global lives

    # TODO: Fill in this function

'''
This function compares the current state of what has been guessed
with the word the computer picked. If the characters of the status
list equals the word, then this will return True and notify the user
that they won. If the lives reaches 0, then it will return True as well.
Otherwise, it returns False.

@param - None
@return - True if game ends, False otherwise
'''
def end_if_win_loss():
    global lives
    global word
    global word_len
    global status

    # TODO: Fill in this function

'''
This function runs the guessing sequence. It gets the letter
from the user, it then checks if it has been guessed before,
it will also check if the word contains the guess, and then
it will determine if it is a good or bad guess. It will fill
status, which is the list that contains the users valid guesses.

@param - None
@return - None
'''
def run_guess_sequence():
    global word
    global word_len
    global status
    global guessed_letters
    global lives
    global indicies

    guess = get_letter()

    if has_guessed(guess) != 0:
        print "Already guessed, new letter please"
        return status
    else:
        guessed_letters.append(guess)

    does_word_contain_letter(guess)

    if len(indicies) == 0:
        bad_guess(guess)

    fill_status(guess)

'''
This is the main loop structure of the game. It sets up the
various variables. It will get a word from the dictionary,
set up the status list, guessed_letters list, the lives,
and the loop value.

In the loop, it will print out information about the state
of the game: what you have guessed, your progress, and lives.

It will then flush variables that need to be cleared and then
call the run_guess_sequence() function which actually does the
guessing.

If the end_if_win_loss() function returns True, then the game
will exit. If it returns False, it will run guessing again.

@param - dictionary, is the list of words read from the file
@return - None
'''
def play_game(dictionary):
    global word
    global word_len
    global guessed_letters
    global status
    global lives
    global indicies

    word = computer_pick_word(dictionary).rstrip('\n')
    word_len = len(word)
    guessed_letters = []
    fill_status_init()
    lives = 7
    end = False

    print "Computer picked word, lets play!"
    print "Word is of length %d" % word_len
    print ""

    while end == False:
        print "You have guessed: ",
        for c in guessed_letters:
            print c+" ",
        print ""
        print "You have %d more lives" % lives
        print ""
        for c in status:
            print c+" ",
        print ""
        print ""

        indicies = []
        run_guess_sequence()
        end = end_if_win_loss()

'''
This function reads in the dictionary and gets a list of words.
It also calls the play_game function which starts the game.

@param - None
@return - None
'''
def start_game():
    dictionary = get_dictionary()

    play_game(dictionary)

'''
This function prints goodbye.

@param - None
@return - None
'''
def exit_message():
    print "Goodbye!"

welcome_message()   # Prints out a greeting and instructions
start_game()        # Starts the game
exit_message()      # Prints out goodbye
