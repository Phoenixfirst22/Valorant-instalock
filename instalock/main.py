import pyautogui, keyboard

#import win32api, win32con
#def click(x,y):
    #win32api.SetCursorPos((x,y))
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
#click(1069, 461)
#def move_mouse(x,y):
    #win32api.SetCursorPos((x,y))
print("Made by Phoenixfirst22")
print("https://github.com/Phoenixfirst22")
print("Reyna = 1     | Kayo = 12")
print("Jett = 2      | Sova = 13")
print("Raze = 3      | Fade = 14")
print("Neon = 4      | Skye = 15")
print("Phoenix = 5   | Breach = 16")
print("Yoru = 6      | Gekko = 17")
print("Omen = 7      | Killjoy = 18")
print("Brimstone = 8 | Cypher = 19")
print("Astra = 9     | Chamber = 20")
print("Viper = 10    | Deadlock = 21")
print("Harbour = 11  | Sage = 22")

user_choice = int(input("Agent: "))
if user_choice > int(22):
    print("Please take a displayed number")
    user_choice = int(input("Agent: "))

print("If you have problems, press and hold '#' to end")
list = ["k","reyna","jett","raze","neon","phoenix","yoru","omen","brim","astra","viper","harbour","kayo","sova","fade","skye","breach","gekko","kj","cypher",
        "chamber","deadlock","sage"]

while keyboard.is_pressed("#") == False:
    locate = pyautogui.locateOnScreen("pic/" + list[user_choice] + ".png", confidence=0.99)

    if locate is not None:
        lock = pyautogui.locateOnScreen("pic/lock2.png", confidence=0.94)
        pyautogui.moveTo(locate)
        pyautogui.click()
        pyautogui.click()
        while keyboard.is_pressed("#") == False:
            if lock is not None:
                pyautogui.moveTo(lock)
                pyautogui.click()
                pyautogui.click()
                break
            else:
                continue




    else:
        continue
    break

