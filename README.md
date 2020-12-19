# MatrixHasYou

A script that simulates with the exact right times on the terminal the four messages recieved by Thomas Anderson ("Neo") at the beggining of the popular film "The Matrix":

    Wake up, Neo...
    The Matrix has you...
    Follow the white rabbit.
    Knock, knock, Neo.
    
Watch a demonstration here:
https://asciinema.org/a/378478

- The script can be used anyway and anywhere, though -HINT- you can use it to customize your terminal in GNUL systems (GNUL = "GNU/Linux") add a command line at the end of /home/[USER]/.bashrc to run the MatrixHasYou script every time you launch your terminal (i.e.; python3 MatrixHasYou.py). This way the console will greet you everytime as if you were Neo :) (achieving this was the reason why I wanted to develop this script in the first place!).

- This script addresses in two different ways the problem of representing the movie scene typed messages with high fidelity. The first two lines drop the characters with a particular rythm, so they required lists of sleep times for each character (measured from the scene, letter by letter!). For the third line it uses a function (which I called "liveType") that displays the characters in any text string in a fancy way, as if it was being typed live (in this case at a constant rate, though, also measured from the film scene). Appart from the text string itself, "liveType" also takes 'delay' and 'remain' parameters: 'delay' sets the time it takes for new characters to appear, 'remain' sets the time the whole message will remain displayed.

- As the original scene times can likely result in too long a waiting for your everyday terminal usage, the variables 'remainFactor' and 'delayFactor' affect the whole code, so lower them to make characters appear faster and/or messages be cleared faster. The script is provided already a bit accelerated at 0.2 and 0.7 for these factors, respectively.

- Escape the script at any time by pressing CTRL + C. Doing so will deploy a quick "Switch! Apoc!" (as Morpheus yells at the black cat 'deja vu' scene) followed by a "671tcH iN Th3 M4tr1x" message before exiting the script.

- All the text should show in light green, but actual color will depend on your terminal color palette configuration I believe. For a better emulation of the real scene configure your 'light green' terminal color to be hex #5FFFAF (the closest 256 Xterm color to the actual text color in the film).


Things I want to add:

- Have a little GUI (and/or CLI) from which users can set 'remainFactor' and 'delayFactor', or change the text strings, or the color, or opt-out the exit messages for a faster exit, all of this without having to edit the file manually.

- Play a slight 'beep' sound on each character appearing, emulating the real scene sound. This would be cool but I ignore if achiavable. I've tryed printing 'bel' escape sequences to no success on my system so far. Also playing a 'knocking on door' sound as the last line appears would add to the drama!

- Inform the code to use a particular size and font for the messages (i.e.: Tlwg Typewriter Regular) so the messages don't show in the default font/size on each system terminal, but in one resembling better the original from the movie.

- Add some code so that any keyboard inputs won't be printed on screen while the script runs (since Neo presses "CTRL + X", and later "Esc" twice and these actions show nothing on his screen).

Please, if you know how to accomplish any of these ^ feel free to contribute on the project's Git at:
https://github.com/narkhy/MatrixHasYou


Also, if you like The Matrix aesthetics, try (and rate) my Matrix inspired theme for Firefox:
https://addons.mozilla.org/es/firefox/addon/the-matrix-has-you/


Enjoy! ... as in free beer ;)

Call trans opt: received. 9-18-99 14:32:21 REC:Log>
