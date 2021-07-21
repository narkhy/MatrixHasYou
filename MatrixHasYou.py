# MatrixHasYou.py Made by narkhy, 2020.
# This python code reproduces messages on the terminal emulating those from the film "The Matrix" (1999).
from os import system, name
from time import sleep
from sys import exit

def clearTrm ():
    '''Clears the terminal regardless of OS.
       For cool systems: 'clear'.
       For uncool systems: 'cls'.'''
    if name == 'posix':
        _ = system('clear')
    else:
        _ = system('cls')

def liveType (text='liveType demo text', delay=0.02, remain=3):
    '''Makes text strings seem typed live. Inspired in the film "The Matrix".
    PARAMETERS:
      'text' == text string to simulate typed live
      'delay' == seconds before new character shows up
      'remain' == seconds before message dissappears'''
    for letter in text:
        print (letter, end='', flush=True)
        sleep (delay)
    sleep (remain)

# These special strings here are called ANSI escape codes, also SGR. They are here for text formating.
LIGHT_GREEN = '\033[92m'
DARK_GREEN = "\033[0;32m"
BOLDON = '\033[1m'
CURSORON = '\x1b[?25h'
CURSOROFF = '\x1b[?25l'
END = '\033[0m'

if __name__ == "__main__":

    remainFactor = 0.2    # Affects typing speed. Lower for faster emulation. '1' for real scene times.
    delayFactor = 0.7     # Affects messages display time. Lower for faster emulation. '1' for real scene times. 

    _here = "\n\n\n      " # This is meant for later prints positioning

    urName = "Neo" # If you change this to a name longer than "Neo" provide times accordingly to "secs1" list.
    msg1 = f"Wake up, {urName}..." 
    msg2 = "The Matrix has you..."
    msg3 = "Follow the white rabbit."
    msg4 = f"Knock, knock, {urName}."
    exitMsg = "    671tcH iN Th3 M4tr1x\n"
    exitMsg2 = "         gLiTCh In tH€ WaTriX\n"

    # The following lists (secs1 and secs2) are the time lapses for the appearing of each character
    # They have been measured directly from the real film scene.
    secs1 = [0, 0.1500, 0.1625, 0.1500, 0.1625, 0.1500, # The last 3 times in secs1 are for the 3 dots (...)
                0.1625, 0.1500, 0.1200, 0.1250, 0.1200, # so you want *them* to always be the last 3.
                0.1250, 0.0625, 0.0875, 0.0625]         # Insert your new times per character right *before* them!
    
    secs2 = [0, 0.7325, 0.6700, 0.6000, 0.7800, 0.0950, 
                0.1350, 0.1075, 0.5275, 0.6225, 0.0080, 
                0.1200, 0.1475, 0.4500, 0.0080, 0.4275, 
                0.1275, 0.1425, 0.3550, 0.2275, 0.1450]

    try:
        clearTrm()
        print(BOLDON + LIGHT_GREEN + CURSOROFF, end = '') # Sets text to bold green and hides the cursor.
        print(_here, end = '')
        x1 = 0
        for i in msg1:
            sleep (secs1[x1]*delayFactor)
            print (msg1[x1], end='', flush=True)
            x1 += 1
        sleep(16.03*remainFactor)   # 16.03 seconds measured from the real scene from film "The Matrix"
        clearTrm()

        print(_here, end = '')
        x2 = 0
        for i in msg2:
            sleep (secs2[x2]*delayFactor)
            print (msg2[x2], end='', flush=True)
            x2 += 1
        sleep(7.54*remainFactor)    # 7.54 seconds measured from the real scene from film "The Matrix"
        clearTrm()

        print(_here, end = '')
        liveType(msg3, 0.1167*delayFactor, 8.515*remainFactor)  # 0.1167 and 8.515 seconds measured from the real scene from film "The Matrix"
        clearTrm()

        print(_here, end = '')
        print(msg4, end = '')

        print(_here * 2, end = '')
        sleep(4)
        clearTrm()
        
    except KeyboardInterrupt:
        clearTrm ()
        print(_here, end = '')
        print (END + LIGHT_GREEN + "Switch!")
        sleep (0.6*remainFactor)
        clearTrm ()
        print(_here, end = '')        
        print ("Switch!\n\t\tApoc!")
        sleep (1.2*remainFactor)
        clearTrm ()
        print(_here, end = '\n\n\n  ')
        print(exitMsg, flush=True)
        sleep (0.9*remainFactor)
        clearTrm ()
        print(_here, end = '\n    ')
        print(exitMsg2, flush=True)
        sleep (0.6*remainFactor)
        clearTrm ()
        print(_here, end = '')
        liveType(exitMsg, 0.045*delayFactor, 3.5*remainFactor)
        print(CURSORON + END) # Unhide cursor
        clearTrm()
        exit()    
    print(CURSORON + END) # Unhide cursor and set all text formating back to system default.
    ClearTrm()
