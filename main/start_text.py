from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt="ʜʏ ᴜꜱᴇʀ , ɪ ᴀᴍ ᴀ ᴘᴇʀꜱᴏɴᴀʟ ʙᴏᴛ ."
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("🤖 SOURCE CODE", url="https://github.com/amitpatle/DankRobot")
        ],])
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"ᴡᴏᴀʜ  {msg.from_user.mention}  ,ʏᴏᴜʀ ꜰɪʟᴇꜱ' ᴘᴇʀꜱᴏɴᴀʟ ꜱᴛᴀɴᴅ-ᴜᴘ ᴄᴏᴍᴇᴅɪᴀɴ!\n ᴜɴʟᴇᴀꜱʜ ᴛʜᴇ ʟᴀᴜɢʜᴛᴇʀ, ᴏɴᴇ ᴡᴀᴄᴋʏ ꜰɪʟᴇɴᴀᴍᴇ ᴀᴛ ᴀ ᴛɪᴍᴇ. 🤖🎤.\n> 🥷🏼 ᴅᴇᴠᴇʟᴏᴘᴇʀ <b><a href=https://github.com/amitpatle>  ᴀᴍɪᴛ </a></b>"                                     
    button= [[
        InlineKeyboardButton("🤖 ʙᴏᴛ ᴄᴏᴅᴇ ", url="https://github.com/amitpatle/DankRobot")
        ],[
        InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        InlineKeyboardButton("📡 About", callback_data="about") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt = "ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴀ ꜰɪʟᴇ ᴀɴᴅ /ʀᴇɴᴀᴍᴇ <ɴᴇᴡ ɴᴀᴍᴇ> ᴡɪᴛʜ ʀᴇᴘʟᴀʏᴇᴅ ʏᴏᴜʀ ꜰɪʟᴇ\n\n"
    txt += "ꜱᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄ \n"
    txt += "/view ᴛᴏ ꜱᴇᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ \n"
    txt += "/del ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ"
    button= [[        
        InlineKeyboardButton("🚫 ᴄʟᴏꜱᴇ", callback_data="del"),
        InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()  
    Source="<a href=https://github.com/amitpatle/DankRobot>Click Here</a>"
    txt=f"<b>Bot Name: {me.mention}\nDeveloper: <a href=https://github.com/amitpatle>ᴀᴍɪᴛᴘᴀᴛʟᴇ</a>\n</a>\nSource Code: {Source}</b>"                 
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


