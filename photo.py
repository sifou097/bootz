from telethon import TelegramClient, events, sync
import os,random
from PIL import Image
#انضم عزيزي @xxfix
api_id = 11111111
api_hash = ""
client = TelegramClient(f'session_name', api_id, api_hash).start(bot_token="token")

def ze(inp, ou, iz):
    with Image.open(inp) as image:
        imag = image.resize(iz)
        imag.save(ou, "PNG")

@client.on(events.NewMessage())
async def newMessageListener(event):
    try:
	    ran,ran2 = [str(random.randint(1000, 99999)),str(random.randint(1000, 99999))]
	    file_name = f"{ran}.jpg"
	    if event.photo:
	        await event.download_media(file_name)
	        ze(file_name, f"{ran2}.png", (100, 100))
	        await client.send_file(event.chat.id,f'{ran2}.png',force_document=True)
	        os.system(f'rm {ran2}.png && rm {file_name}')
	    elif event.message.message == "/start":
	    	await event.reply("hi ^ᴥ^\nsend photo plz")
	    else:
	    	await event.reply("just photo plz")
    except Exception as E:
    	await event.reply(f"erorr:{str(E)}")

client.run_until_disconnected()