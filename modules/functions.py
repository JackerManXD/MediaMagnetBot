from os import listdir
from os.path import join, isfile, getsize
from modules.global_variables import *

def showFiles(app, msg, usr, name_app):
    
    listfiles = f"**📂 RUTA: `./{usr}`**\n\n"
    totalSize = 0
    fileList = {}
    
    for count, file in enumerate(listdir(usr)):
        count+=1
        if isfile(join(usr, file)):
            link = f"https://{name_app}.onrender.com/file/{usr}/{file}"
            size = round(getsize(join(usr, file)) / 1000024, 2)
        
            if file.endswith("zip") or file.endswith("rar") or file.endswith("7z"):
                listfiles += (f"╭**[/up_{count}] [/rn_{count}] [/dl_{count}] [/th_{count}]**\n")
                listfiles += f"╰📦 **{size} MB - [{file}]({link})**\n\n"
                
            elif file[-3] == "0":
                listfiles += (f"╭**[/up_{count}] [/rn_{count}] [/dl_{count}] [/th_{count}]**\n")
                listfiles += f"╰🧩 **{size} MB - [{file}]({link})**\n\n"
                
            else:
                listfiles += (f"╭**[/up_{count}] [/opciones_{count}]**\n")
                listfiles += f"╰** {size} MB - [{file}]({link})**\n\n"

            totalSize += size
            fileList[count] = join(usr, file)
            
        userFiles[usr] = fileList
    
    msg.reply(listfiles)
        
    