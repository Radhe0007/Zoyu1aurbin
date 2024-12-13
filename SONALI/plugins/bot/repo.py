from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ 𝗥ᴇᴘᴏs ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 𝗥ᴇᴘᴏ 𝗢ᴡɴᴇʀ ᴋᴏ 

✰ || @ll_RADHE7_ll ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗗𝗽_𝗰𝗼𝗹𝗹𝗲𝗰𝘁𝗶𝗼𝗻", url="https://t.me/DP_WORLD7"),
          InlineKeyboardButton("𝗥𝗔𝗗𝗛𝗘", url="https://t.me/ll_RADHE7_ll"),
          ],
               [
                InlineKeyboardButton("𝗧ᴇᴀᴍ 𝗜ɴᴄʀɪᴄɪʙʟᴇ 𝗕ᴏᴛs", url=f"https://t.me/ll_BOTCHAMBER_ll"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/RADHE_MUSIC_ROBOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/UNo.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
