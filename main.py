# MIS MODULOS
from modules.pyrogram_init import PyrogramInit
from modules.functions import *
from modules.global_variables import *
from modules.download_files import downloadFiles
# MODULOS EXTERNOS
from pyrogram import filters
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup)
from Debug import *
from os.path import exists, join
from os import mkdir

from modules.upload_files import uploadFile

bot = PyrogramInit(PORT=PORT, 
             API_HASH=API_HASH, 
             API_ID=API_ID,
             BOT_TOKEN=BOT_TOKEN)





@bot.app.on_message(filters.command('start'))
def enviar_mensajes(app, m):
    btn = ReplyKeyboardMarkup([
        ['📁 Archivos', '⚙️ Opciones'],
        ['📤 Subir todo', '🗂 Subir album'],
        ['🗑 BORRAR TODO']
    ], resize_keyboard=True)
    
    m.reply('Bienvenido a mi bot :v', reply_markup=btn)
    
    
    
    
    
# VER ARCHIVOS DESCARGADOS --------------------------------------------------------
@bot.app.on_message(filters.regex('📁 Archivos'))
def mostrar_archivos(app, msg):
    if not exists(msg.from_user.username): mkdir(msg.from_user.username)
    showFiles(app, msg, msg.from_user.username, bot.NAME_APP)





# DESCARGAR ARCHIVOS Y VIDEOS ------------------------------------------------------
@bot.app.on_message(filters.regex('http'))
def descargar_archivos(app, msg):
    if not exists(msg.from_user.username): mkdir(msg.from_user.username)
    
    title = downloadFiles(app, msg, msg.from_user.username)
    
    app.send_video(msg.chat.id, join(msg.from_user.username, title))





# OPCIONES DEL ARCHIVO -----------------------------------------------------------------
@bot.app.on_message(filters.regex("/opciones_"))
def opcionesArchivo(app, msg):
    file = userFiles[msg.from_user.username][int(msg.text.split('_')[-1])]
    
    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton('📝 CAMBIAR NOMBRE', callback_data='rename')],
        [InlineKeyboardButton('🚮 ELIMINAR ARCHIVO', callback_data='del_file')],
        [InlineKeyboardButton('🌄 AGREGAR IMAGEN', callback_data='add_thumb')],
    ])

    msg.reply(f'MAS OPCIONES PARA: {file}', reply_markup=btn)





# SUBIR UN ARCHIVO -----------------------------------------------------------------
@bot.app.on_message(filters.regex("/up_"))
def subirArchivo(app, msg):
    file = userFiles[msg.from_user.username][int(msg.text.split('_')[-1])]
    uploadFile(app, msg, file)





bot.iniciar_bot()