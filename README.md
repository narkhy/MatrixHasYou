# MatrixHasYou

A script that simulates on the terminal the four messages recieved by Thomas Anderson ("Neo") at the beggining of the popular film "The Matrix":

    Wake up, Neo...
    The Matrix has you...
    Follow the white rabbit.
    Knock, knock, Neo.
    
Watch a demonstration here:
https://asciinema.org/a/378478

- The script can be used anyway and anywhere, though -HINT- you can use it to customize your console in GNUL systems (GNUL = "GNU/Linux") add a command line at the end of /home/[USER]/.bashrc to run the MatrixHasYou script every time you launch your terminal (i.e.; python3 MatrixHasYou.py). This way the console will greet you everytime as if you were Neo :) (achieving this was the reason why I wanted to develop this script in the first place!).

- This script addresses in two different ways the problem of representing the movie scene with absolute fidelity. The first two lines drop the characters with a particular rythm, so they required a list of sleep times for each character (measured from the scene, letter by letter!). For the third line it uses a function (which I called "liveType") that displays the characters in any text string in a fancy way, as if it was being typed live (in this case at a constant rate, though, also measured from the film scene). Appart from the text string itself, "liveType" also takes 'delay' and 'remain' parameters: 'delay' sets the time it takes for new characters to appear, 'remain' sets the time the whole message will remain displayed.

- As the original scene times can likely result in too long a waiting for your everyday console usage, the variables 'delayFactor' and 'remainFactor' affect the whole code, so alter them to make characters appear faster and/or messages be cleared faster. Bear in mind though that you can end the escape the script at any moment by pressing CTRL + C. This will deploy a quick "671tcH iN Th3 M4tr1x" message before exiting the script.

- All the text should show in light green, but actual color will depend on your terminal color palette configuration I believe. For a better emulation of the real scene configure your 'light green' terminal color to be hex #5FFFAF (the closest 256 Xterm color to the actual text color in the film).


Things I want to add (but haven't found how to do them):

- Have a simple little GUI (and or CLI) from which users can determine 'remainFactor' and 'delayFactor', or change the lines, or the color, without having to edit manually the file.

- Play a slight 'beep' sound on each character appearing, emulating the real scene sound. This would be cool but I ignore if achiavable. I've tryed printing 'bel' escape sequences to no success so far.

- Inform the code to use a particular font for the messages (like: Tlwg Typewriter Regular) so the messages don't show in the default font on each system terminal.

Please, if you know how to accomplish any of these ^ feel free to contribute on the project's Git at:
https://github.com/narkhy/MatrixHasYou


Also, if you like The Matrix aesthetics, try (and rate) my Matrix inspired theme for Firefox:
https://addons.mozilla.org/es/firefox/addon/the-matrix-has-you/


Enjoy! ... as in free beer ;)

Call trans opt: received. 9-18-99 14:32:21 REC:Log>
