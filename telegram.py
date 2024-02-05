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
        seasons_dict = webscraping() 
        # due to the immutable nature of dicts, we create a new dict for the text in bold
        bold_dict = {}

        for titulo, link in seasons_dict.items():
            bold_title = f"<b>{titulo}</b>"
            bold_dict[bold_title] = link
        
        temporadas = str(bold_dict)

        #print(type(chaves))

        formatted_dict = temporadas.replace("{", "").replace("}", "").replace(",","\n").replace("'", "")
        bot.sendMessage(chat_id, formatted_dict, parse_mode='HTML')

#TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)