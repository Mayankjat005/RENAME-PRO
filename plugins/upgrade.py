from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GBGB
	Price 0

        ⚡Cheapest Price In Whole Telegram⚡
 
	**🪙 Basic** 
	Daily  Upload  limit 20GB
	Price Rs 20rs/🌎 0.3$  per Month
	
	**⚡ Standard**
	Daily Upload limit 50GB
	Price Rs 40 ind /🌎 0.5$  per Month
	
	**💎 Pro**
	Daily Upload limit 100GB
	Price Rs 80 ind /🌎 1$  per Month
	
	
	Pay Using Upi I'd `hxbots@sbi`
	
	After Payment Send Screenshots Of 
        Payment To Admin @OO7JATJI"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Admin",url = "https://t.me/OO7JATJI")], 
        			[InlineKeyboardButton("Phone Pay",url = "https://upayme.vercel.app/007jatji@ybl"),
        			InlineKeyboardButton("Paytm Wallet/UPI",url = "https://upayme.vercel.app/007jatji@ybl")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0

        ⚡Cheapest Price In Whole Telegram⚡
 
	**🪙 Basic** 
	Daily  Upload  limit 20GB
	Price Rs 20 ind /🌎 0.3$  per Month
	
	**⚡ Standard**
	Daily Upload limit 50GB
	Price Rs 40 ind /🌎 1.19$  per Month
	
	**💎 Pro**
	Daily Upload limit 100GB
	Price Rs 80 ind /🌎 1$  per Month
	
	
	Pay Using Upi I'd `007jatji@ybl`
	
	After Payment Send Screenshots Of 
        Payment To Admin @OO7JATJI"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Admin",url = "https://t.me/OO7JATJI")], 
        			[InlineKeyboardButton("Phone Pay",url = "https://upayme.vercel.app/007jatji@ybl"),
        			InlineKeyboardButton("Paytm Wallet/UPI",url = "https://upayme.vercel.app/007jatji@ybl")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
