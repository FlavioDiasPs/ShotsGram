import pyautogui, telepot
from telepot.loop import MessageLoop
from time import sleep

# Enter your token
TOKEN = ''
# Set your password
PASSWORD = ''

CHECK_ID = None

def handle(data):
    chat_id = data['chat']['id']
    message = data['text']
    response(chat_id, message)

def response(chat_id, message):
    global CHECK_ID, PASSWORD
    if message == '/start':
        if chat_id != CHECK_ID:
            bot.sendMessage(chat_id, 'Digite sua senha utilizando "/password *SUA SENHA*".')
        else:
            bot.sendMessage(chat_id, 'Você já está autenticado.')
    elif '/password' in message:
        if message[10:] == PASSWORD:
            CHECK_ID = chat_id
            bot.sendMessage(chat_id, 'Iniciando monitoramento. Utilize "/screenshot" para visualizar uma captura de tela em tempo real do seu computador.')
        else:
            bot.sendMessage(chat_id, 'Senha incorreta.')
    elif message == '/screenshot':
        if verify_id(chat_id):
            pyautogui.screenshot('screenshot.png')
            bot.sendPhoto(chat_id, open('screenshot.png','rb'))
    else:
        bot.sendMessage(chat_id, 'Comando não interpretado. Use "/screenshot" para visualizar seu desktop ou "/start" para se autenticar.')

def verify_id(chat_id):
    global CHECK_ID
    if chat_id == CHECK_ID:
        return True
    else:
        bot.sendMessage(chat_id, 'Você precisa estar autenticado primeiro. Utilize "/start".')
        return False

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

print('Listening..')

while 1:
    sleep(1)