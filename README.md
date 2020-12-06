# matrix-has-you
A script that simulates on terminal the messages recieved by Thomas Anderson at the beggining of the popular film "The Matrix".

- This script basically incorporates a function to display any text in a fancy way as if it was typed live.

- It can be used anyway and anywhere you preffer. However, on GNUL ("GNU/Linux") systems it may be interesting to add a command to your .bashrc (in your /home/[USER]/ folder) to run this script every time you lauch your terminal (i.e.; python3 matrix-has-you.py), therefore greeting you as if you were "Neo" (This was the reason why the script was written in the first place).

- "Delay", "Remain" parameters and the parameters given to the "sleep" functions used try to reproduce as exactly as possible those from the original scene, however, as this can result in long waiting time for the script to end you can change 'delayMultip' and 'remainMultip' to make text appear and disappear faster.

- Also, a "KeyboardInterrupt" option has been added so you can exit the excecution pressing CTRL + C at any time with a "Glitch in the Matrix" message.

- Text should show in light green, but actual color will depend on your terminal color palette configuration.
