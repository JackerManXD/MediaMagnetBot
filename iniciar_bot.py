import subprocess
import time

comando = ['python3', 'main.py']
proceso = subprocess.Popen(comando)

while True:
    rd = input('Escriba (exit) para salir o presione enter para reiniciar el Bot: \n\n')
    if rd == 'exit':
        proceso.terminate()
        break
    else:
        print('\n\nReiniciando Bot...\n\n')
        proceso.terminate()
        time.sleep(5)
        proceso = subprocess.Popen(comando)
        
    
    
