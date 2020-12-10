# MatrixHasYou

A script that simulates on the terminal the 4 messages recieved by Thomas Anderson ("Neo") at the beggining of the popular film "The Matrix".

    Wake up, Neo...
    The Matrix has you...
    Follow the white rabbit.
    Knock, knock, Neo.

- This script basically incorporates a function (called liveType) to display any text in a fancy way as if it was typed live. It takes 3 parameters: text, delay and remain. Text being the text to apply the effect on, delay being the time it takes for the next character to be printed on screen, and remain being the time the message remains on display.

- It can be used anyway and anywhere you preffer. -Hint- On GNUL systems ("GNU/Linux") it may be interesting to add a command line at the end of your .bashrc file (it's in your /home/[USER]/ folder) to run this script every time you launch your terminal (i.e.; python3 MatrixHasYou.py), so that it greets you as if you were "Neo" (achieving this was the reason why I wanted to develop this script in the first place). -- If you know of better ways of achieving the same please say it in the comments (I've just started learning programming recently and developing this was an excuse to practice Python).

- "Delay" and "Remain" parameters, as well as the parameters given to the "sleep" functions used on the script try to reproduce as accurately as possible those from the original scene (I actually chronometered them one by one playing the video at a fourth of its normal speed to facilitate the task), however, as these original times can likely result in too long a waiting for the whole script to end, you can decrease the values for 'delayFactor' and 'remainFactor'in the code to make characters appear and messages be cleared faster.

- A "KeyboardInterrupt" option has been added so you can exit the script excecution pressing CTRL + C at any time for a quick "Glitch in the Matrix" message.

- Text should show in light green, but actual color will depend on your terminal color palette configuration I believe. For a better emulation of the real scene configure your light green terminal color to hex #5FFFAF (closest 256 Xterm color from the actual colors in the film).

- Enjoy! Collaborate! Leave comments.
