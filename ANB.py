#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.
"""
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, RegexHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    keyboard = [[InlineKeyboardButton("Join Our Group", url = 'www.google.com')] ,
                # InlineKeyboardButton("Option 2", callback_data='2')],

              [InlineKeyboardButton("Press Yes, If you have joined our group", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('''Welcome to ANB referral program!
	
	Please join our annoucment channel and get 100 ANBP to proceed.''', reply_markup=reply_markup)
	


def button(bot, update):
    query = update.callback_query

    bot.send_message(text='''Thanks for joining our group.
	Press /Next to continue.''',chat_id=query.message.chat_id, message_id=query.message.message_id)


def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")
	
def ETH_Wallet(bot, update):
    update.message.reply_text("Please provide your ERC20 Wallet address")
    return ETH_Wallet_Saved
	
def ETH_Wallet_Saved(bot, update):
    user = update.message.from_user
    logger.info("Bio of %s: %s" % (user.first_name, update.message.text))
    update.message.reply_text('Thank you! I hope we can talk again some day.')
	
def Refferal_Link(bot, update):
    update.message.reply_text("Your referral link is")	

def My_Balance(bot, update):
    update.message.reply_text("Your balance is")	

def Refferal_Balance(bot, update):
    update.message.reply_text("Your referral balance is")

def Next(bot, update):
    keyboardtest = [[KeyboardButton("/ETH_Wallet", callback_data='1')] ,
			
					[KeyboardButton("/Refferal_Link", callback_data='2')],

					[KeyboardButton("/My_Balance", callback_data='3')], 
			  
					[KeyboardButton("/Refferal_Balance", callback_data='3')]]

    reply_markup = ReplyKeyboardMarkup(keyboardtest)

    update.message.reply_text('''get your refferal link, balance & referral balance''', reply_markup=reply_markup)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("605110748:AAFxkzGgG-qPVfHWJwqbi-6SA4RYvg0nUVQ")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('Next', Next))
    updater.dispatcher.add_handler(RegexHandler('^ETH_Wallet$', ETH_Wallet))
    updater.dispatcher.add_handler(CommandHandler('Refferal_Link', Refferal_Link))
    updater.dispatcher.add_handler(CommandHandler('My_Balance', My_Balance))
    updater.dispatcher.add_handler(CommandHandler('Refferal_Balance', Refferal_Balance))
    updater.dispatcher.add_handler(CommandHandler('ETH_Wallet_Saved', ETH_Wallet_Saved))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()