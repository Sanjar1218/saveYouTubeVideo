# django libraries
from django.http import JsonResponse

# python telegram bot libraries
import telegram

TOKEN = '5128554563:AAGXrWFZ8YKt0lSbFpr6X1xo4P14X-L5NjE'
url = 'site to be run'

def setWeebHook(request):
    # for more information about webhook head over to this site
    #https://docs.python-telegram-bot.org/en/stable/telegram.bot.html#telegram.Bot.set_webhook
    
    bot = telegram.Bot(token=TOKEN)
    bot.setWebhook(url)
    return JsonResponse({'status':bot.getWebhookInfo()})

def home(request):
    #telegram bot handlers here

    return JsonResponse({'status':'ok'})