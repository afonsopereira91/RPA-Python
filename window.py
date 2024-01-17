import pyautogui

window = pyautogui.getActiveWindow()
print(window)
print(window.title)
print(window.size)
print(window.topleft)
print(window.area)

pyautogui.click(window.left + 30, window.top + 50) 