# Pen-Testing
A collection of random pieces of code I have created all sorted into one repository
No code here is guaranteed to run, so do not expect much

**RUN AT YOUR OWN RISK**

## **Rick.exe**
When run, this program will open the default browser on the computer and enter the URL of never going to give you up on YouTube. The catch is that it does this forever in a loop until the program closes, or your computer crashes.

## Keylogger Via Discord.py
This program creates 2 new pyw files called logger and sender. Logger usually gets flagged by antivirus as a keylogger and is automatically removed. This is a good idea as it is indeed a keylogger. The main file runs both of these new files. Logger.pyw creates a TXT file of all keyboard presses while sender.pyw  reads the TXT, formats it, then sends to an allocated discord channel that is hardcoded into the program. This is an awful way of transmitting the keystrokes, as you have to send the person a file with your bot token in and a channel from a server.
