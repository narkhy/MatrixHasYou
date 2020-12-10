# MatrixHasYou

A script that simulates on the terminal the four messages recieved by Thomas Anderson ("Neo") at the beggining of the popular film "The Matrix":

    Wake up, Neo...
    The Matrix has you...
    Follow the white rabbit.
    Knock, knock, Neo.

- This script basically incorporates a function (which I called "liveType") that displays any text string (given as parameter) in a fancy way, as if it was typed live! Appart from the text string itself, the function also takes 'delay' and 'remain' parameters: the first sets the time it takes for new characters to be printed on screen, the second sets the time the whole message remains on display.

- The script can be used anyway and anywhere you preffer, though -Hint- on GNUL systems (I use GNUL for GNU/Linux) it may be interesting to add a command line at the end of your .bashrc file (at your /home/[USER]/ folder) to run the MatrixHasYou script every time you launch your terminal (i.e.; python3 MatrixHasYou.py), so that it greets you everytime as if you were "Neo" and bla, bla, (achieving this behaviour for my terminal was the reason why I wanted to develop this script in the first place!). Please comment if you know of better ways to achieve the same (I've just started learning programming very recently and developing this script was my excuse to practice some Python).

- 'delay' and 'remain' parameters, as well as the parameters given to the 'sleep' functions used on this script try to reproduce -as accurately as possible- those from the original scene (I actually chronometered some of them one by one playing the video at a fourth of its normal speed to facilitate the task), however, as these original times (particularly the 'remain' ones) can likely result in too long a waiting for the whole script to end and your terminal to be ready to use, I recommend decreasing the values for 'delayFactor' and 'remainFactor' in the code to make characters appear faster and/or messages be cleared faster. I like to use 0.2 for 'remainFactor' and 0.7 for 'delayFactor'. You'll have to set these up manually.
 
- A "KeyboardInterrupt" option has been added so you can exit the script excecution at anytime by pressing CTRL + C for a quick "671tcH iN Th3 M4tr1x" message. You can freely edit this to suit your prefference (actually the whole of the code as this is published under the GPL license).

- All the text should show in light green, but actual color will depend on your terminal color palette configuration I believe. For a better emulation of the real scene configure your 'light green' terminal color to be hex #5FFFAF (the closest 256 Xterm color to the actual text color in the film).

Enjoy!
