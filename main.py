import pyrogram, os, asyncio

try: app_id = int(os.environ.get("app_id", None))
except Exception as app_id: print(f"⚠️ App ID Invalid {app_id}")
try: api_hash = os.environ.get("api_hash", None)
except Exception as api_id: print(f"⚠️ Api Hash Invalid {api_hash}")
try: bot_token = os.environ.get("bot_token", None)
except Exception as bot_token: print(f"⚠️ Bot Token Invalid {bot_token}")
try: custom_caption = os.environ.get("custom_caption", "`{file_name}`")
except Exception as custom_caption: print(f"⚠️ Custom Caption Invalid {custom_caption}")

AutoCaptionBot = pyrogram.Client(
   name="AutoCaptionBot", api_id=app_id, api_hash=api_hash, bot_token=bot_token)

start_message = """
<b>ɴᴀᴍᴀsᴛᴇ {}</b>
<b>ɪ ᴀᴍ ᴀɴ ᴀᴜᴛᴏᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ</b>
<b>ᴀʟʟ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴅᴏ ɪs ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɪ ᴡɪʟʟ sʜᴏᴡ ʏᴏᴜ ᴍʏ ᴘᴏᴡᴇʀ</b>
<b>@projectcrown</b>"""

about_message = """
<b>• 𝐍𝐚𝐦𝐞 : [AutoCaption V1](t.me/{username})</b>
<b>• 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 : [ʙʟᴀᴄᴋʜᴀᴛ](https://t.me/little_little_hackur)
<b>• 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : Python3</b>
<b>• 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : Pyrogram v{version}</b>
<b>• 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 : <a href=https://t.me/projectcrown>Click Here</a></b>
<b>• 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 : <a href=https://github.com/dor3Monbotz/CrownAutoCaption-Bot>Click Here</a></b>"""

@AutoCaptionBot.on_message(pyrogram.filters.private & pyrogram.filters.command(["start"]))
def start_command(bot, update):
  update.reply(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBot.on_callback_query(pyrogram.filters.regex("start"))
def strat_callback(bot, update):
  update.message.edit(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBot.on_callback_query(pyrogram.filters.regex("about"))
def about_callback(bot, update): 
  bot = bot.get_me()
  update.message.edit(about_message.format(version=pyrogram.__version__, username=bot.mention), reply_markup=about_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBot.on_message(pyrogram.filters.channel)
def edit_caption(bot, update: pyrogram.types.Message):
  if os.environ.get("custom_caption")
      motech, _ = get_file_details(update)
      try:
          try: update.edit(custom_caption.format(file_name=motech.file_name))
          except pyrogram.errors.FloodWait as FloodWait:
              asyncio.sleep(FloodWait.value)
              update.edit(custom_caption.format(file_name=motech.file_name, mote))
      except pyrogram.errors.MessageNotModified: pass 
  else:
      return
    
def get_file_details(update: pyrogram.types.Message):
  if update.media:
    for message_type in (
        "photo",
        "animation",
        "audio",
        "document",
        "video",
        "video_note",
        "voice",
        # "contact",
        # "dice",
        # "poll",
        # "location",
        # "venue",
        "sticker"
    ):
        obj = getattr(update, message_type)
        if obj:
            return obj, obj.file_id

def start_buttons(bot, update):
  bot = bot.get_me()
  buttons = [[
   pyrogram.types.InlineKeyboardButton("Updates", url="t.me/projectcrown"),
   pyrogram.types.InlineKeyboardButton("About 🤠", callback_data="about")
   ],[
   pyrogram.types.InlineKeyboardButton("➕️ Add To Your Channel ➕️", url=f"http://t.me/{bot.username}?startchannel=true")
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

def about_buttons(bot, update):
  buttons = [[
   pyrogram.types.InlineKeyboardButton("🏠 Back To Home 🏠", callback_data="start")
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

print("Telegram CrownAutoCaption V1 Bot Start")
print("Bot Created By https://t.me/little_little_hackur")

AutoCaptionBot.run()
