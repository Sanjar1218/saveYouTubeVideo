# django libraries
from django.http import JsonResponse
from .models import Links
from .app import *

# python telegram bot libraries
import telegram
from telegram.ext import (
    Updater, 
    Dispatcher,
    MessageHandler, 
    CommandHandler,
    CallbackQueryHandler,
    Filters,
    CallbackContext,
)
import json

TOKEN = '5128554563:AAGXrWFZ8YKt0lSbFpr6X1xo4P14X-L5NjE'
# url to be called when new message arrive in bot
url = 'https://savingbot.pythonanywhere.com/'

bot = telegram.Bot(token=TOKEN, base_url='https://savingvideo.herokuapp.com/bot')

def setWebHook(request):
    # for more information about webhook head over to this site
    #https://docs.python-telegram-bot.org/en/stable/telegram.bot.html#telegram.Bot.set_webhook
    
    
    # print(bot.getWebhookInfo())
    # this changes bots request url to url
    return JsonResponse({'status':bot.setWebhook(url)})

# telegram bot functions here
TOKEN = '5128554563:AAGXrWFZ8YKt0lSbFpr6X1xo4P14X-L5NjE'



def home(request):
    # to logout bot from official site 
    # need to be runs ones befor using it
    # bot.log_out()
    print('requesting')
    print('request')
    # gets data from request that bot sended
    if request.method =='POST':
        print(request.get_full_path())
        print(request.body)
        data = json.loads(request.body.decode())
        # handlers here
        # changing raw data to telegram object
        update = Update.de_json(data, bot)
        print('dispatcher')
        #telegram bot handlers here
        dp = Dispatcher(bot, None, workers=2)
        dp.add_handler(CommandHandler('start', start))
        dp.add_handler(MessageHandler(Filters.entity('url'), named))
        dp.add_handler(CallbackQueryHandler(url_inline_button))

        # this runs ones a time
        dp.process_update(update)
        print('update')
        return JsonResponse({'status': 'ok'})
    
    return JsonResponse({'status':'get'})