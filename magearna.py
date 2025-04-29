import ctypes
import ctypes.wintypes
import time
from pynput import keyboard
from pynput.keyboard import Controller
import keyboard as simplekeyboard

tecla = Controller()

OCR_NORMAL = 32512 
LoadCursorFromFile = ctypes.windll.user32.LoadCursorFromFileW
SetSystemCursor = ctypes.windll.user32.SetSystemCursor

numero_de_skills = 6
teclas_para_bloquear = ['w', 'a', 's', 'd']

# FUNÇOES RELACIONADAS A BLOQUEIOS E DESBLOQUEIOS
def liberar_teclas_pressionadas():
    for teclas in teclas_para_bloquear:
        tecla.release(teclas)

def bloquear_teclado():
    for tecla in teclas_para_bloquear:
        simplekeyboard.block_key(tecla)

def desbloquear_teclado():
    for tecla in teclas_para_bloquear:
        simplekeyboard.unblock_key(tecla)

def bloquear_mouse():
#    tela cheia
    ctypes.windll.user32.ClipCursor(ctypes.byref(ctypes.wintypes.RECT(40, 50, 60, 70)))
# janela
    # ctypes.windll.user32.ClipCursor(ctypes.byref(ctypes.wintypes.RECT(40, 50, 70, 90)))

def desbloquear_mouse():
    ctypes.windll.user32.ClipCursor(None)

# FUNÇOES RELACIONADAS AO USO DAS TECLAS

def pressionar_tecla(teclaEscolhida):
    tecla.press(teclaEscolhida)
    time.sleep(0.1)
    tecla.release(teclaEscolhida)

def combo(numero_de_skills):
    combo = [str(n) for n in range(2, numero_de_skills + 1)] 

    for combo_skill in combo:
       pressionar_tecla(combo_skill)
       time.sleep(0.6) 



#  LISTENER DE TECLAS
def on_press(key):
    
    try:
        # REVIVE (F1)
        if key == keyboard.Key.f1:
            bloquear_mouse()  
            tecla.release(keyboard.Key.f1)

            # CTRL + 1
            tecla.press(keyboard.Key.ctrl)
            pressionar_tecla('1')
            tecla.release(keyboard.Key.ctrl)
            
            time.sleep(0.1)

            # SHIFT + 0
            tecla.press(keyboard.Key.shift)
            pressionar_tecla('0')
            tecla.release(keyboard.Key.shift)
            
            time.sleep(0.1)
            

            # CTRL + 1 novamente
            tecla.press(keyboard.Key.ctrl)
            pressionar_tecla('1')
            tecla.release(keyboard.Key.ctrl)
            time.sleep(0.1)

            # PARAR O POKÉMON
            tecla.press(keyboard.Key.f8)
            tecla.release(keyboard.Key.f8) 
            
            # COLOCAR NO MODO DEFENSIVO PÓS REVIVE PARA LURAR 
            with tecla.pressed(keyboard.Key.alt):
                tecla.press('3')
                tecla.release('3')

            desbloquear_mouse()  
            


        # COMBO (F2)
        if key == keyboard.Key.f2:
            liberar_teclas_pressionadas()
            bloquear_teclado()
            # COLOCAR NO MODO OFENSIVO
            with tecla.pressed(keyboard.Key.alt):
                tecla.press('1')
                tecla.release('1')
            time.sleep(0.1)
            # USAR AS SKILLS
            combo(numero_de_skills)
            desbloquear_teclado()
    

    except AttributeError:
        pass  


# INICIA O LISTENER DO TECLADO
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()