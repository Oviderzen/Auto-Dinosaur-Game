import pyautogui

###### Try this script here: https://elgoog.im/t-rex/ ######

###### Use this to fine tune the position of the obstacles based on your screen resolution #######
# print(pyautogui.position())


def jump():
    pyautogui.keyDown('up')


def check_for_cacti() -> bool:
    ### Defined a range to make sure the dino can jump when there is more than one cactus ###
    x = range(-1500, -1480)
    for n in x:
        if pyautogui.pixelMatchesColor(n, 427, (83, 83, 83)):
            return True
    else:
        return False


if __name__ == '__main__':
    while True:
        if check_for_cacti():
            jump()


