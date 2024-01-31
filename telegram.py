import sys
import time
import telepot
import json
import re
from op_webscraping_test import webscraping
from telepot.loop import MessageLoop


with open("tokens.json", "r") as f:
    TOKEN = json.load(f)["telegram_token"]

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        #for temporada, link in webscraping().items():
            #bot.sendMessage(chat_id, f"{temporada} {link}")
        padrao = r'"([^"]+)":' #"[^"]+":(?=)
        #re.findall(padrao, web_scraping())
        chaves = re.sub(r"'([^']+)':", r'**', str(webscraping()))
        #print(type(chaves))

        x = str(webscraping()).replace("{", "").replace("}", "").replace(",","\n").replace("'", "")
        bot.sendMessage(chat_id, chaves)

#TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)