# Automate Desktop Apps
# pip install pynput
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller
keyboard = Controller()
# type 
keyboard.type('Hello World')
# press key
keyboard.press(Key.space)
# release key
keyboard.release(Key.space)
# press combination
keyboard.press(Key.cmd)
keyboard.press('r')
keyboard.release('r')
keyboard.release(Key.cmd)
# Press function keys
keyboard.press(Key.f1)
# Get Pressed Key
with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')
# Get Mouse Position
mouse = Controller()
print(mouse.position)
# Set Mouse Position
mouse.position = (10, 20)
# move mouse
mouse.move(5, -5)
# Left Click
mouse.click(Button.left, 1)
# Right Click
mouse.click(Button.right, 1)
# Scroll
mouse.scroll(0, 2)
# Drag
mouse.press(Button.left)
# Release
mouse.release(Button.left)
# Double Click
mouse.click(Button.left, 2)