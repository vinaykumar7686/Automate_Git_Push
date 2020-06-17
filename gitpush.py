# make sure that the Git bash option is added to context menu and will open by pressing s when context menu is visible
# after running the script be sure to be in the directory that you want to push

import pyautogui as pag,time 

pag.FAILSAFE=False
commitstatement=str(input('Enter the commit message: '))
pag.hotkey('win','down')

def gitPush_Curr():
    time.sleep(3)
    pag.hotkey('shift','f10')
    time.sleep(1)
    pag.hotkey('s')
    time.sleep(1)
    pag.hotkey('enter')
    time.sleep(5)
    pag.hotkey('win'+'up')
    pag.hotkey('win'+'up')
    
    pag.typewrite('git init', interval= 0.1)
    pag.hotkey('enter')
    time.sleep(1)

    pag.typewrite('git add -A', interval= 0.1)
    pag.hotkey('enter')
    time.sleep(1)

    pag.typewrite('git commit -a -m ""',interval= 0.1)
    pag.hotkey('left')
    time.sleep(1)

    pag.typewrite(commitstatement, interval=0.1)
    pag.hotkey('enter')
    time.sleep(1)

    pag.typewrite('git push', interval=0.1)
    pag.hotkey('enter')

gitPush_Curr()

