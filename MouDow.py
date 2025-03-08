import win32api
import win32con
from pynput import keyboard, mouse
import threading
import sys
import os

MOUSE_MOVE_PIXELS = int(input("MOUSE_MOVE_SPEED(Do Not Input 0):"))
MOVE_INTERVAL_MS = int(input("MOVE_INTERVAL_MS(You can Input 0):"))

is_compensation_enabled = False
is_left_button_pressed = False
move_thread = None

def on_press(key):
    global is_compensation_enabled
    if key == keyboard.KeyCode.from_char('g'):
        is_compensation_enabled = not is_compensation_enabled
        print(f"压枪功能 {'开启' if is_compensation_enabled else '关闭'}")

def on_click(x, y, button, pressed):
    global is_left_button_pressed, move_thread
    if button == mouse.Button.left:
        if is_compensation_enabled:
            if pressed:
                is_left_button_pressed = True
                print("MOUSE DOWN: 开始压枪")
                move_thread = threading.Thread(target=move_mouse_down, daemon=True)
                move_thread.start()
            else:
                is_left_button_pressed = False
                print("MOUSE UP: 停止压枪")
                if move_thread and move_thread.is_alive():
                    move_thread.join()

def move_mouse_down():
    while is_left_button_pressed:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, MOUSE_MOVE_PIXELS)
        win32api.Sleep(MOVE_INTERVAL_MS)

def exit_program():
    print("\nEXIT NOW")
    sys.exit()
    os.system("taskkill /f /im MouDow.exe")

def on_key_press(key):
    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            exit_program()
    except AttributeError:
        pass

keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_click)
exit_listener = keyboard.Listener(on_press=on_key_press)

keyboard_listener.start()
mouse_listener.start()
exit_listener.start()

print("鼠标压枪控制器已启动，按 G 键开启/关闭压枪功能，长按鼠标左键进行压枪，按 Ctrl+C 退出")
keyboard_listener.join()
mouse_listener.join()
exit_listener.join()